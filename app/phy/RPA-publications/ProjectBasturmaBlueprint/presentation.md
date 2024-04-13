---
layout: presentation_v1.2.0
title: "CI/CD with UiPath RPA"
date: 2024-01-01 00:00:00 +0100
abstract: Project Basturma Pipelines
excerpt: Excerpt
published: true
_titleimagefull: /biz/community/thisyearinrpa/resources/images/trends-from-tags-2022-Q4.png
---

<section><!-- begin vertical -->

<!-- Intro/frame/act1/hook/…
//
//
//
//
//
//-->

<section data-markdown># The situation
Note:
This will only display in the notes window.</section>

<section data-markdown>
## RPA 2024

- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>
## The state of UiPath RPA delivery in 2024

- mature vendor ecosystem
- 5+ years of experience commonly available
- legacy RPA code and new code

- adoption of industry best practices lagging
- low code abstracts away fundamentals

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## What is DevOps

- DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.
- DevOps is complementary with Agile software development; several DevOps aspects came from Agile methodology.
- DevOps is a culture, movement, or practice that emphasizes the collaboration and communication of both software developers and other information-technology (IT) professionals while automating the process of software delivery and infrastructure changes.

- DevOps CALMS: Culture, Automation, Lean, Measurement, Sharing

- DevOps infinity loop: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## DevOps for RPA

- many initiatives
- vendor tool

### eat your own dog food

- DevOps contains "Automation" which in turn requires standardization
- DevOps for (not just) RPA is based on standardzing source code management (Git)
- …

### pro CI/CD for RPA

- automate the RPA delivery pipeline: eat your own dog food
- raise the bar, raise the value, raise the price?
- governance, compliance, security
- …

Note:
This will only display in the notes window.

- No Git expert? No CI/CD!

</section>

<section data-markdown data-background="/biz/marketing/keyvisuals/eat-own-dogfood.png">
</section>

<section data-markdown>

## contra CI/CD for RPA

- RPA is low code and should not be treated as software development
- skills gap
- …

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!-- section data-markdown># About</section //-->

<section>
<h2>About</h2>
<span class="r-fit-text">
<p>Nicht erst in der Phase "Operations" nach Abschluß des initialen "Development" können RPA Projekte von einer CI/CD-Pipeline profitieren:
Den RPA Code automatisiert in Pakete zu bauen, auf Herz oder auch auf Nieren zu testen und in einen Feed für den Orchestrator (Tenant) zu deployen, um das build-Projekt oder einen Change zu releasen, das sollte nicht nur auf dem Fundament einer Automatisierung beruhen, sondern erfodert überraschenderweise auch einen kulturellen Überbau.</p>

<p>CI/CD steht für Continous Integration, Continous Delivery (oder auch Continous Deployment).</p>

<p>Übertragen auf UiPath RPA Projekte besteht eine solche Pipeline aus Bausteinen wie</p>

<ul>
<li>Umgang mit der Versionsnummer (im Semantic Versioning Schema)</li>
<li>einem strukturierten Umgang mit der Quellcodeverwaltung, bsw in Git repositories</li>
<li>der Chance auf vollautomatisierte Code-Qualitäts-Analysen</li>
<li>und einem fein granularen Blick auf jeden Schritt zwischen drag&drop-Programmierung und der Ausführung auf einem Roboter</li>
</ul>

<p>In diesem Beitrag soll in schneller Folge zwischen Vogelperspektive und Codezeilen gewechselt werden, um die Chancen und Herausforderungen einer CI/CD-Pipeline für UiPath RPA Projekte einschätzen zu können.</p>
</span>
</section>

<section data-markdown>

## About Me

- Nothing to sell, just here to share my experience
- content based on personal research in my free time

Note:
This will only display in the notes window.

</section>

