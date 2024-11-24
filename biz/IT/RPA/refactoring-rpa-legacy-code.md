---
layout: presentation_v1.2.2
theme: solarized
ticker___?: foobar
title: "Gen AI for Power Users"
self-contained: false
excerpt: excerpt
dummycontent: true
titleimagefull: "/app/phy/RPA-publications/ProjectBasturmaBlueprint/images/cprima_pipelines_valves_nodes_fe463353-c3ea-484c-a68c-21ad1189e24e.png"
---

<section>
<h2>Software Quality</h2>
{% include slides/biz_IT_Software-Engineering_resources_slides_softwarequality-ISO25010-table.md %}
</section>

<section>
<section><aside class="notes">…</aside><h2>Learning Objectives</h2>Slide 1</section>

<section><aside class="notes">…</aside><h2>What to Expect</h2>
<p class="stretch" wordcloud-activate="once" wordcloud='{ "minRotation": 0.1, "maxRotation": 0.9, "rotateRatio": 0.8, "rotationSteps": 99, "color": "random-dark", "backgroundColor": "" }'>
30 Power User
20 Expert^2
10 Chat Assistant Web UI
10 Warming Up the Chat
10 Markdown
4 One-Shot Questions
4 Magic
4 theory
4 integrating LLMs
</p>
</section>
<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>

</section>

<section>
<section><aside class="notes">…</aside><h2>Target Audience</h2>Slide 1</section>
<section><aside class="notes">…</aside><h3>Users of AI Chat Assistants</h3>sub slide</section>
</section>

<section>
<section><aside class="notes">…</aside><h2>Typical UI Elements</h2>Slide 1</section>
<section><aside class="notes">…</aside><h3>List of Chats</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Renaming Chats</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Copying Code</h3>sub slide</section>
<section><aside class="notes">Introduce Markdown</aside><h3>Copying Answers</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
</section>

<section>
<section><h2>How to Chat</h2>Slide 1</section>
<section><aside class="notes">…</aside><h3>Warm Up</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Chain Of Thoughts</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Re-Wording Input</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Context</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
</section>

<section>
<section><aside class="notes">…</aside><h2>How to Write</h2>Slide 1</section>

<section data-background-opacity="0.5" data-state="filterblur" data-background="/biz/education/resources/images/bookshelf_1920-1080.png"><aside class="notes">…</aside><h3>Terminology</h3>sub slide</section>

<section class="center" data-background-color="rgb(203,75,22)" data-transition="zoom-in fade-out" data-lower-third='{"visibility": "collapsed", "layout": "two-line", "content": {"line1": "Avoid negations", "line2": "Use \"Do&hellip;_\" instead of \"Do not&hellip;\""}}'><aside class="notes">
Use affirmative directives like 'do', avoiding negative language such as 'don’t'.
</aside><h2 style="margin:0;padding:0;color:#fdf6e3;" class="r-fit-text"><s>&nbsp;Don't&nbsp;</s></h2></section>

<section data-carousel='{"images": ["/tec/phy/Markdown/resources/screenshots/markdownguide.org_homepage.png","/tec/phy/Markdown/resources/screenshots/markdownguide.org_unordered-lists.png","/tec/phy/Markdown/resources/screenshots/markdownguide.org_emphasis.png","/tec/phy/Markdown/resources/screenshots/markdownguide.org_code.png","/tec/phy/Markdown/resources/screenshots/markdownguide.org_fenced-code-blocks.png"], "autoplay": true, "interval": 3000}'><aside class="notes">
https://www.markdownguide.org/getting-started/#what-is-markdown
Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Created by John Gruber in 2004, Markdown is now one of the world’s most popular markup languages.

Using Markdown is different than using a WYSIWYG editor. In an application like Microsoft Word, you click buttons to format words and phrases, and the changes are visible immediately. Markdown isn’t like that. When you create a Markdown-formatted file, you add Markdown syntax to the text to indicate which words and phrases should look different.

