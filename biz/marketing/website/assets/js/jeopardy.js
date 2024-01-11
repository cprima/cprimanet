/**
 * Jeopardy Game Grid Script
 *
 * This script provides functionality to dynamically generate and manage multiple Jeopardy-style game grids.
 * Each grid has a fixed layout of 6 columns, with 1 header row and 4 data rows. The grids are created based 
 * on inline CSV data and are associated with specific container elements.
 *
 * Key Features:
 * - Generates multiple Jeopardy grids with a fixed layout of 6 columns, 1 header row, and 4 data rows.
 * - Dynamically populates grids based on inline CSV data provided for each instance.
 * - Supports tri-state toggling for each cell: showing label, question, or answer.
 * - Allows toggling the entire column to display labels, questions, or answers based on single, double, and triple clicks.
 * - Implements a custom CSV parser that handles quoted fields and escaped quotes within inline CSV data.
 *
 * Usage:
 * 1. Define inline CSV data for each Jeopardy grid early in the HTML document.
 * 2. Queue initialization calls by pushing objects with container IDs and CSV data to `jeopardyInitializations` array.
 * 3. Include this script in the HTML file. The script will process queued initializations and generate grids accordingly.
 * 4. Interact with each grid through mouse clicks to reveal questions and answers.
 *
 * Inline CSV Format:
 * The expected inline CSV format for the data should have trios of label, question, and answer for each column of the Jeopardy grid.
 * Example:
 * label1,question1,answer1,label2,question2,answer2,...
 *
 * Dependencies:
 * This script requires specific HTML structure for each Jeopardy grid container element.
 * The container elements' IDs are to be specified in the queued initialization calls.
 *
 * Author: Christian Prior-Mamulyan <cprior@gmail.com>
 * Created: 2024-01-01
 * License: CC-BY - This work is licensed under a Creative Commons Attribution 4.0 International License.
 */

// Fallback CSV Data
const fallbackCsvData  = `label1,question1,answer1,label2,question2,answer2,label3,question3,answer3,label4,question4,answer4,label5,question5,answer5,label6,question6,answer6
50,question1-50,answer1-50,50,question2-50,answer2-50,50,question3-50,answer3-50,50,question4-50,answer4-50,50,question5-50,answer5-50,50,question6-50,answer6-50
"",question1-100,answer1-100,100,question2-100,answer2-100,100,question3-100,answer3-100,100,question4-100,answer4-100,"","","-",100,question6-100,answer6-100
250,question1-250,answer1-250,250,question2-250,answer2-250,250,question3-250,answer3-250,250,question4-250,answer4-250,250,question5-250,answer5-250,250,question6-250,answer6-250
500,question1-500,answer1-500,500,question2-500,answer2-500,500,question3-500,answer3-500,500,question4-500,answer4-500,500,question5-500,answer5-500,500,question6-500,answer6-500`;

// Function to parse CSV data
function parseCSV(csvString) {
  const rows = csvString.trim().split("\n");
  return rows.map((row) => {
    const regex = /"((?:[^"]|"")*)"|([^,]+)/g;
    const fields = [];
    let match;

    while ((match = regex.exec(row))) {
      if (match[1] !== undefined) {
        fields.push(match[1].replace(/""/g, '"'));
      } else {
        fields.push(match[2]);
      }
    }

    // Group every three fields into an object for label, question, answer
    const groupedFields = [];
    for (let i = 0; i < fields.length; i += 3) {
      groupedFields.push({
        label: fields[i],
        question: fields[i + 1],
        answer: fields[i + 2]
      });
    }

    return groupedFields;
  });
}

// Populate Grid
function populateGrid(rows, containerId) {
  const gridContainer = document.getElementById(containerId);

  // Extracting headers from the first row of rows
  const headers = rows[0].map((item) => item.label);

  // Add headers
  headers.forEach((headerText, columnIndex) => {
    const header = document.createElement("div");
    header.className = `cell header column-${columnIndex}`;
    header.textContent = headerText;
    header.onclick = (event) => toggleColumnQuestions(columnIndex, event);
    gridContainer.appendChild(header);
  });

  // Add questions and answers (starting from the first row)
  rows.slice(1).forEach((row, rowIndex) => {
    row.forEach((item, colIndex) => {
      const cellDiv = document.createElement("div");
      cellDiv.className = `cell question column-${colIndex} row-${rowIndex}`;
      cellDiv.textContent = item.label;
      cellDiv.dataset.state = "label";
      cellDiv.dataset.label = item.label;
      cellDiv.dataset.question = item.question;
      cellDiv.dataset.answer = item.answer;
      cellDiv.onclick = () => toggleCellState(cellDiv);
      gridContainer.appendChild(cellDiv);
    });
  });
}

// Toggle Question/Answer
// deprecated
function toggleQuestionAnswer(element) {
  if (element.dataset.answerShown === "true") {
    element.textContent = element.dataset.question;
    element.dataset.answerShown = "false";
  } else {
    element.dataset.question = element.textContent;
    element.textContent = element.dataset.answer;
    element.dataset.answerShown = "true";
  }
}

// Tri-state toggle function
function toggleCellState(cell) {
  if (cell.dataset.state === "label") {
    cell.textContent = cell.dataset.question;
    cell.dataset.state = "question";
  } else if (cell.dataset.state === "question") {
    cell.textContent = cell.dataset.answer;
    cell.dataset.state = "answer";
  } else {
    cell.textContent = cell.dataset.label;
    cell.dataset.state = "label";
  }
}

// Initialize
function initializeJeopardy(containerId, csvData = fallbackCsvData) {
  // If csvData is not provided or is an empty string, fallbackCsvData will be used
  const dataToUse = csvData.trim() !== '' ? csvData : fallbackCsvData;
  const parsedData = parseCSV(dataToUse);
  populateGrid(parsedData, containerId);
}

// Toggle Questions in a Column
let lastClickTime = 0;
let clickCount = 0;
let clickTimer = null;

function toggleColumnQuestions(columnIndex, event) {
  if (event) {
    event.preventDefault();
  }

  const currentTime = new Date().getTime();
  if (currentTime - lastClickTime < 400) {
    clickCount++;
  } else {
    clickCount = 1;
  }
  lastClickTime = currentTime;

  if (clickTimer) {
    clearTimeout(clickTimer);
  }

  clickTimer = setTimeout(() => {
    const cells = document.querySelectorAll(`.question.column-${columnIndex}`);

    cells.forEach((cell) => {
      if (clickCount === 1) {
        cell.textContent = cell.dataset.label;
        cell.dataset.state = "label";
      } else if (clickCount === 2) {
        cell.textContent = cell.dataset.question;
        cell.dataset.state = "question";
      } else if (clickCount >= 3) {
        cell.textContent = cell.dataset.answer;
        cell.dataset.state = "answer";
      }
    });

    clickCount = 0;
  }, 400);

  if (window.getSelection) {
    window.getSelection().removeAllRanges();
  } else if (document.selection) {
    document.selection.empty();
  }
}

function escapeHTML(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}


// Process any queued initializations
if (window.jeopardyInitializations && window.jeopardyInitializations.length > 0) {
    window.jeopardyInitializations.forEach(init => {
        initializeJeopardy(init.containerId, init.csvData);
    });
}