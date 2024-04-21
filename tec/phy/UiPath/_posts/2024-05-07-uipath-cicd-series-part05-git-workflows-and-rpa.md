---
layout: post
title: "What Can RPA Learn from Git Workflows in Traditional Software Development?"
date: 2024-05-07 03:30:00 +0000
categories: RPA DevOps SoftwareDevelopment
tags: [RPA, UiPath, Git, GitHub, DevOps, Automation, CI/CD, Workflow]
excerpt: "This mini-series explores the integration of Git workflows into UiPath RPA projects, questioning current practices and proposing new strategies to leverage Git's full potential in RPA development."
---

🔔 What can RPA learn from Git workflows in traditional software development?

This mini-series about CI/CD pipelines in UiPath RPA will not yet proceed to TEST, RELEASE, or DEPLOY stages. There is still much to discuss regarding CODE and BUILD to master RPA software development.

In the comments, please share your thoughts: I believe that in RPA, source code management, such as Git, is often used merely as a file archive, which fails to leverage its full capabilities. This usage should be expanded.

In traditional software development, teams typically define their Git workflows, which may resemble those depicted in the attached image. 🖼️

I am not advocating for a direct copy of these methods, but rather suggesting an exploration of how they could be beneficial in a technical RPA role.

Without diving into the specifics:

- Circles can be understood as events,
- upon which we can react with automated code in a structured, rule-based, and repetitive digital way.

I propose that in UiPath RPA, these automations should be commonly implemented:

- On each push to a central Git repository, the Workflow Analyzer is executed.
- A pull request from a development branch to a defined release branch triggers a package build.
- Publishing from the UiPath Studio should be abandoned.

Implementing these practices would ensure all RPA developers are equipped for future professional challenges with today's source code management tools, providing a foundation to meet security concept requirements and potentially leading to beneficial changes in UiPath's Git implementation.

🪡 The next post will cover a publicly visible GitHub implementation of all concepts discussed in this series so far.

Nota bene: Git is the SCM, and GitHub a collaborative platform built on Git. Pull requests, as commonly understood, are a feature of GitHub, whereas Git itself manages commits and merges.
