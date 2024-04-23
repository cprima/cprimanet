---
layout: post
title: "Automating Version Management Using PowerShell in UiPath RPA Projects"
date: 2024-04-23 03:30:00 +0000
categories: RPA CI/CD Automation
tags: [UiPath, RPA, CI/CD, PowerShell, Version Control, Automation, Git, SemVer]
excerpt: "Explore automating version management using PowerShell in UiPath RPA projects. This post delves into a sample implementation based on Git commit messages, sharing insights and code examples to enhance your CI/CD pipeline."
---

⬆️ In this post in my series on CI/CD for UiPath RPA projects, I will share insights into automating version management using PowerShell. Today, we look at a sample implementation based on Git commit messages.

In previous posts, I explored:

- 🎯 The central role of `projectVersion` as stored in the `project.json` file
- 📘 What Semantic Version is and how it is implemented in UiPath Studio

The entire script is available as a gist: [View Gist](https://gist.github.com/cprima/860f63327e05297b510b49acb7cc79ad) It contains 2 PowerShell functions to:

- 🔍 Parse-SemVer
- ⬆️ Increment-SemVer
  which I also publish elsewhere as a PowerShell module. But for the sake of simplicity, the functions are included in the script file.

📜 At the core, the script contains:

```powershell
$projectJson = Get-Content ".\project.json" -Raw | ConvertFrom-Json
$commitMessage = (git log --format=%B -n 1) -join " "
$incrementedVersion = Increment-SemVer -semVerString $projectJson.projectVersion -commitMessage $commitMessage

$projectJson.projectVersion = $incrementedVersion
$projectJson | ConvertTo-Json -Depth 99 | Set-Content ".\project.json"

git add ".\project.json" && git commit -m "Version bump in project.json" && git push
```

Here is what Increment-SemVer does to a projectVersion of 0.2.3:

--commitMessage 'BREAKING CHANGE: Refactoring output arguments for use via Orchestrator API, incompatible with previous versions.'
👉 Major increment to 1.0.0

-commitMessage 'Feature: Add dynamic email templating capability to customer notification process.'
👉 Minor increment to 0.3.0

-commitMessage 'Bug Fix: Resolve memory leak in PDF generation module observed under high load conditions.'
👉 Patch increment to 0.2.4

🔑 Key point is: The words in the commit message determine the version increment.

It might come as a surprise to RPA developers that this approach bypasses the UiPath Studio "publish" function and has requirements on well-crafted commit messages. But as RPA (and UiPath Studio) matures, our skillset also has to converge towards best practices in other coding environments.
