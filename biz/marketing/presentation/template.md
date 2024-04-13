---
layout: presentation_v1.1.0
title: "cprima.net presentation template"
date: 2023-03-25 00:00:00 +0100
abstract: Starting with a definition, digging into individual aspects
excerpt: Starting with a definition, digging into individual aspects
published: true
_titleimagefull: /biz/community/thisyearinrpa/resources/images/trends-from-tags-2022-Q4.png
---

<section>

<section>
  <h2>Some Slide</h2>

  <aside class="notes">
    Shhh, these are your private notes 📝
  </aside>
</section>

<section data-markdown="example.md" data-separator="^\n\n\n"
         data-separator-vertical="^\n\n" data-separator-notes="^Note:">
</section>

</section>

<!-- discussion ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

<section><!-- begin vertical -->

<section data-markdown># Discussion</section>

<style>
.jeopardy-grid-container {
  display: grid;
  grid-template-columns: repeat(6, 1fr); /* 6 columns */
  gap: 10px;
  margin: 20px;
  text-align: center;
  align-items: stretch; /* Make all items in a row stretch to the tallest one's height */
}
.jeopardy-grid-container .cell {
    border: 1px solid #ddd;
    padding: 20px;
    background-color: #eee8d5;
    display: flex; /* Flex layout to allow content to center vertically */
    justify-content: center; /* Center content horizontally */
    align-items: center; /* Center content vertically */
    min-height: 20px; /* Optional: Set a minimum height for shorter cells */
}
.jeopardy-grid-container .header {
  font-weight: bold;
  background-color: #2aa198;
  color: white;
}
.jeopardy-grid-container .question:hover {
  background-color: #fdf6e3;
}
</style>

<section>
<h2>Q&A Jeopardy style</h2>
<div id="jeopardy-grid-container" class="jeopardy-grid-container"></div>
</section>

<script>
<!-- prettier-ignore-start -->
// CSV Data
const csvData = `
One-question,column1answer,Two-Question,column2answer,Three-question,column3answer,Four-question,column4answer,Five-question,column5answer,Six-question,column6answer
"What is the <answer /> to life, the universe and ""everything""?",answer 42,question 2,answer 2,question 3,answer 3,question 4,answer 4,question 5,answer 5,question 6,answer 6
question 1,answer 1,question 2,answer 2,question 3,answer 3,question 4,answer 4,question 5,answer 5,question 6,answer 6
question 1,answer 1,question 2,answer 2,question 3,answer 3,question 4,answer 4,question 5,answer 5,question 6,answer 6
question 1,answer 1,question 2,answer 2,question 3,answer 3,"What is the <answer /> to life, the universe and ""everything""?",answer 42,question 5,"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",question 6,answer 6
`;

// Function to parse CSV data
function parseCSV(csvString) {
  const rows = csvString.trim().split("\n");
  return rows.map((row) => {
    const regex = /"((?:[^"]|"")*)"|([^,]+)/g;
    const fields = [];
    let match;

    while ((match = regex.exec(row))) {
      if (match[1] !== undefined) {
        //fields.push(escapeHTML(match[1].replace(/""/g, '"')));
        fields.push(match[1].replace(/""/g, '"'));
      } else {
        //fields.push(escapeHTML(match[2]));
        fields.push(match[2]);
      }
    }

    return fields;
  });
}

// Populate Grid
function populateGrid(rows) {
const gridContainer = document.getElementById("jeopardy-grid-container");

// Extracting headers from the first row
const headers = rows[0]
.filter((_, index) => index % 2 === 0)
.map((header) => header.replace(/-?_?question/i, "").trim());

// Add headers
headers.forEach((headerText, columnIndex) => {
const header = document.createElement("div");
header.className = `cell header row-0 column-${columnIndex}`;
header.textContent = headerText;
header.onclick = () => toggleColumnQuestions(columnIndex);
gridContainer.appendChild(header);
});

// Add questions and answers (starting from the second row)
rows.slice(1).forEach((row, rowIndex) => {
for (let i = 0; i < 12; i += 2) {
const questionDiv = document.createElement("div");
questionDiv.className = `cell question column-${Math.floor(i / 2)} row-${rowIndex + 1}`;
questionDiv.textContent = row[i];
questionDiv.dataset.answer = row[i + 1];
questionDiv.onclick = () => toggleQuestionAnswer(questionDiv);
gridContainer.appendChild(questionDiv);
}
});
}

// Toggle Question/Answer
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

// Initialize
const parsedData = parseCSV(csvData);
populateGrid(parsedData);

// Toggle Questions in a Column
let lastClickTime = 0;
let clickCount = 0;
let clickTimer = null;

