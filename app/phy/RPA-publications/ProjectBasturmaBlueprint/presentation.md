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

### pro CI/CD for RPA

- automate the RPA delivery pipeline: eat your own dog food
- raise the bar, raise the value, raise the price?
- governance, compliance
- security
- …

Note:
This will only display in the notes window.

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

<section data-markdown># About</section>

<section data-markdown>

## About Me

- bar
- baz

Note:
This will only display in the notes window.

</section>

<!-- section data-markdown>

## In Scope, Out of Scope

### In Scope:

- Code, Build, Test, Release, Deploy
- (Culture), Automation

### Out of Scope:

- Plan, Operate, Monitor
- Lean, Measurement, Sharing

Note:
This will only display in the notes window.

</section> //-->

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

        .roof-container {
            width: 100%;
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
          margin-bottom: 20px;
        }

        .roof {
            width: calc(100% - 10px); /* Adjust as needed */
            height: 30px; /* Height of the triangle */
            background-color: #b58900; /* Roof color */
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%); /* Triangle shape */
            display: flex;
            justify-content: center;
        }

        .roof-text {
            width: 100%; /* Full width */
            background-color: #b58900; /* Same color as the roof */
            text-align: center;
            padding: 10px 0;
          margin-top: -1px;
            border-radius: 5px; /* Rounded bottom right corner */
        }

        .pillars {
            display: flex;
            justify-content: space-around;
            width: 100%;
            height: 300px;
        }

        .pillar {
            width: 15%; /* Adjusted width for each pillar */
            height: 100%;
            border-radius: 5px;
            background-color: #93a1a1; /* Default pillar color */
            margin: 0 1%; /* Space between pillars */
            color: #002636;
        }

        .pillar .label, .pillar .sub-label {
            background-color: #657b83; /* Label background */
            width: 100%;
            padding: 5px 0; /* Padding for the label */
            text-align: center;
            color: #fdf6e3;
        }

        .pillar .label {
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }

        .pillar .sub-label {
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

    <h2>In Scope</h2>

<div width="90%">
    <div class="pillars-container">
        <div class="roof-container fragment fade-up">
            <div class="roof"></div>
            <div class="roof-text">Culture</div>
        </div>
        <div class="pillars">
            <div class="pillar fragment fade-up">
                <div class="label">Code</div>
                <div class="sub-label">Sub-Label 1</div>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Build</div>
                <div class="sub-label">Sub-Label 2</div>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Test</div>
                <div class="sub-label">Sub-Label 3</div>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Release</div>
                <div class="sub-label">Sub-Label 4</div>
            </div>
            <div class="pillar fragment fade-up">
                <div class="label">Deploy</div>
                <div class="sub-label">Sub-Label 5</div>
            </div>
        </div>
        <div class="foundation fragment fade-up">Automation, Lean IT, Measure, Share</div>
    </div>
</div>
<aside class="notes">
This will only display in the notes window.
</aside>
</section>

<section data-markdown>

## About Slides Structure

- building blocks, …, vision
- domains: off-the-shelf technology, biz processes, custom apps / scripts

Note:
This will only display in the notes window.

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

<section data-markdown>

## DevOps Framework(s)

- CALMS

Note:
This will only display in the notes window.

</section>

<section data-markdown>

## Devops inifinity loop

- …

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

## foo

- bar
- baz

Note:
This will only display in the notes window.

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

### Beyond the UiPath Studio

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

### Code Review

- It's a culture thing
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### Modern

1. Process
2. Library (Object Repository!)
3. …

Note:
Since Object Repository availability: towards more library projects

</section>

<section data-markdown>

### Git & Compagnie

- automated Workflow Analyzer: "Static Code Analysis"
- defined branching strategy
- defined commit message conventions
- Git vs. GitHub/GitLab/…
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### deepdive: Static Code Analysis

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

### projct.json projectVersion

- SemVer? Really?
- increment: human or automation?
- automated commit?
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### build runners

- Windows
- uipcli.exe vs. UiPath Studio
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### build script(s)

- custom
- skills needed to develop and maintain
- continous integration (triggered by commit)
- test and production builds
- …

Note:
This will only display in the notes window.

</section>

<section data-markdown>

### dependencies and libraries

- libraries are built differently
- library naming conventions and dependency management
- …

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

<section data-markdown>## Deepdive Test</section>

<section data-markdown>

### foo

- bar
- baz

Note:
This will only display in the notes window.

</section>

</section><!-- end vertical -->

<section><!-- begin vertical -->

<!--
//
// [code] [build] [test] [**RELEASE**] [deploy]
//
//-->

<section data-markdown>## Deepdive Release</section>

<section data-markdown>

### foo

- bar
- baz

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

<section data-markdown>## Deepdive Deploy</section>

<section data-markdown>

### foo

- bar
- baz

Note:
This will only display in the notes window.

</section>

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

<section data-markdown># Appendix</section>

<section>
<h2>The LCAP-Definition — step by step</h2>
<figure>
    <blockquote class="lcap" cite="https://www.gartner.com/reviews/market/enterprise-low-code-application-platform<"><strong>An Enterprise Low-Code Application Platform is</strong> <span class="fragment fade-in-then-semi-out">an application platform that is used to</span><span class="fragment fade-in-then-semi-out"> rapidly develop and deploy</span><span class="fragment fade-in-then-semi-out"> custom applications</span><span class="fragment fade-in-then-semi-out"> by abstracting and minimizing or replacing the coding needed in development.</span><span class="fragment fade-in-then-semi-out"> At a minimum, an LCAP must include:</span><span class="fragment fade-in-then-semi-out"> Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span><span class="fragment fade-in-then-semi-out"> Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span><span class="fragment fade-in-then-semi-out"> Simplified application test, deployment and management.</span></blockquote>
    <figcaption>Source: <cite>https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</cite></figcaption>
</figure>
</section>

</section><!-- end vertical -->