<style>
        .pillars-container {
            display: flex;
            flex-direction: column; /* Stack elements vertically */
            align-items: center;
            background-color: #eee8d5; /* Lighter shade for container background */
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            color: #fdf6e3;
        }

        .pillars-container .roof-container {
            width: 100%;
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
          margin-bottom: 20px;
        }

        .pillars-container .roof {
            width: calc(100% - 10px); /* Adjust as needed */
            height: 30px; /* Height of the triangle */
            background-color: #b58900; /* Roof color */
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%); /* Triangle shape */
            display: flex;
            justify-content: center;
        }

        .pillars-container .roof-text {
            width: 100%; /* Full width */
            background-color: #b58900; /* Same color as the roof */
            text-align: center;
            padding: 10px 0;
          margin-top: -1px;
            border-radius: 5px; /* Rounded bottom right corner */
        }

        .pillars-container .pillars {
            display: flex;
            justify-content: space-around;
            width: 100%;
            min-height: 350px; /* Minimum height */
            max-height: 800px; /* Maximum height */
            overflow: auto; /* Enable scrolling if content exceeds max height */
        }

        .pillars-container .pillar {
            width: 15%; /* Adjusted width for each pillar */
            border-radius: 5px;
            background-color: #93a1a1; /* Default pillar color */
            margin: 0 1%; /* Space between pillars */
            color: #002636;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0px;
            font-size: 60%; /* Set the font size to 60% inside the pillar */

        }
        .pillars-container .pillar ul {
            padding-left: 10px;
            padding-bottom: 10px;
        }

        .pillars-container .pillar .label, .pillars-container .pillar .sub-label {
            background-color: #657b83; /* Label background */
            width: 100%;
            padding: 5px 0; /* Padding for the label */
            text-align: center;
            color: #fdf6e3;
            font-size: 1.4em;
        }

        .pillars-container .pillar .label {
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }

        .pillars-container .pillar .sub-label {
            font-size: 80%; /* Smaller font size for sub-label */
            margin-top: -1px;
        }

        .pillars-container .foundation {
            display: flex; /* Enable flexbox */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            background-color: #586e75; /* Foundation color */
            width: calc(100% - 20px); /* Adjusted to the padding of the container */
            height: 50px; /* Height of the foundation */
            border-radius: 5px;
            margin-top: 20px; /* Space between pillars and foundation */
            text-align: center; /* Centering text inside the foundation */
        }
</style>

<section>

    <h2>In Scope: Culture, Code, Build, Release</h2>

<div width="90%">
    <div class="pillars-container">
        <div class="roof-container fragment fade-up">
            <div class="roof"></div>
            <div class="roof-text">Culture</div>
        </div>
        <div class="pillars">
            <div class="pillar fragment fade-up">
                <div class="label">Code</div>
                <!-- div class="sub-label">Sub-Label 1</div -->
<ul>
<li>Git template repo(s)</li>
<li>manual Workflow Analyzer</li>
<li>automated Workflow Analyzer on push</li>
<li>code review(s)</li>
<li>Git workflow</li>
<li>Configurability</li>
</ul>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Build</div>
                <!-- div class="sub-label">Sub-Label 2</div -->
<ul>
<li>version number increment</li>
<li>project.json</li>
<li>handle process vs. library, dependencies</li>
<li>build scripts</li>
<li>build runner(s)</li>
<li>build trigger(s)</li>
<li>uipcli.exe</li>
</ul>
            </div>
            <div class="pillar fragment fade-up" style="background-color: #839496 !important; color: #073642;">
                <div class="label" style="color: #eee8d5;">Test</div>
                <!-- div class="sub-label">Sub-Label 3</div -->
<ul>
<li>(automated testing)</li>
<li>(Canary?)</li>
<li style="text-decoration: line-through">user acceptance testing</li>
</ul>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Release</div>
                <!-- div class="sub-label">Sub-Label 4</div -->
<ul>
<li>publish to Orchestrator test tenant feed(!)</li>
<li>publish to Orchestrator prod tenant feed(!)</li>
<li>deployment script(s)</li>
</ul>
            </div>
            <div class="pillar fragment fade-up" style="background-color: #839496 !important; color: #073642;">
                <div class="label" style="color: #eee8d5;">Deploy</div>
                <!-- div class="sub-label">Sub-Label 5</div -->
<ul>
<li>Staging Environment Testing</li>
<li>approvals, schedule</li>
<li>set active version prod tenant</li>
<li>Smoketest</li>
</ul>
            </div>
        </div>
        <div class="foundation fragment fade-up">Automation<span style="font-size: 60%;"> </span></div>
        <!-- div class="foundation fragment fade-up">Lean IT</div -->
        <!-- div class="foundation fragment fade-up">Measure</div -->
        <!-- div class="foundation fragment fade-up">Share</div -->
    </div>
</div>
<aside class="notes">
This will only display in the notes window.
</aside>
</section>

<section data-markdown data-background="/biz/marketing/keyvisuals/TOGAF-Cube_Business-Data-Application-Technology_Vision-ArchitectureDomain-BuildingBlocks.svg">

