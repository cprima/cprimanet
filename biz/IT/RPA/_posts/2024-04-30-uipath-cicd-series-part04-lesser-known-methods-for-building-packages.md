---
layout: post
title: "Exploring Lesser-Known Methods for Building Packages in UiPath RPA Projects"
date: 2024-04-30 03:30:00 +0000
categories: RPA Automation DevOps
tags:
  [
    UiPath,
    RPA,
    CI/CD,
    Automation,
    Jenkins,
    PowerShell,
    DevOps,
    Package Building,
  ]
excerpt: "This post delves into lesser-known methods for building packages in UiPath RPA projects, including insights from the UiPath Jenkins plugin and using uipcli.exe for deployment and testing. Learn how these tools can streamline your CI/CD pipeline."
---

🛠️ Today: Exploring lesser-known methods for building packages.

I cannot stress enough how insightful it was for me when I discovered the UiPath Jenkins plugin sourcode, specifically the UiPathPack.java and Utility.java files. And also https://docs.uipath.com/test-suite/automation-suite/2023.4/user-guide/jobs
🔴 THE major takeaway: Using uipcli.exe it is possible to build and even deploy to Orchestrator!

The uipcli.exe

- does not require a UiPath licence
- can be downloaded ad hoc from a nupkg packages (see attached document for sample code)

It is best documented in the Test Suite docs: https://docs.uipath.com/test-suite/automation-suite/2023.4/user-guide/uipath-command-line-interface

To ease into CI/CD pipelines I recommend to place uipcli.exe locally where a PowerShell script can call it, and write a few lines into a ps1 file to execute it. It capabilities are

- running workflow analyzer
- build a nupkg
- deploy to Orchestrator
- run tests
- and more

Such a minimal implementation will also tell if it works in your environment (building packages needs network access to nuget feeds, for example.)

I was able to successfully use uipcli.exe on a personal, public repo on github.com, on an ""ephemeral"" runner. (An ""ephemeral runner"" is a temporary virtual environment that is provisioned for running specific tasks or jobs and is disposed of after use, ensuring a clean, isolated setup for each execution.)

👉 This is how to run Workflow Analyzer with uipcli.exe
& 'C:\Program Files\uipcli\tools\uipcli.exe' package analyze .\project.json --resultPath path\to\uipath-workflow-analyzer_results.json

👉 And this is how to build a process package with a supplied version string:
& 'C:\Program Files\uipcli\tools\uipcli.exe' package pack .\project.json --output "".\path\to\output"" --traceLevel Verbose --disableTelemetry --outputType Process

Reading the project.json it is trivial to build dynamically a Process or Library, the key designOptions.outputType contains

- Process
- Library
- or others

And because the projectVersion was already incremented as per Semantic Versioning rules with code published earlier in this series, uipcli.exe brings us one step further in the CI/CD pipeline for UiPath RPA.

Remember the DevOps infinity symbol? Leveraging ""CODE"" version control and a few lines of PowerShell code the ""BUILD"" phase is also covered.

Next step will one step back: Git is much more than file snapshots, and with the additional capabilities of GitHub on top the structured, rule-based and repetitive digital task of building UiPath RPA packages can be automated. Sounds familiar? That's why I consider this series as advocating to ""eat our own dogfood"".

https://github.com/jenkinsci/uipath-automation-package-plugin/blob/develop/src/main/java/com/uipath/uipathpackage/util/Utility.java
https://github.com/jenkinsci/uipath-automation-package-plugin/blob/develop/src/main/java/com/uipath/uipathpackage/UiPathPack.java

#RPA #UiPath #Automation #DevOps #build
