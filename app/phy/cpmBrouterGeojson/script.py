import json
import os
import pandas as pd
import gpxpy
import gpxpy.gpx

def read_brouter_geojson(file_path, time_in_milliseconds=False):
    # Load the GeoJSON data from the file
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)
    
    # Extract the relevant features
    features = geojson_data['features'][0]
    times = features['properties']['times']  # Cumulative times (already accumulated)
    coordinates = features['geometry']['coordinates']  # Coordinates (longitude, latitude, elevation)

    # Create a DataFrame from the coordinates (longitude, latitude, elevation)
    coordinates_df = pd.DataFrame(coordinates, columns=['Longitude', 'Latitude', 'Elevation'])
    
    # Add the cumulative time to the DataFrame, time starts at 0 for the first point
    times_with_initial = [0] + times  # Add 0 for the first point
    coordinates_df['Cumulative Time (seconds)'] = times_with_initial
    
    # If the time is in milliseconds, convert it to seconds
    if time_in_milliseconds:
        coordinates_df['Cumulative Time (seconds)'] = coordinates_df['Cumulative Time (seconds)'] / 1000

    # Convert time from seconds to hours for easier comparison
    coordinates_df['Cumulative Time (hours)'] = coordinates_df['Cumulative Time (seconds)'] / 3600
    
    return coordinates_df

def ensure_directory_exists(file_path):
    # Ensure the directory for the file exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

def export_to_csv(df, csv_path):
    ensure_directory_exists(csv_path)
    df.to_csv(csv_path, index=False)
    print(f"Data successfully exported to {csv_path}")

def export_to_gpx(df, gpx_path):
    ensure_directory_exists(gpx_path)
    
    # Create a GPX object
    gpx = gpxpy.gpx.GPX()

    # Add track
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    # Add segment to the track
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Add points to the segment
    for index, row in df.iterrows():
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(row['Latitude'], row['Longitude'], elevation=row['Elevation']))

    # Write to a GPX file
    with open(gpx_path, 'w') as f:
        f.write(gpx.to_xml())
    print(f"Data successfully exported to {gpx_path}")

def extract_waypoints_by_nth_hour(coordinates_df, n):
    # Find the coordinates where cumulative time crosses each n-th hour
    nth_hour_mark = n
    nth_hour_marks = []
    for index, row in coordinates_df.iterrows():
        if row['Cumulative Time (hours)'] >= nth_hour_mark:
            nth_hour_marks.append({
                'Hour': nth_hour_mark,
                'Longitude': row['Longitude'],
                'Latitude': row['Latitude'],
                'Elevation': row['Elevation'],
                'Cumulative Time (hours)': row['Cumulative Time (hours)']
            })
            nth_hour_mark += n  # Increase by n hours

    # Create a DataFrame with the extracted waypoints
    waypoints_df = pd.DataFrame(nth_hour_marks)
    return waypoints_df

# Main function that takes n-th hour as a parameter
def process_brouter_data(file_path, n, time_in_milliseconds=False):
    # Read the GeoJSON data
    coordinates_df = read_brouter_geojson(file_path, time_in_milliseconds)
    
    # Extract waypoints where cumulative time crosses each n-th hour
    waypoints_df = extract_waypoints_by_nth_hour(coordinates_df, n)

    # Create output filenames based on the n-th hour
    csv_path = f'./output/brouter_waypoints_{n}th_hour.csv'
    gpx_path = f'./output/brouter_waypoints_{n}th_hour.gpx'

    # Export waypoints to CSV
    export_to_csv(waypoints_df, csv_path)

    # Export waypoints to GPX
    export_to_gpx(waypoints_df, gpx_path)

# Example usage
file_path = './dat/geodata/gpx/geojson/brouter.geojson'  # Replace with your actual file path
n = 8  # Replace with the desired n-th hour interval
time_in_milliseconds = False  # Set to True if time is in milliseconds

# Process the data for every n-th hour
process_brouter_data(file_path, n, time_in_milliseconds)
