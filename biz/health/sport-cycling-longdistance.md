---
layout: page
title:  "my long-distance cycling (learnings)"
categories: [ biz/health/maintenance/sport ]
component: BA_PRO_007
---


todo:

- replenish, not replace
- my change in focus over time
- carbs, fluid, protein, electrolytes, fat


{% include checklist.html checklistnames="preparation, packlist, on-the-road" heading="h2" %}

## Visualizing a GPX recording with custom markers

The following visualizations are based on

- a GPX recording
- with included waypoints adhering to a naming convention
- show
  - the delta or summary of elevation
  - and where food was eaten

{% include gpx.html gpxfilename="/dat/geodata/gpx/2024-08-20-2024-08-20_LDK-WOB.gpx" gpxfilename2="/dat/geodata/gpx/2024-08-20-2024-08-20_LDK-WOB_processed.gpx" %}

{% include gpx.html gpxfilename="/dat/geodata/gpx/2024-08-20-2024-08-20_LDK-WOB.gpx" gpxfilename2="/dat/geodata/gpx/WOB-Gilserberg-LDK_2024-08-31_05-00.gpx" %}

## Solar calculations

-> biz/health/maintenance/sport/2024/09/01/solar-calculations.html

## Bikepacking

I am not a bikepacker.

Here’s a comparison between **Bikepackers** and **Audax/Randonneurs**:

| **Aspect**                 | **Bikepackers**                              | **Audax/Randonneurs**                      |
|----------------------------|----------------------------------------------|--------------------------------------------|
| **Primary Focus**           | Adventure and exploration                    | Endurance and distance riding              |
| **Social Interaction**      | Often solitary, minimal interaction          | Strong community, cooperative group rides  |
| **Attitude Towards Gear**   | Gear-heavy, focused on self-sufficiency      | Minimalist, focused on functionality       |
| **Performance**             | Less emphasis on speed, more on experience   | Focused on consistent, long-distance pace  |
| **Connection to Surroundings** | Deep connection to remote or rugged environments | Engage with local cultures and landscapes  |
| **Mindset**                 | Individualistic, self-reliant                | Collaborative, values shared experience    |
| **Interaction with Other Cyclists** | Sometimes perceived as aloof          | Inclusive, often greet and engage with others |
| **Environmental Focus**     | Nature immersion, often off-road; gear-dependent | Uses human infrastructure like roads/gas stations/cafes     |
| **Ride Objective**          | Personal discovery, off-the-beaten-path      | Time-constrained long-distance events (brevets)       |
| **Cultural Values**         | Focus on adventure as an identity            | Emphasis on endurance, humility, and tradition |

This juxtaposition highlights the key differences in mindset, goals, and approach to cycling between Bikepackers and Audax/Randonneurs.

## (Custom) Bicycle Requirements

My ideal bicycle is built for both performance and reliability, balancing speed with the ability to carry gear over long distances; with versatility in the setup. Performance in this context means to cover distances between two points upwards of 200km.

- Self-Sufficiency: front hub dynamo powering USB charger, for charging devices and navigating in low light, invaluable for multi-day touring

- Frame Versatility: dropouts and mounts for V-brakes and disc brakes; for racks, low-rider, mudguards, bottle cages and kickstand

- Comfort: Flexible steel frame; 3-cross spoke pattern; moderate saddle-to-bar drop; tire size up to 37mm; a handlebar setup with varied positions

## GPS, tracks and OpenStreetMap data

A long-distance cyclist is interested in geodata (like supermarkets, gas stations, bakeries or shelters) close to the planned route. A combination of geodata tools helps to achieve a custom point-of-interest

1. take a track in a GPX file
1. determine (buffered) bounding box
1. use overpass to extract geodata
1. load into QGIS
1. buffer the track
1. clip geodata with buffered track
1. export as GPX (optionally copy into original file)