Note:
Some slides will be about building blocks, some about the vision, some in between.

</section>

<section data-markdown>

## Further reading

- https://github.com/rpapub/project-basturma-pipelines
- presentation: …

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!-- the technology, off-the-shelf
//
//
//
//
//
//-->

<section data-markdown># What is out there?</section>

<section data-markdown data-background="/biz/IT/resources/DevOps_CALMS-circles.png">

## DevOps Framework(s)

Note:
This will only display in the notes window.

- CALMS

</section>

<section data-markdown data-background="/biz/IT/resources/DevSecOps-infinity.svg">
## Devops inifinity loop

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## tools

- Jenkins
- GitHub
- Azure DevOps
- GitLab
- UiPath
  - Orchestrator
  - uipcli.exe
  - …
- Git
- Postman
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### UiPath RPA platform

- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## .NET specifics

- NuGet feed(s)
- UiPath project.json
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## concepts

- SemVer
- …

Note:
This will only display in the notes window.

</section>

<section>
<h2>project.json</h2>
<pre><code data-line-numbers="2-3|4|16|37|49-51|60,48" style="max-height: 600px">{
  "name": "BlankProcess",
  "description": "Blank Process",
  "main": "Main.xaml",
  "dependencies": {
    "UiPath.Excel.Activities": "[2.20.2]",
    "UiPath.Mail.Activities": "[1.20.3]",
    "UiPath.System.Activities": "[23.4.5]",
    "UiPath.Testing.Activities": "[23.4.1]",
    "UiPath.UIAutomation.Activities": "[23.4.8]"
  },
  "webServices": [],
  "entitiesStores": [],
  "schemaVersion": "4.0",
  "studioVersion": "23.4.5.0",
  "projectVersion": "1.2.103",
  "runtimeOptions": {
    "autoDispose": false,
    "netFrameworkLazyLoading": false,
    "isPausable": true,
    "isAttended": false,
    "requiresUserInteraction": true,
    "supportsPersistence": false,
    "workflowSerialization": "DataContract",
    "excludedLoggedData": [
      "Private:*",
      "*password*"
    ],
    "executionType": "Workflow",
    "readyForPiP": false,
    "startsInPiP": false,
    "mustRestoreAllDependencies": true,
    "pipType": "ChildSession"
  },
  "designOptions": {
    "projectProfile": "Developement",
    "outputType": "Process",
    "libraryOptions": {
      "includeOriginalXaml": false,
      "privateWorkflows": ""
    },
    "processOptions": {
      "ignoredFiles": ""
    },
    "fileInfoCollection": [],
    "modernBehavior": true
  },
  "expressionLanguage": "VisualBasic",
  "entryPoints": [
    {
      "filePath": "Main.xaml",
      "uniqueId": "25ae295d-22df-4044-a699-d0614d9feffd",
      "input": "",
      "output": ""
    }
  ],
  "isTemplate": false,
  "templateProjectData": {},
  "publishData": {},
  "targetFramework": "Windows"
}
</code></pre>
<aside class="notes">
This will only display in the notes window.
</aside>
</section>

<section data-markdown>

## foo

- bar

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!-- the examples, applied to UiPath RPA, …
//
//
//
//
//
//-->

<section data-markdown># CI/CD for UiPath RPA
Note:
This will only display in the notes window.
</section>

<section data-markdown>

## [Culture] How much complexity?

- LowCode vs. "HighCode"
- upskilling paths
- prerequisites "Git"
- …

Note:
This will only display in the notes window.

</section>

<section>
<h2>Git can be a beast</h2>
<div class="r-stack">
  <img class="fragment" src="/tec/phy/Git/assets/images/octocat-morph-cute-to-ugly_1of4.png" width="960" height="540">
  <img class="fragment" src="/tec/phy/Git/assets/images/octocat-morph-cute-to-ugly_2of4.png" width="960" height="540">
  <img class="fragment" src="/tec/phy/Git/assets/images/octocat-morph-cute-to-ugly_3of4.png" width="960" height="540">
  <img class="fragment" src="/tec/phy/Git/assets/images/octocat-morph-cute-to-ugly_4of4.png" width="960" height="540">
</div>

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [**CODE**] [build] [test] [release] [deploy]
//
//-->

<section data-markdown>## Deepdive Code</section>

<section data-markdown>

### [Code, Culture] Beyond the UiPath Studio

- new projects should NOT start in UiPath Studio but in a version control system
- Use separate Git client (GUI or CLI) to manage the code
- Soft-enforce Workflow Analyzer

