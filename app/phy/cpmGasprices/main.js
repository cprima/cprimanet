/**
 * Automated download of gas station prices
 * leveraging tankerkoenig.de API
 *
 * @author: Christian Prior-Mamulyan <cprior@gmail.com>
 * @license: MIT
 *
 * depends on config file containing apikey, ids_csv, output_spreadsheetId, output_sheetname
 */

/**
 * The main function to be called by a trigger
 */
function main() {

  json = fetchJson()
  stations = parseData(json)
  appendData(stations)

}

/**
 * returns json data like
 * {data=MTS-K, ok=true, license=CC BY 4.0 -  https://creativecommons.tankerkoenig.de, prices=
 * {005056ba-7cb6-1ed2-bceb-79dff61a8d26={status=open, e5=1.709, e10=1.649, diesel=1.509}, 
 *  005056ba-7cb6-1ed2-bceb-7a4d9fd46d26={status=open, diesel=1.509, e10=1.649, e5=1.709}}}
 */
function fetchJson() {
  var url = 'https://creativecommons.tankerkoenig.de/json/prices.php'
    + '?apikey=' + apikey + '&ids=' + encodeURIComponent(ids_csv);

  var response = UrlFetchApp.fetch(url, { 'muteHttpExceptions': true }); //todo: try/catch
  return JSON.parse(response)
}

/**
 * iterates json input and maps to target columns in the Google Sheet
 */
function parseData(json) {

  var date = new Date();
  var dateUtc = Utilities.formatDate(date,
    'Etc/GMT',
    'yyyy-MM-dd\'T\'HH:mm:ss.SSS\'Z\'');

  var i = 0;
  var output = [];
  //the response ist not a list of objects but "object of objects"
  for (let key in json['prices']) {
    output.push(['',
      date,
      getWeek(date),
      key,
      json['prices'][key]['status'],
      json['prices'][key]['e5'],
      json['prices'][key]['e10'],
      json['prices'][key]['diesel'],
      dateUtc,
      '-']);
    i++;
  }

  return output;

}

/**
 * depends on config file containing apikey, ids_csv, output_spreadsheetId, output_sheetname
 */
function appendData(data) {

  var sheet = SpreadsheetApp.openById(output_spreadsheetId).getSheetByName(output_sheetname);

  sheet.getRange(sheet.getLastRow() + 1, 1, data.length, data[0].length).setValues(data);
  sheet.getRange(2, 11, sheet.getLastRow() - 1, 1).setFormula('vlookup(D2,mapping_stations!B:J,9,false)'); //easier to set the whole column
  sheet.getRange(2, 12, sheet.getLastRow() - 1, 1).setFormula('B2>today()-L$1');
  sheet.getRange(2, 13, sheet.getLastRow() - 1, 1).setFormula('if(weekdaY(B2)=1,7,weekday(B2)-1)');
  sheet.getRange(2, 14, sheet.getLastRow() - 1, 1).setFormula('vlookup(M2,mapping_weekdays!A:B,2,true)');
  sheet.getRange(2, 15, sheet.getLastRow() - 1, 1).setFormula('if(AND((weeknum(now())-weeknum(B2))<=3,(weeknum(now())-weeknum(B2))>0),TRUE,FALSE)');

}

/*
 * @see: https://stackoverflow.com/a/67570524
 */
function getWeek(date) {
  return Number(Utilities.formatDate(new Date(date), "Europe/Berlin", "u")) === 7 ?
    Number(Utilities.formatDate(new Date(date), "Europe/Berlin", "w")) - 1 : Number(Utilities.formatDate(new Date(date), "Europe/Berlin", "w"));
}

function postToFacebookPage() {
  var output_chartfilename = "test_" + getWeek(new Date()) + ".png";
  var file = DriveApp.getFilesByName(output_chartfilename).next();
  var url = file.getDownloadUrl().replace("&export=download", "");

  var data = {
    "message": "Durchschnittliche Preise E5 ausgewählter Tankstellen",
    "slug": "Letzte 3 volle Wochen zwischen 17:00 und 22:00",
    "link": url
  }

  Logger.log(data)
  response = callFacebookApi(facebook_baseurl + 'feed?access_token=' + facebook_accesstoken,
    'post',
    data);
  Logger.log(response.getContentText());
}

function generateFileInDrive() {
  var output_chartfilename = "test_" + getWeek(new Date()) + ".png";
  var sheet = SpreadsheetApp.openById(output_spreadsheetId).getSheetByName(output_visualization_sheetname);
  var chart = sheet.getCharts()[0];

  chart = chart.modify()
    .setOption('title', "Durchschnittliche Preise E5 ausgewählter Tankstellen")
    .setOption('subtitle', "Letzte 3 volle Wochen zwischen 17:00 und 22:00 bis vor KW " + getWeek(new Date()))
    .setOption('width', 640)
    .setOption('height', 360)
    .build();
  sheet.updateChart(chart);

  var myimage = formatChartAsImage(chart);

  folder = DriveApp.getFolderById(output_spreadsheetId).getParents().next();
  try {
    var file = DriveApp.getFilesByName(output_chartfilename).next();
    Logger.log(file.getId());
    Logger.log(file.getName());
    Logger.log(file.getMimeType());
    var url = file.getDownloadUrl().replace("&export=download", "");
    Logger.log(url);
    //https://stackoverflow.com/a/24226885/9576512
    //Resources > Advanced Google services
    //var foo = Drive.Files.update({ title: file.getName(),mimeType: 'image/png' }, file.getId(), myimage);
  } catch (e) {
    Logger.log("catch");
    var file = folder.createFile(myimage);
    file.setName(output_chartfilename);
    file.setSharing(DriveApp.Access.ANYONE, DriveApp.Permission.VIEW);
    var url = file.getDownloadUrl().replace("&export=download", "");
    Logger.log(url);
  }
}

//charts from a Sheet are formatted unreliably. Better to channel them through a Slide presentation.
function formatChartAsImage(chart) {
  // https://stackoverflow.com/a/60487108

  // Insert sheets chart into slide as an embedded image
  var proxySaveSlide = SlidesApp.openById(temp_slidesID).getSlides()[0];
  var chartImage = proxySaveSlide.insertSheetsChartAsImage(chart, 0, 0, 640, 360);

  // Get image from slides
  var myimage = chartImage.getAs('image/png');

  // Delete image in presentation slide
  chartImage.remove();

  // Return the image
  return myimage;

}


//helper function for the repeated API calls
//url must be the endpoint for the particular call
function callFacebookApi(url, method, payload) {
  var options = {
    'method': method,
    'muteHttpExceptions': true,
    'headers': {
    },
    'contentType': 'application/json'
  };
  if (payload !== false) { options['payload'] = JSON.stringify(payload) }
  return UrlFetchApp.fetch(url, options);
}