import os
import math
from lxml import etree

# Haversine function to calculate distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of the Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in meters

# Function to process GPX file and detect terrain features
def process_gpx(file_path, output_dir=None):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()

    # Extract namespaces from the root element
    namespaces = root.nsmap
    default_ns = namespaces.pop(None, '')

    # Register namespaces to use in XPath queries
    etree.register_namespace('default', default_ns)
    for prefix, uri in namespaces.items():
        etree.register_namespace(prefix, uri)

    # Parse trackpoints
    trackpoints = []
    for trkpt in root.xpath('//default:trkpt', namespaces={'default': default_ns}):
        lat = float(trkpt.attrib['lat'])
        lon = float(trkpt.attrib['lon'])
        ele = float(trkpt.find(f'{{{default_ns}}}ele').text)
        time = trkpt.find(f'{{{default_ns}}}time').text
        trackpoints.append({'lat': lat, 'lon': lon, 'ele': ele, 'time': time, 'trkpt': trkpt})

    if len(trackpoints) < 2:
        print("Not enough data points for analysis.")
        return

    # Parse waypoints and filter for Bottom, Peak of Ascend, and Undulating
    bottom_peaks = []
    undulating_segments = []
    waypoints = []
    for wpt in root.xpath('//default:wpt', namespaces={'default': default_ns}):
        lat = float(wpt.attrib['lat'])
        lon = float(wpt.attrib['lon'])
        ele = float(wpt.find(f'{{{default_ns}}}ele').text)
        time = wpt.find(f'{{{default_ns}}}time').text
        name = wpt.find(f'{{{default_ns}}}name').text
        if "Bottom of Ascend" in name or "Peak of Ascend" in name:
            waypoints.append({'lat': lat, 'lon': lon, 'ele': ele, 'time': time, 'name': name})
        elif "Undulating Start" in name or "Undulating End" in name:
            undulating_segments.append({'lat': lat, 'lon': lon, 'ele': ele, 'time': time, 'name': name})

    # Pair Bottoms and Peaks
    for i in range(0, len(waypoints), 2):
        if "Bottom of Ascend" in waypoints[i]['name'] and i + 1 < len(waypoints) and "Peak of Ascend" in waypoints[i + 1]['name']:
            bottom_peaks.append((waypoints[i], waypoints[i + 1]))

    # Map waypoints to the closest trackpoints
    waypoint_to_trackpoint = {}
    for bottom, peak in bottom_peaks:
        for waypoint in [bottom, peak]:
            closest_trackpoint = None
            min_distance = float('inf')
            for trackpoint in trackpoints:
                distance = haversine(waypoint['lat'], waypoint['lon'], trackpoint['lat'], trackpoint['lon'])
                if distance < min_distance:
                    min_distance = distance
                    closest_trackpoint = trackpoint
            if closest_trackpoint:
                waypoint_to_trackpoint[waypoint['name']] = closest_trackpoint

    # Debugging: Print matched waypoints to trackpoints
    for wp_name, tp in waypoint_to_trackpoint.items():
        print(f"Waypoint '{wp_name}' matched to trackpoint with elevation {tp['ele']} meters.")

    # Calculate and insert elevation delta for ascends
    for bottom, peak in bottom_peaks:
        bottom_tp = waypoint_to_trackpoint[bottom['name']]
        peak_tp = waypoint_to_trackpoint[peak['name']]

        elevation_delta = round(peak_tp['ele'] - bottom_tp['ele'])
        print(f"Elevation delta between {bottom['name']} and {peak['name']} is {elevation_delta} meters.")

        # Add TerrainAnalysis to GPX trackpoints
        extensions = bottom_tp['trkpt'].find(f'{{{default_ns}}}extensions')
        if extensions is None:
            extensions = etree.SubElement(bottom_tp['trkpt'], f'{{{default_ns}}}extensions')
        terrain_analysis = etree.SubElement(extensions, 'TerrainAnalysis')
        etree.SubElement(terrain_analysis, 'isBottomOfAscend').text = 'true'

        extensions = peak_tp['trkpt'].find(f'{{{default_ns}}}extensions')
        if extensions is None:
            extensions = etree.SubElement(peak_tp['trkpt'], f'{{{default_ns}}}extensions')
        terrain_analysis = etree.SubElement(extensions, 'TerrainAnalysis')
        etree.SubElement(terrain_analysis, 'isPeakOfAscend').text = 'true'
        etree.SubElement(terrain_analysis, 'ElevationDelta').text = str(elevation_delta)

    # Calculate cumulative elevation gain for undulating segments
    for i in range(0, len(undulating_segments), 2):
        if "Undulating Start" in undulating_segments[i]['name'] and i + 1 < len(undulating_segments) and "Undulating End" in undulating_segments[i + 1]['name']:
            start_segment = undulating_segments[i]
            end_segment = undulating_segments[i + 1]

            start_tp = None
            end_tp = None
            min_distance_start = float('inf')
            min_distance_end = float('inf')

            for trackpoint in trackpoints:
                start_distance = haversine(start_segment['lat'], start_segment['lon'], trackpoint['lat'], trackpoint['lon'])
                end_distance = haversine(end_segment['lat'], end_segment['lon'], trackpoint['lat'], trackpoint['lon'])

                if start_distance < min_distance_start:
                    min_distance_start = start_distance
                    start_tp = trackpoint

                if end_distance < min_distance_end:
                    min_distance_end = end_distance
                    end_tp = trackpoint

            # Calculate the cumulative elevation gain
            cumulative_gain = 0
            is_uphill = False
            if start_tp and end_tp:
                start_index = trackpoints.index(start_tp)
                end_index = trackpoints.index(end_tp)

                for j in range(start_index, end_index):
                    elevation_delta = trackpoints[j + 1]['ele'] - trackpoints[j]['ele']
                    if elevation_delta > 0:
                        cumulative_gain += elevation_delta
                        is_uphill = True

                # Round cumulative gain
                cumulative_gain = round(cumulative_gain)
                print(f"Cumulative elevation gain for undulating terrain from {start_segment['name']} to {end_segment['name']} is {cumulative_gain} meters.")

                if is_uphill and cumulative_gain > 0:
                    # Mark the start of the undulating terrain
                    extensions = start_tp['trkpt'].find(f'{{{default_ns}}}extensions')
                    if extensions is None:
                        extensions = etree.SubElement(start_tp['trkpt'], f'{{{default_ns}}}extensions')
                    terrain_analysis = etree.SubElement(extensions, 'TerrainAnalysis')
                    etree.SubElement(terrain_analysis, 'isBeginOfUndulatingTerrain').text = 'true'

                    # Mark the end of the undulating terrain
                    extensions = end_tp['trkpt'].find(f'{{{default_ns}}}extensions')
                    if extensions is None:
                        extensions = etree.SubElement(end_tp['trkpt'], f'{{{default_ns}}}extensions')
                    terrain_analysis = etree.SubElement(extensions, 'TerrainAnalysis')
                    etree.SubElement(terrain_analysis, 'isEndOfUndulatingTerrain').text = 'true'
                    etree.SubElement(terrain_analysis, 'CumulativeElevationGain').text = str(cumulative_gain)

    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '_processed.gpx'
    output_file_path = os.path.join(output_dir, output_file_name)

    # Write the modified GPX file
    tree.write(output_file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print(f"Processed GPX file saved at: {output_file_path}")

    # Read back the file to ensure it is valid XML
    try:
        read_tree = etree.parse(output_file_path)
        print(f"Successfully parsed the written GPX file: {output_file_path}")
    except etree.XMLSyntaxError as e:
        print(f"Failed to parse the written GPX file: {e}")

# Example usage:
#process_gpx('../../../dat/geodata/gpx/WOB-Warburg-LDK_2024-08-13_2024-08-13.gpx')
process_gpx('./dat/geodata/gpx/WOB-Gilserberg-LDK_2024-08-31_05-00.gpx')