Note:
Never create a project in UiPath Studio. Rather from a e.g. GitHub template to achieve:

- defined project.json (dependencies, …), .gitignore, CI/CD pipeline readiness, branch conventions, …

Git Clients:

- GitHub Desktop
- GitKraken
- SourceTree
- TortoiseGit
- Git CLI

</section>

<section data-markdown>

### [Culture] Code Review

- It's really a culture thing
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### [Code] Modern

1. Process
2. Library (Object Repository!)
3. …

Note:
Since Object Repository availability: towards more library projects

</section>

<section data-markdown>

### [Code, Automation] Git & Compagnie

- automated Workflow Analyzer: "Static Code Analysis"
- defined branching strategy
- defined commit message conventions
- Git vs. GitHub/GitLab/…
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### [Code] deepdive: Static Code Analysis

- low hanging fruit
- template quality!
- …

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [code] [**BUILD**] [test] [release] [deploy]
//
//-->

<section data-markdown>## Deepdive Build</section>

<section data-markdown>

### [Code, Automation] project.json projectVersion

- SemVer? Really?
- increment: human or automation? Pre or post build?
- automated commit?
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### [Automation] build runners

- Windows
- uipcli.exe vs. UiPath Studio
- self-hosted vs. SAAS
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### [Automation] build script(s)

- custom
- skills needed to develop and maintain
- continous integration (triggered by commit)
- test and production builds
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### [Code, Build, Automation] Dependencies and Libraries

- libraries are built differently
- library naming conventions and dependency management
- …
- dependency substitution necessary? (depends on naming scheme e.g. Object Repository Descriptor) Libraries

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [code] [test] [**TEST**] [release] [deploy]
//
//-->

<section><h2>Deepdive Test</h2><span class="r-fit-text">Out of Scope</span><aside class="notes">This will only display in the notes window.</aside></section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [code] [build] [test] [**RELEASE**] [deploy]
//
//-->

<section data-markdown>## Deepdive Release</section>

<section data-markdown>

### hands-on

- publish UiPath Orchestrator feed(s)
- can be automated without UiPath Studio (uipcli.exe)
- can be automated via API calls to UiPath Orcehstrator API

### RPA pecularities

- delta test and prod environments
- to be discussed: test after release?

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [code] [build] [test] [release] [**DEPLOY**]
//
//-->

<section><h2>Deepdive Deploy</h2><span class="r-fit-text">Out of Scope</span><aside class="notes">This will only display in the notes window.</aside></section>

</section><!-- end vertical -->

<!-- the demo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

<section><!-- begin vertical -->

<section data-markdown># Demo</section>

<section data-markdown>

## foo

- bar
- baz

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<!-- the call to action ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

<section><!-- begin vertical -->

<section data-markdown># What's next?</section>

<section data-markdown>

## Some Thoughts

- It's a culture, not a product, not a tool
- Tt's am upskilling journey, not a destination

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

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
<div id="jeopardy-grid-container1" class="jeopardy-grid-container"></div>
</section>

<style>
/* body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #fdf6e3;
  color: #657b83;
  line-height: 1.6;
  margin: 0;
  padding: 0;
}*/

#carousel-container {
  margin: auto;
  position: relative;
  background-color: #eee8d5; /* Solarized Light secondary background */
}

#carousel-container .carousel-item {
  display: none;
  position: relative;
  color: #657b83; /* Solarized Light primary text */
}

#carousel-container .carousel-item img {
  width: 100%;
  height: auto;
}

#carousel-container .text-overlay {
  position: absolute;
  bottom: 0;
  background: rgba(0, 43, 54, 1.0); /* Solarized Dark background with transparency */
  color: #eee8d5; /* Solarized Light text */
  width: 100%;
  text-align: center;
}

#carousel-container .carousel-navigation {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
}

#carousel-container .nav-element, #carousel-container .nav-dot {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 25px;  /* Standardized width for all navigation elements */
  height: 25px; /* Standardized height for all navigation elements */
  margin: 0 5px;
  cursor: pointer;
  font-size: 20px; /* Font size adjusted for nav-element */
  border-radius: 50%;
  line-height: 1; /* Standardize line-height */
}

#carousel-container .nav-element {
  background-color: #268bd2; /* Solarized Light blue */
}

#carousel-container .nav-dot {
  font-size: 15px; /* Smaller font size for dots if needed */
  background-color: #93a1a1; /* Solarized Light grey */
}

