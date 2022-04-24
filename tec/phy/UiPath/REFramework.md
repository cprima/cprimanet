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


## Prerequisites

arguments, parameters and variables


## Perspective

As an architect or a developer, how can we design or implement with the REFramework characteristics:

- Portability
  - adaptable config file
- Functionality of
  - correct handling of business rule violations
- Reliability
  - fault tolerance with retries of "System Exceptions"
- Interoperability with
  - emails, databases, spreadsheets and UiPath Orchestrator Queues
- Maintainability
  - analysis of logfiles
  - test wrapper



## Overview

…
GitHub repo out-of-date and unmaintained, but referenced in the documentation.

## Features

Error Handling: To retry or not to retry


|         | Initialization | GetTransactionData |   |   |
|---------|----------------|--------------------|---|---|
| Retries |                |        TRUE        |   |   |
|         |                |                    |   |   |
|         |                |                    |   |   |

## Walkthrough Statemachine

{% include_relative assets/texts/walkthrough-statemachine.md headingmodifier="#" %}


## Processing of a transaction item

TransactionItem

may be part of TransactionData (datatable) but unused if Orechstrator Queue

TransactionData datatable

if emails then redefine as List of MailMessages
if spreadsheet then read spreadsheet as datatable rows



## (Adaptable) config file

From the documentation:

> One important variable that is passed to almost all the workflows invoked in Main.xaml is the Config dictionary. This variable is initialized by the InitAllSettings.xaml workflow in the Initialization state, and it contains all the configuration declared in the Config.xlsx file. Since it is a dictionary, the values in Config can be accessed by its keys, like Config(“Department”) or Config(“System1_URL”)
>
> For easier manipulation, this configuration file is an Excel workbook with three sheets:
> - Settings: Configuration values to be used throughout the project and that usually depend on the environment being used. For example, names of queues, folder paths or URLs for web systems.
> - Constants: Values that are supposed to be the same across all deployments of the workflow. For example, the department name or the bank name to be used as input in a certain screen.
> - Assets: Values defined as assets in Orchest
>
> @see: Documentation\REFramework Documentation-EN.pdf

### Standard:

1. Main.xaml > Initialization (State)
1. If first run, read local configuration file (If)
1. Invoke InitAllSettings workflow (InvokeWorkflowFile)
  - { in_ConfigFile; value = Data\Config.xlsx, Type = String, Direction = In }

The standard REFramework reads in Main.xaml during the first run of the Initialization state by invoking the InitAllSettings workflow the Excel file as located by the input argument in_ConfigFile, defaulting to Data\Config.xlsx. The location of this config file cannot be declared otherwise.

### Customization:

1. In Main.xaml, create an input string argument `in_ConfigFile` defaulting to  Data\Config_dev.xlsx
1. In the InitAllSettings.xaml workflow file, remove the default value for in_ConfigFile
1. In Main.xaml > Initialization (State) when invoking `Framework\InitAllSettings.xaml` change in the collection of the invoked workflow's argument the value for `in_ConfigFile` to `in_ConfigFile`.

That way you can supply in UiPath Orchestrator a parameter for either Process or Job with a different location. This customization even allows for multiple Processes of the same Package with differing default config files. 













## Conclusions

Prevent by all means any exception type other than Business Rule Exception if
- you can't rollback the processing of an "transaction item" and/or
- your processing is not idempotent!
Any exception like SelectorNotFound or System.IO.FileNotFoundException will be retried!


//todo
//check
The RetryNumber is "in the current REFramework" only checked in RetryCurrentTransaction.xaml, and Initializing actually checks for maxConsecutiveSystemExceptions

System.Exeception is worded "ApplicationException":
`in_Config("LogMessage_ApplicationException").ToString+" Retry: "+io_RetryNumber.ToString+". "+in_SystemException.Message+" at Source: "+in_SystemException.Source` @see RetryCurrentTransaction.xaml


## Tipps & Tricks

Export to Excel is your friend, too!
