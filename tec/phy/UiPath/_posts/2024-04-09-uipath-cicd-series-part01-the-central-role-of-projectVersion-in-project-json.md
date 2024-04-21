---
layout: post
title: "Enhancing CI/CD Pipelines for UiPath RPA Projects"
date: 2024-04-09 03:30:00 +0000
categories: RPA UiPath CI/CD Automation
tags: [UiPath, CI/CD, automation, PowerShell, projectVersion]
excerpt: "This winter, I enhanced my skills in CI/CD pipelines for UiPath RPA projects, challenging norms and exploring the impacts of GUI automation on testing. Dive into a series of lessons learned and debunked misconceptions about the role of projectVersion in automation."
---

🎯 This winter, I have enhanced my skills in CI/CD pipelines for UiPath RPA projects, expanded my use of Git and GitHub, implemented static code analysis, and created several automated build scripts. My focus has been on exploring the impact of "GUI automation" on "testing."

Welcome to the first post in a series where I'll share key lessons learned and some common misconceptions debunked. 📚

The official stance is clear: ‘Manually editing the project.json file should be attempted for troubleshooting scenarios only, as it may lead to severe consequences and loss of support.’ However, my experience tells a different story. Here's a safe, scripted approach that challenges the norm. 🔍

🎯 THE centerpiece of any automated process towards UiPath RPA projects releases is:
👉 The value of projectVersion in the project.json file in the root folder of each project.

Contrary to the vendor's documented advice, I recommend updating this version number, either manually or via script. Personally, I prefer using PowerShell, which I accomplish with just three lines of code. ⚙️

```
$json = Get-Content "$env:WORKSPACE\project.json" -Raw | ConvertFrom-Json
$json.projectVersion = $env:PROJECT_VERSION
$json | ConvertTo-Json | Set-Content "$env:WORKSPACE\project.json"
```

For various reasons a clearly defined approach of incrementing this version string is core to any CI/CD pipelinefor RPA projects, and is where the interest of both management and technichians overlap: There is no governance without understanding deployment and release of versioned packages, and any automation-assisted development must increment the version based on clear rules.

Do watch out for `projectVersion` from project.json in the next parts of this series as it will resurface repeatedly in this series of posts.
