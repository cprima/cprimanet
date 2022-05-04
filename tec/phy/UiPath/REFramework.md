---
layout: post
title: "Yet another perspective on the UiPath REFramework"
component: 
date:   2022-01-01 00:00:00 +0100
abstract: ""
---

## Objectives

As an architect or a developer, how can we design or implement with the REFramework basic software quality characteristics like:

- Portability
  - _implement_ an adaptable config file for dev/(test/)prod environments
- Reliability
  - fault tolerance with retries of "System Exceptions a.k.a. Application Exceptions". This needs to be _planned_ and _contrasted_ against Business Rule Expections. _Diagramming_ the implemented state machine in comparison to textbook examples gives a high-level insight.
- Functionality of
  - solid handling of business rule violations. To achieve this the handling of Business Rule Expections needs to be _analyzed_.
- Interoperability with
  - emails, databases, spreadsheets and UiPath Orchestrator Queues. To achieve this the control flow and logic structure needs to be _investigated_.
- Maintainability
  - prepare insightful analysis of logfiles. Existing logging enhancements need to be _located_.
  - set up test wrapper

Finally to critique omissions in the template gives the confidence to handle the REFramework like a Pro!


## Prerequisites

Understanding of arguments, parameters and variables in UiPath Studio.



## Contents

- TOC
{:toc}

## Preface

Nota bene: There are two official REFramework versions without distinguishable versioning, here referred to as Classic and Modern version.
Henceforth focus on the Modern version.

Nota bene: Although the GitHub repo is prominently referred to from the documentation it is unmaintained since about 4 years.

{% include_relative assets/texts/portability.md headingmodifier="#" %}

{% include_relative assets/texts/reliability.md headingmodifier="#" %}

{% include_relative assets/texts/functionality.md headingmodifier="#" %}

{% include_relative assets/texts/interoperability.md headingmodifier="#" %}

{% include_relative assets/texts/maintainability.md headingmodifier="#" %}


## Tipps & Tricks & Gotchas

Prevent by all means any exception type other than Business Rule Exception if
- you can't rollback the processing of an "transaction item" and/or
- your processing is not idempotent!
Any exception like SelectorNotFound or System.IO.FileNotFoundException will be retried!


//todo
//check
The RetryNumber is "in the current REFramework" only checked in RetryCurrentTransaction.xaml, and Initializing actually checks for maxConsecutiveSystemExceptions

System.Exeception is worded "ApplicationException":
`in_Config("LogMessage_ApplicationException").ToString+" Retry: "+io_RetryNumber.ToString+". "+in_SystemException.Message+" at Source: "+in_SystemException.Source` @see RetryCurrentTransaction.xaml



Export to Excel is your friend, too!

GitHub repo out-of-date and unmaintained, but referenced in the documentation.

retries: not backoff implemented, rather "immediately"

no batchsize