function toggleColumnQuestions(columnIndex) {
// Prevent default double-click behavior (text selection)
if (event) {
event.preventDefault();
}
const currentTime = new Date().getTime();
if (currentTime - lastClickTime < 400) {
// 400 ms for quick successions
clickCount++;
} else {
clickCount = 1;
}
lastClickTime = currentTime;

// Clear the existing timer if it exists
if (clickTimer) {
clearTimeout(clickTimer);
}

clickTimer = setTimeout(() => {
const questions = document.querySelectorAll(
`.question.column-${columnIndex}`
);

    if (clickCount === 2) {
      questions.forEach((questionDiv) => {
        if (questionDiv.dataset.answerShown === "true") {
          toggleQuestionAnswer(questionDiv);
        }
      });
    } else if (clickCount >= 4) {
      questions.forEach((questionDiv) => {
        if (questionDiv.dataset.answerShown !== "true") {
          toggleQuestionAnswer(questionDiv);
        }
      });
    } else {
      questions.forEach((questionDiv) => toggleQuestionAnswer(questionDiv));
    }

    // Reset click count after action
    clickCount = 0;

}, 400); // Delay to allow for subsequent clicks

// Clear any text selection
if (window.getSelection) {
window.getSelection().removeAllRanges();
} else if (document.selection) {
// For older versions of IE
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
<!-- prettier-ignore-end -->
</script>

</section><!-- end vertical -->

<section>
<h2>Intelligent Automation and Low-Code</h2>
<img src="{{ "/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png" | prepend: site.baseurl }}" alt="" class="resize">
</section>

<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<h2 style="position: fixed; bottom: 0; width: 100%; margin: 0px 0px 64px 0px;">bar</h2>
<div class="container">
<div class="col" style="padding-top: 20px; height: 100vh; background-image: linear-gradient(to right, rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,0));"><h3>Code</h3><p style="text-align: left; top: 50%; position: absolute; transform: translateY(-50%); padding-left: 100px; width: 35%;">foo<br />Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</div>
<div class="col"></div>

</div>
</section>

<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<h2 style="position: fixed; bottom: 0; width: 100%; margin: 0px 0px 64px 0px;">bar2</h2>
<div class="container">
<div class="col">&nbsp;
</div>
<div class="col" style="padding-top: 20px; height: 100vh; background-image: linear-gradient(to right, rgba(238,232,213,0), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9));"><h3>Code</h3><p style="text-align: left; top: 50%; position: absolute; transform: translateY(-50%); padding-left: 200px;">foo<br />Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br />baz</p>
</div>

</div>
</section>
<section>
<h2>bar</h2>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png">
<h2>Low-Code and Intelligent Automation</h2>
<p>RPA and Low-Code: Sister technologies in the Intelligent Automation space</p>
<figure>
    <blockquote class="lcap" cite="https://www.example.com">The <strong>Execution</strong> capability … include smart workflow and low-code platforms, and robotic process automation (RPA). This capability is a foundation for end-to-end automated process delivery. It acts as a glue, connecting the technologies across the capabilities.</blockquote>
    <figcaption>Source: <cite>Pascal Bornet et al. (2020) Intelligent Automation,WSPC.</cite></figcaption>
</figure>
</section>

<section>
<h2>The LCAP-Definition — step by step</h2>
<figure>
    <blockquote class="lcap" cite="https://www.gartner.com/reviews/market/enterprise-low-code-application-platform<"><strong>An Enterprise Low-Code Application Platform is</strong> <span class="fragment fade-in-then-semi-out">an application platform that is used to</span><span class="fragment fade-in-then-semi-out"> rapidly develop and deploy</span><span class="fragment fade-in-then-semi-out"> custom applications</span><span class="fragment fade-in-then-semi-out"> by abstracting and minimizing or replacing the coding needed in development.</span><span class="fragment fade-in-then-semi-out"> At a minimum, an LCAP must include:</span><span class="fragment fade-in-then-semi-out"> Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span><span class="fragment fade-in-then-semi-out"> Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span><span class="fragment fade-in-then-semi-out"> Simplified application test, deployment and management.</span></blockquote>
    <figcaption>Source: <cite>https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</cite></figcaption>
</figure>
</section>

<section>
<h2>animate appearance</h2>
<ul>
    <li class="animate__bounceInUp">Add it to any text element</li>
    <li class="animate__bounceInUp">Like list items, or headers.</li>
    <li class="animate__bounceInUp">It adds some attention.</li>
</ul>
</section>

<section class="center present" style="top: 178.5px; display: block;" data-fragment="0" data-appearance-can-start="true">
    <h2>Inside fragments</h2>
    <p class="animate__fadeInDown animate__animated">Like this <span class="animate__fadeInDown animate__faster animate__animated" style="font-size: 0.9em; animation-delay: 300ms;">(click next)</span>:</p>
    <div class="fragment visible current-fragment" data-fragment-index="0">
        <ul>
            <li class="animate__bounceInUp" style="animation-delay: 0ms;">Add it to any text element</li>
            <li class="animate__bounceInUp" style="animation-delay: 300ms;">Like list items, or headers.</li>
            <li class="animate__bounceInUp" style="animation-delay: 600ms;">It adds some attention.</li>
        </ul>
    </div>
</section>

<section class="center present" data-autoappear="" style="top: 137px; display: block;" data-appearance-can-start="true">
                <h2>Autoappear mode</h2><small>Sometimes (for example with Markdown), adding classes to elements is a chore. Appearance can automatically add animation classes to specific elements (tags or other selectors) in the presentation (with the option <code>autoappear</code>) or per slide (with <code>data-autoappear</code>), like this slide.</small>
                <ul>
                    <li class="animate__animated animate__fadeInLeft">This is list item 1</li>
                    <li class="animate__animated animate__fadeInLeft" style="animation-delay: 300ms;">This is list item 2</li>
                    <li class="animate__animated animate__fadeInLeft" style="animation-delay: 600ms;">This is list item 3</li>
                </ul>
                <p><small>Seems not to work when transition via spacebar //CPM</small></p>
</section>

<section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with some text and a [link](https://hakim.se).
    ---
    ## Slide 2
    ---
    ## Slide 3
  </textarea>
</section>

<section data-markdown>
    <script type="text/template">
    <!-- .slide: class="center" -->
    ## Test
        Markdown content
    </script>
</section>

<section data-markdown>
  <script type="text/template">
  <!-- .slide: data-background="#ff0000" -->
    Markdown content
  </script>
</section>

<section data-markdown>
  <script type="text/template">
    ## foo
    - Item 1 <!-- .element: class="fragment" data-fragment-index="2" -->
    - Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->
  </script>
</section>

<section>Horizontal Slide</section>
<section>
    <section>Vertical Slide 1</section>
    <section>Vertical Slide 2</section>
</section>

<section class="center no-bg">
<div style="width: 80%; margin: 0 auto;"><h2 class="r-fit-text">Chapter h2</h2></div>
<p>RPA and Low-Code: Sister technologies in the Intelligent Automation space</p>
</section>

<section data-auto-animate>
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>

<section class="center no-bg" data-auto-animate data-transition="none">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4712 #circle_c1r1 {color: #b48900;  fill: #b48900; transform: translate(1000px, 0px)}
</style>
<svg id="myid4712" width="1280" height="64" version="1.1" viewBox="0 0 1280 64" xmlns="http://www.w3.org/2000/svg" style="">
 <g transform="translate(0,0)">
  <path d="m0,32 h1222" stroke="#586e75" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" />
  <g fill="#cb4b16">
   <circle data-id="circle_c1r1" id="circle_c1r1" cx="32" cy="32" r="32" />
   <circle id="circle_c2r1" cx="437" cy="32" r="32" />
   <circle id="circle_c3r1" cx="842" cy="32" r="32" />
   <circle id="circle_c4r1" cx="1248" cy="32" r="32" />
  </g>
 </g>
</svg>
<h2>&nbsp;</h2>
</section>

<section class="center no-bg" data-auto-animate data-transition="none">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4713 #circle_c1r1 {color: #b48900;  fill: #b48900; transform: translate(0px, 0px)}
</style>
<svg id="myid4713" width="1280" height="64" version="1.1" viewBox="0 0 1280 64" xmlns="http://www.w3.org/2000/svg" style="">
 <g transform="translate(0,0)">
  <path d="m0,32 h1222" stroke="#586e75" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" />
  <g fill="#cb4b16">
   <circle data-id="circle_c1r1" id="circle_c1r1" cx="32" cy="32" r="32" />
   <circle id="circle_c2r1" cx="437" cy="32" r="32" />
   <circle id="circle_c3r1" cx="842" cy="32" r="32" />
   <circle id="circle_c4r1" cx="1248" cy="32" r="32" />
  </g>
 </g>
</svg>
<h2>&nbsp;</h2>
</section>

<section data-auto-animate data-transition="none">
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>

<section class="center no-bg">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4714 #circle_c3r1 {color: #b48900;  fill: #b48900}
</style>
<div id="myid4714">{% include_relative resources/visualizations/drawing.svg %}</div>
<h2>&nbsp;</h2>
</section>
