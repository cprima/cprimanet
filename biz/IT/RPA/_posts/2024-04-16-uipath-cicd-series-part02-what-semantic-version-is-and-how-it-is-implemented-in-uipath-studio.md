---
layout: post
title: "Understanding Semantic Versioning (SemVer) in UiPath RPA Projects"
date: 2024-04-16 03:30:00 +0000
categories: RPA SoftwareDevelopment VersionControl
tags: [UiPath, SemVer, Versioning, NuGet, Software Development]
excerpt: "Explore how Semantic Versioning (SemVer) is integrated into UiPath RPA projects and why it's crucial for managing versions accurately. This post delves into SemVer's basic usage, its components, and how it shapes the deployment of project versions within UiPath Studio."
---

📘 Understanding Semantic Versioning (SemVer) in UiPath RPA Projects

With the tight integration of UiPath RPA projects into NuGet package feeds, the Semantic Versioning, or SemVer, system is ubiquitous. In its basic use, this methodology employs a three-part format: major, minor, and patch (MAJOR.MINOR.PATCH). Each component signals the scope of changes included: a MAJOR version for incompatible API changes, a MINOR version for adding functionality in a backwards-compatible manner, and a PATCH version for backwards-compatible bug fixes. Additionally, SemVer allows for pre-release and build metadata to provide further detail and structure to version management.

In the realm of UiPath Studio, the implementation of project versions adheres to a simplified form of SemVer, described in Backus-Naur Form as:

```
projectVersion ::= <version core>
 | <version core> "-" <pre-release>
```

This notation allows for a core version and an optional pre-release designation, providing flexibility in how versions are staged and deployed.

🛑 A common pitfall in RPA is starting projects with a "finished" version number, like 1.0.0, which may not accurately reflect the developmental stage of most projects. This practice can lead to misconceptions about the project's stability and readiness.

It’s good practice to reflect version changes in your commit messages or pull request titles. This approach not only ensures that each increment is documented and traceable, aligning development work with versioning strategy, but it also lays the groundwork for version increments in automated build scripts.

### Example Git log

```
cpm@host:/mnt/t/example$  git log --all --decorate --oneline --graph
* 36c3d50 (HEAD -> master) Merging development changes
* 23c2383 (tag: v2.0.0) Breaking: new input argument for config file
* 536ff71 (tag: v1.1.0) Feature: Added reporting
* 409121f (tag: v1.0.1) Fix: bug
* 0996c07 (tag: v1.0.0) Major: Release to Production
* d09d6db (tag: v0.2.1) Fix: bug detected during UAT
* 6969130 (tag: v0.2.0) Feature: Implemented requirement foo
* 83a5dac (tag: v0.1.1) Minor: Refactored code
* 3ceda6a (tag: v0.1.0) Initial version
```