#carousel-container .nav-dot.active {
  background-color: #2aa198; /* Cyan for active dot */
}

#carousel-container #back.inactive, #carousel-container #forward.inactive {
  color: #93a1a1; /* Solarized Light muted text color */
  cursor: default;
}

/* Additional styling for Rewind and Show Collage buttons */
#carousel-container #rewind, #carousel-container #show-collage {
  /* Optional additional styles */
}

#carousel-container .collage-container {
    display: none;
    /* background-color: #fff; /* Set your desired background color */
    overflow: auto; /* Add scrollbar when content overflows */
    position: relative;
}

#carousel-container .collage-item:nth-child(odd) {
    background-color: #002b36; /* Use your desired base0 color */
}

#carousel-container .collage-item:nth-child(even) {
    background-color: #073642; /* Use your desired base1 color */
}
</style>

<script>
const carouselList = [
  {
    img: "https://dummyimage.com/1920x1080/002b36/eee8d5&text=one",
    text:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.",
    title: "Lorem ipsum"
  },
  {
    img: "https://dummyimage.com/1920x1080/073642/93a1a1&text=two",
    text:
      "Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie.",
    title: "Cras elementum"
  },
  {
    img: "https://dummyimage.com/1920x1080/b58900/002b36&text=three",
    text:
      "Etiam ullamcorper. Suspendisse a pellentesque dui, non felis. Maecenas malesuada elit lectus felis, malesuada ultricies.",
    title: "Etiam ullamcorper"
  },
  {
    img: "https://dummyimage.com/1920x1080/dc322f/eee8d5&text=four",
    text:
      "Curabitur et ligula. Ut molestie a, ultricies porta urna. Vestibulum commodo volutpat a, convallis ac, laoreet enim.",
    title: "Curabitur et"
  },
  {
    img: "https://dummyimage.com/1920x1080/6c71c4/073642&text=five",
    text:
      "Phasellus fermentum in, dolor. Pellentesque facilisis. Nulla imperdiet sit amet magna. Vestibulum dapibus, mauris nec malesuada fames ac.",
    title: "Phasellus fermentum"
  }
];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.querySelector("#carousel-container");
  const carouselItem = container.querySelector(".carousel-item");
  const img = carouselItem.querySelector("img");
  const textOverlay = carouselItem.querySelector(".text-overlay");
  const collageContainer = container.querySelector(".collage-container");
  const carouselNavigation = container.querySelector(".carousel-navigation");
  const forwardButton = container.querySelector("#forward");
  const showCollageButton = document.getElementById("show-collage");
  let currentIndex = 0;
  let isCollageShown = false;

  function createNavDots() {
    carouselList.forEach((_, index) => {
      const dot = document.createElement("div");
      dot.className = "nav-dot";
      dot.addEventListener("click", () => {
        if (isCollageShown) {
          toggleCollageDisplay(false);
        }
        displayItem(index, false);
      });
      dot.addEventListener("dblclick", () => displayItem(index, true));
      carouselNavigation.insertBefore(dot, forwardButton); // Insert before the Forward button
    });
  }

  function displayItem(index, showText) {
    currentIndex = index;
    const item = carouselList[index];
    img.src = item.img;
    img.alt = item.title || "Carousel image";
    textOverlay.textContent = showText ? item.text : "";
    carouselItem.style.display = "block";
    updateNavigationState();
  }

  function updateNavigationState() {
    document.querySelectorAll(".nav-dot").forEach((dot, index) => {
      dot.classList.toggle("active", index === currentIndex);
    });
  }

  function toggleCollageDisplay(show) {
    collageContainer.style.display = show ? "block" : "none";
    carouselItem.style.display = show ? "none" : "block";
    isCollageShown = show;
    updateNavigationState(); // Update navigation dots
  }