https://www.markdownguide.org/getting-started/#why-use-markdown
Markdown is everywhere.
Markdown can be used for everything. People use it to create websites, documents, notes, books, presentations, email messages, and technical documentation.
Markdown is future proof.

</aside><h3>Markdown Syntax</h3><div class="carousel-container r-stretch"></div></section>
<section><aside class="notes">
</aside><h3>Markdown with AI Chat Assistants</h3>
<div class="container">
<div class="col">
<a href="https://cpr.in-berlin.de/utils/iframe.php?url=https://www.markdownguide.org/basic-syntax/#unordered-lists" data-modal-type="iframe">What is Markdown</a>
</div>
<div class="col" style="text-align: left;"><p>Used to add formatting elements to plaintext text documents</p>
<p><b>Quotation Marks (" "):</b><br />Use these to specify exact phrases or words.</p>
<p><b>Brackets ([ ]):</b><br />Use these to include optional information or clarifications.</p>
<p><b>Parentheses ( ):</b><br />Use these for additional details or notes.</p>
<p><b>Braces ({ }):</b><br />Use these to group related information or commands.</p>
<p><b>Pipes (|):</b><br />Use these to separate multiple options or items.</p>
</div></div>
</section>

<section><aside class="notes">
When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

XML tip: Use tags like &lt;instructions&gt;, &lt;example&gt;, and &lt;formatting&gt; to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.
?
Why use XML tags?
Clarity: Clearly separate different parts of your prompt and ensure your prompt is well structured.
Accuracy: Reduce errors caused by Claude misinterpreting parts of your prompt.
Flexibility: Easily find, add, remove, or modify parts of your prompt without rewriting everything.
Parseability: Having Claude use XML tags in its output makes it easier to extract specific parts of its response by post-processing.
There are no canonical &ldquo;best&rdquo; XML tags that Claude has been trained with in particular, although we recommend that your tag names make sense with the information they surround.
?
Tagging best practices
Be consistent: Use the same tag names throughout your prompts, and refer to those tag names when talking about the content (e.g, Using the contract in &lt;contract&gt; tags...).
Nest tags: You should nest tags &lt;outer&gt;&lt;inner&gt;&lt;/inner&gt;&lt;/outer&gt; for hierarchical content.
Power user tip: Combine XML tags with other techniques like multishot prompting (&lt;examples&gt;) or chain of thought (&lt;thinking&gt;, &lt;answer&gt;). This creates super-structured, high-performance prompts.

https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags

</aside><h3>XML tags</h3>
Use tags like &lt;instructions&gt; or &lt;example&gt; to clearly separate different parts of your prompt.
</section>

<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
</section>

<section>
<section><aside class="notes">…</aside><h2>Observations</h2>Slide 1</section>
<section><aside class="notes">…</aside><h3>Terminology</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Expertise</h3>sub slide</section>
<section><aside class="notes">Anecdote: from bash to PowerShell</aside><h3>Transfer of Expertise</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Past Chats</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Integrated AI or Web UI</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Caveats</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Knowledge Management</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
</section>

<section>
<section><aside class="notes">…</aside><h2>Theory</h2>Slide 1</section>
<section><aside class="notes">…</aside><h3>Hallucinations</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Multishot Prompts</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Chain-of-Thoughts</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>System Prompts</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>Context</h3>sub slide</section>
<section><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
</section>

<section>
<section data-lower-third='{"visibility": "collapsed", "layout": "two-line", "content": {"line1": "Title", "line2": "Subtitle"}}'><aside class="notes">…</aside><h3>tbd</h3>sub slide</section>
<section data-ticker='{"visibility": "visible", "tickertext": "foobar" }' ><h3>Slide 3</h3></section>
<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<div class="container">
<div class="col" style="padding-top: 20px; height: 100vh; background-image: linear-gradient(to right, rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,0));">
<h2>Code</h2>
<p style="text-align: left; top: 50%; position: absolute; transform: translateY(-50%); padding-left: 100px; width: 35%;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</div>
<div class="col"></div>
</div>
</section>
</section>

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
<h3>foo</h3>
<div id="chat-container" class="stretch r-stretch"></div>

