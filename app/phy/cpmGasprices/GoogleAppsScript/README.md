---
checklists: []
---

# German gas prices by API into Google sheets

## Preprequisites

0. A Google account

1. create an API key at https://creativecommons.tankerkoenig.de/
2. create a Google Sheet, e.g. in Google Drive and note the alphanumerical ID in the URL
3. write in row 1 header cells  date, dateUtc, iso_calendarweek, station_key, station_status, price_e5, price_e10, price_diesel -- the exact spelling doesn't matter. Google Apps Script will simply append the data from the next empty row.
4. create a new project in https://script.google.com/home 
5. Find gas stations in your vincinity with an API call, e.g. in your browser to https://creativecommons.tankerkoenig.de/json/list.php?lat=52.521&lng=13.438&rad=1.5&sort=dist&type=all&apikey=00000000-0000-0000-0000-000000000002 (adapt your lat lon values and the apikey) -- in the code you will need to make a comma-separated string from those

## The code

Copy&paste it in the new Google Script project. Rename the "Unbenanntes Projekt" to something meaningful, it will become an "app" name. The same app name you will see at https://myaccount.google.com/permissions after you granted access permissions in the next step.

## First run

In the Google Script editor windows, click

When asked to "Autorisierung erforderlich Für dieses Projekt ist Ihre Erlaubnis zum Dateizugriff erforderlich." click "Berechtigungen überprüfen" 


## Repeated runs

In the Google Script editor, use in the left menu the "watch" symbol to define a trigger, e.g.

- Choose which function to run: main
- Which runs at deployment: head
- Select event source: time driven
- Select type of time based trigger: minutes timer
- Select minute interval: every 15 min