function showCollage() {
    collageContainer.innerHTML = '';
    carouselList.forEach((item, index) => {
        const collageItem = document.createElement('div');
        collageItem.className = 'collage-item';
        collageItem.textContent = item.text;
        collageContainer.appendChild(collageItem);

        // Add zebra background color based on index
        if (index % 2 === 0) {
            collageItem.style.backgroundColor = '#base0_color'; // Use your desired base0 color
        } else {
            collageItem.style.backgroundColor = '#base1_color'; // Use your desired base1 color
        }
    });

    toggleCollageDisplay(true);

    // Calculate and set the height based on the width
    const containerWidth = container.offsetWidth;
    const height = (containerWidth * 9 / 16);
    collageContainer.style.height = height + 'px';
}


  // Event Listeners
  document
    .getElementById("rewind")
    .addEventListener("click", () => displayItem(0, false));
  document
    .getElementById("back")
    .addEventListener(
      "click",
      () => currentIndex > 0 && displayItem(currentIndex - 1, false)
    );
  document
    .getElementById("forward")
    .addEventListener(
      "click",
      () =>
        currentIndex < carouselList.length - 1 &&
        displayItem(currentIndex + 1, false)
    );

  showCollageButton.addEventListener("click", () => {
    if (isCollageShown) {
      toggleCollageDisplay(false);
    } else {
      showCollage();
    }
  });

  img.addEventListener("click", () =>
    displayItem(currentIndex, !textOverlay.textContent)
  );

  createNavDots();
  displayItem(0, false); // Initialize with the first item
});

</script>

<section>
<h2>Carousel</h2>
<!-- div class="r-stretch" -->
<div style="width: 1080px !important; margin: 0 auto;">
<div id="carousel-container" >
  <div class="carousel-item">
    <img src="" alt="carousel image">
    <div class="text-overlay"></div>
  </div>
  <div class="collage-container" style="display: none;"></div> <!-- Collage container -->
  <div class="carousel-navigation">
    <div id="rewind" class="nav-element">&#8634;</div> <!-- Rewind button -->
    <div id="back" class="nav-element">&#9664;</div> <!-- Back button -->
    <div id="nav-dots-container"></div> <!-- Navigation dots will be inserted here -->
    <div id="forward" class="nav-element">&#9654;</div> <!-- Forward button -->
    <div id="show-collage" class="nav-element">&#9733;</div> <!-- Show Collage button -->
  </div>
</div>
</div>
</section>

<script>
<!-- prettier-ignore-start -->

var jeopardyInitializations = [];

// CSV Data
const csvData2 = `Culture,question1,answer1,Code,question2,answer2,Build,question3,answer3,Test,question4,answer4,Release,question5,answer5,Deploy,question6,answer6
50,question1-50,answer1-50,50,question2-50,answer2-50,50,question3-50,answer3-50,50,question4-50,answer4-50,50,question5-50,answer5-50,50,question6-50,answer6-50
"",question1-100,answer1-100,100,question2-100,answer2-100,100,question3-100,answer3-100,100,question4-100,answer4-100,"","","-",100,question6-100,answer6-100
250,question1-250,answer1-250,250,question2-250,answer2-250,250,question3-250,answer3-250,250,question4-250,answer4-250,250,question5-250,answer5-250,250,question6-250,answer6-250
500,question1-500,answer1-500,500,question2-500,answer2-500,500,question3-500,answer3-500,500,question4-500,answer4-500,500,question5-500,answer5-500,500,question6-500,answer6-500`;

jeopardyInitializations.push({ containerId: 'jeopardy-grid-container1', csvData: csvData2 });

<!-- prettier-ignore-end -->
</script>

</section><!-- end vertical -->

<!-- appendix ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

<section><!-- begin vertical -->

<section data-markdown># Appendix</section>

<section>
<h2>The LCAP-Definition — step by step</h2>
<figure>
    <blockquote class="lcap" cite="https://www.gartner.com/reviews/market/enterprise-low-code-application-platform<"><strong>An Enterprise Low-Code Application Platform is</strong> <span class="fragment fade-in-then-semi-out">an application platform that is used to</span><span class="fragment fade-in-then-semi-out"> rapidly develop and deploy</span><span class="fragment fade-in-then-semi-out"> custom applications</span><span class="fragment fade-in-then-semi-out"> by abstracting and minimizing or replacing the coding needed in development.</span><span class="fragment fade-in-then-semi-out"> At a minimum, an LCAP must include:</span><span class="fragment fade-in-then-semi-out"> Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span><span class="fragment fade-in-then-semi-out"> Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span><span class="fragment fade-in-then-semi-out"> Simplified application test, deployment and management.</span></blockquote>
    <figcaption>Source: <cite>https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</cite></figcaption>
</figure>
</section>

</section><!-- end vertical -->

<!-- footer id="title-footer" style="bottom: 5px !important;"><p>Copyright © 2024 {% if page.author %}{{ page.author }}{% else %}{{ site.author }}{% endif %}. Except where otherwise noted, this work is licensed under a Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License.</p></footer //-->