<style>
#chat-container {
max-width: 1280px;
margin: 0 auto;
overflow-y: auto;
height: 500px;
border: 1px solid #93a1a1; /_ Solarized base1 _/
padding: 10px;
border-radius: 5px;
background-color: #eee8d5; /_ Solarized base2 _/
}

.message {
padding: 10px;
margin: 10px 0;
border-radius: 8px;
transition: transform 0.3s ease, opacity 0.3s ease;
max-width: 75%; /_ Limit message width _/
clear: both;
}

.message.question {
background-color: #268bd2; /_ Solarized blue _/
color: #fdf6e3; /_ Solarized base3 _/
text-align: right;
float: right;
}

.message.answer {
background-color: #2aa198; /_ Solarized cyan _/
color: #fdf6e3; /_ Solarized base3 _/
text-align: left;
float: left;
}

.message pre {
background-color: #073642; /_ Solarized base02 _/
color: #839496; /_ Solarized base0 _/
padding: 5px;
border-radius: 5px;
overflow-x: auto;
white-space: pre-wrap;
}

.message.emoji {
font-size: 1.2em;
}

/_ Ensure smooth, modern transitions _/
.message.appear {
opacity: 0;
transform: translateY(20px);
}

.message.visible {
opacity: 1;
transform: translateY(0);
}

/_ Ensure chat scrolling has smooth, readable motion _/
#chat-container {
scroll-behavior: smooth;
}

</style>

<!-- Embedding JSON data -->
<script id="chat-data" type="application/json">
[
    {
    "type": "question",
    "content": "How can I reverse a string in Python?",
    "styled": true
    },
    {
    "type": "answer",
    "content": "You can reverse a string using slicing. Here's an example:\n\n```python\nmy_string = 'hello'\nreversed_string = my_string[::-1]\nprint(reversed_string)  # Output: 'olleh'\n```",
    "code": true
    },
    {
    "type": "question",
    "content": "Got it! 😊 What about removing duplicates from a list?",
    "emoji": true
    },
    {
    "type": "answer",
    "content": "To remove duplicates, convert the list to a set and back to a list:\n\n```python\nmy_list = [1, 2, 2, 3, 4, 4, 5]\nunique_list = list(set(my_list))\nprint(unique_list)  # Output: [1, 2, 3, 4, 5]\n```",
    "code": true
    },
    {
    "type": "question",
    "content": "Is there a way to maintain the order?",
    "styled": true
    },
    {
    "type": "answer",
    "content": "Yes! You can use a loop to preserve order:\n\n```python\nmy_list = [1, 2, 2, 3, 4, 4, 5]\nunique_list = []\n[unique_list.append(x) for x in my_list if x not in unique_list]\nprint(unique_list)  # Output: [1, 2, 3, 4, 5]\n```",
    "code": true
    }
]
</script>

<script>

<!-- prettier-ignore-start -->
// Fetch the JSON data embedded in the HTML
const chatDataScript = document.getElementById("chat-data");
const chatData = JSON.parse(chatDataScript.textContent);

// Function to render the chat data
function renderChat(chatData) {
    const chatContainer = document.getElementById("chat-container");

    chatData.forEach((message) => {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", message.type);
        
        if (message.styled) {
            messageElement.style.fontStyle = "italic"; // example styling
        }

        if (message.code) {
            messageElement.innerHTML = `<pre><code>${message.content}</code></pre>`;

        } else {
            messageElement.textContent = message.content;
        }

        chatContainer.appendChild(messageElement);
    });

}

// Initialize chat rendering
renderChat(chatData);

<!-- prettier-ignore-end -->

</script>

</section>
