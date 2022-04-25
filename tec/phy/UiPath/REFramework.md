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




## Adaptable config file

{% include_relative assets/texts/AdaptableConfigFile.md headingmodifier="#" %}




## Walkthrough Statemachine and retries

{% include_relative assets/texts/walkthrough-statemachine.md headingmodifier="#" %}

Error Handling: To retry or not to retry


|         | Initialization | GetTransactionData |   |   |
|---------|----------------|--------------------|---|---|
| Retries |                |        TRUE        |   |   |
|         |                |                    |   |   |
|         |                |                    |   |   |



## Processing of a single transaction item and handling of business rule violations

TransactionItem

may be part of TransactionData (datatable) but unused if Orechstrator Queue

TransactionData datatable

if emails then redefine as List of MailMessages
if spreadsheet then read spreadsheet as datatable rows

By default not a single BRE is implemented. It is the responsibility of the developer to implement any such BRE.


CAVEAT: "transaction item" has NOT "database transaction integrity"
> A database transaction symbolizes a unit of work performed within a database management system (or similar system) against a database, and treated in a coherent and reliable way independent of other transactions. A transaction generally represents any change in a database. Transactions in a database environment have two main purposes:
>
> To provide reliable units of work that allow correct recovery from failures and keep a database consistent even in cases of system failure. For example: when execution prematurely and unexpectedly stops (completely or partially) in which case many operations upon a database remain uncompleted, with unclear status.
> To provide isolation between programs accessing a database concurrently. If this isolation is not provided, the programs' outcomes are possibly erroneous.
> …
> A database transaction, by definition, must be atomic (it must either be complete in its entirety or have no effect whatsoever), consistent (it must conform to existing constraints in the database), isolated (it must not affect other transactions) and durable (it must get written to persistent storage).[1] Database practitioners often refer to these properties of database transactions using the acronym ACID.
> @see: https://en.wikipedia.org/wiki/Database_transaction



## From Orechestrator Queues on to emails, databases or spreadsheets

queue vs dictionary

single-shot vs. loop

(OnEntry vs. OnExit)



- Maintainability
  - prepare insightful analysis of logfiles. Existing logging enhancements need to be _located_.
  - set up test wrapper



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

