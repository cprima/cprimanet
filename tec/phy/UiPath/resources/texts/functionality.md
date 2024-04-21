#{{include.headingmodifier}} Functional correctness under specified conditions -- and beyond


##{{include.headingmodifier}} Objectives

- Functionality of
  - solid handling of business rule violations. To achieve this the handling of Business Rule Expections needs to be _analyzed_.
  - 

##{{include.headingmodifier}} Concept

//Planning requires understanding

- default BRE: none
- when to throw a BRE
- what to align with business stakeholders
- when processing stops

##{{include.headingmodifier}} 

With RPA being best suited for repetitive, rule-based tasks working on structured data the ROI is dependent on clearly defined scenarios with low exceptions. The presence of variations in a business process can be adressed by either more complex code or defined handover to human scenarios.

A particular invocation of a business process with a single set of input data is referred to as transaction.
@see ... for a critical ... vocabulary

The REFramework deals with the need to cancel any further processing of a particular 
...
with the notion of a BusinessRule Exception. If the developer throws such a BRE the current transaction is not processed any further and not retried.

Sample situations where throwing a BRE is applicable:

- if the process expects a 10 digit input data but only 9 digits are supplied
- ...

By default not a single BRE is implemented. It is the responsibility of the developer to implement any such BRE.






