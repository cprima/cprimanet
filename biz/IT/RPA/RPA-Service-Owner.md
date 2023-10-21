# Introduction

## Content

- Introduction
- Challenge Legacy Code
- Infrastructure and Tools
- RPA metrics before and after
- Challenge: Deployment Gates
- Suggestions

## Background

- RPA Application Service Owner role (amongst others)
- Decentralized CoEs
- Former backlevel supporter for ATM solutions
- 5+ years UiPath RPA
- MVP in my spare time :(

## Objective

As a RPA Service Owner, how can I achieve Continuous (Code) Improvement in "run"-phase?

- How to achieve
- what to do as a Service Owner (read: securing a budget))
- opportunities and limitations

## Scenario

- Decentralized RPA CoE with Process Owner, Service Owner, Developer
- 5-20 Processes, Prod- & Test-Tenant
- LowCode becoming embraced by "IT red tape"
- Ticket system in place ;)
- annual review of support contract & budget, monthly/quarterly service meetings

> Red tape in IT often slows down innovation and implementation, but despite this, LowCode platforms still retain some flexibility and leeway in terms of customization and integration capabilities.

# Challenge Legacy Code: Embrace it!

- assess the code
- communicate shortcomings
- use for budget

## Code assessment / inventory

### Basics:

- UiPath version?
- configurable? prod- and test-switch?
- version control?
- documented? (biz & dev)
- testable?
- …

> The existence of end-to-end testcases (or a process of obtaining fresh testcases) is key for Change Management and deployment gates.

### Advanced

On a Service Owner level, abstract to actionable recommendations:

- fit with current development best practices
  - (insert long list here)
- Workflow Analyzer result for actionable metrics

> Samples from my long list: allEntrypointsAreReframework, hasCanary, isRepoCICDenabled, hasQueue(s), hasObjectRepository, hasPDD, hasSDD, hasOperationalHandboook, createsTempFoldersIfNotExist, doesWorkOnAnyRobot, hasSupportedDependencies

# Infrastructure and Tools

- Supported UiPath product versions
- Git
- Log Analyzer (e.g. Elastic or Splunk)
- CI/CD (e.g. Jenkins)
- Code Analyzer (e.g. SonarQube)

> Ticket system must be a) in place and b) not being bypassed

## Benefits of Infra Components

- Elastic CE: Centralized logging, Advanced Analytics & Visualization, Search
- Splunk: As Elastic, typically Alerting
- Git: Integration with CI/CD, Upskilling developers
- SonarQube: OTS xml-Analysis only. Main benefit is to establish a pipeline at all

> To effectively manage and collaborate on version-controlled RPA projects outside the confines of UiPath Studio, it's essential to have a dedicated Git client.

## Challenge: Stay Updated with Updates

- not just automated systems
- also UiPath Platform components

> In IT, a vendor's product roadmap often dictates necessary infrastructure changes, especially as older product versions become unsupported, requiring adaptations to accommodate new features, compatibility requirements, or evolving technology standards.

## Challenge: Workflow Analyzer results into SonarQube

Solution Draft (UiPath v2022.x)

- get Workflow Analyzer results from a PowerShell script call
- parse results
- prepare in SonarQube "Generic Issue Import Format"
- ingest into SonarQube
- handle as Code Smells, Bugs, and Vulnerabilities

> Making the technical debt of RPA processes transparent to the solution owner fosters better collaboration and opens active mitigation.

# RPA metrics before and after

Typical RPA metrics

- Process Execution Time: The average time it takes for a bot to complete a specific process
- ROI of Automation
- Automation Rate
- …

## RPA metrics v2.0

- Vendor Support Coverage
- Workflow Analyzer Code Quality
- combined score of previously mentioned long list of "current development best practices"

# Challenge: Deployment Gates

Predefined checkpoints or criteria that a software release or update must meet before moving to the next stage of its deployment lifecycle. These gates are established to ensure to meet

- quality
- security
- performance and
- compliance standards

> As an RPA Service Owner with targets to improve code quality, an agreement on deployment gates is mandatory.

## LowCode Deployments

Meeting the criteria set by structured deployment gates in RPA presents its own set of challenges:

- Rapid Development vs. Thorough Testing
- Dependency on External Systems
- Skill Disparity
- Documentation
- …

> One possible distinction could be between code changes that do or do not change the implemented business logic.

## Tickets and Deployments

When an incident ticket is raised that most likely necessitates a deployment, there are several opportunities and risks associated with it:

Opportunities:

- Improvement in Service Quality ("fix")
- Enhanced Monitoring (e.g. adding log messages)
- Learning Opportunity
- …

Risks:

- Unintended Consequences
- Stakeholder Concerns
- Change Overload
- …

> While some tickets might be perfectly solved by fault clearance, others will require a code change. At minimum each incident should address the analysability (adding log messages if the ticket was hard to analyze).

# Suggestions

- create inventory
- ensure annual rythm
- strategically put as target(s)
