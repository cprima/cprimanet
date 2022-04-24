---
layout: post
title: "Yet another perspective on the UiPath REFramework"
component: 
date:   2022-01-01 00:00:00 +0100
abstract: ""
---

* TOC
{:toc}

## Objectives

- (recall how to) implement configuration for dev ( / test ) / prod environments

- investigate the control flow and logic structure

- analyze the handling of Business Rule Expections

- plan for fault tolerance

- locate the enhanced logging

- set up test wrapper

- diagram the implemented state machine in comaprison to textbook examples

- critique omissions in the template


## Perspective

As an architect or a developer, how can we design or implement with the REFramework characteristics:

- Portability
  - adaptable config files
- Functionality of
  - correct handling of business rule violations
- Interoperability with
  - emails, databases, spreadsheets and UiPath Orchestrator Queues
- Maintainability
  - analysis of logfiles
  - test wrapper
- Reliability
  - fault tolerance with retries of "System Exceptions"



## 


## Walkthrough Statemachine

{% include_relative assets/texts/walkthrough-statemachine.md headingmodifier="#" %}


## Processing of a transaction item


