

## QGIS project

Project Properties

Background color: blue

Coordinate System: WGS 84 (EPSG:4326)

groups:

- cpm_travel_basemap
  - cultural
  - physical


| **Zoom Level** | **Scale Approx.** | **Usage** |
|--------------|------------------|-----------|
| **1**  | 1:150,000,000  | Global Overview (All years combined) |
| **2**  | 1:75,000,000  | Large-scale regional context |
| **3**  | 1:37,500,000  | Continental view |
| **4**  | 1:25,000,000  | Subcontinental view |
| **5**  | 1:12,500,000  | Single-year overview |
| **6**  | 1:5,000,000  | Major places and routes |
| **7**  | 1:1,000,000  | Cities & Regional Detail |
| **8**  | 1:500,000  | Towns & Local Roads |



?????????????????????????????
QGIS does not use predefined zoom levels like web maps but instead relies on map scale, which varies depending on screen resolution and projection. To approximate zoom levels similar to web maps, QGIS provides the scale_zoom(@map_scale) function, which converts the current scale into a zoom-equivalent value. For example, a scale of 150M corresponds to zoom level 1, 12.5M to zoom level 5, and 1M to zoom level 8. Since QGIS dynamically adjusts the scale based on viewport size and CRS, developers should use @map_scale in expressions or virtual layers to filter data based on zoom-dependent visibility.
?????????????????????????




### Log

Import NaturalEarth
Style consistently

Import plan GPX
Buffer plan GPX (manually adapt?)

Query OSM API for places



## SqliteBrowser


CREATE VIEW "cpm_travel_combined_buffered-S" AS
SELECT ST_Union(geom) AS geom FROM (
    SELECT geom FROM "cpm_travel_2025_plan_buffered-S"
    UNION ALL
    SELECT geom FROM "cpm_travel_2023_track_buffered-S"
    UNION ALL
    SELECT geom FROM "cpr_travel_2014_track_buffered-S"
    UNION ALL
    SELECT geom FROM "cpr_travel_2013_track_buffered-S"
);




