



> our main business is RPA. But with UiPath Test Suite, we add a universal software testing solution, in which even manual testing has its place.


What is software testing

meets certain requitements

- functional requirement
  expected behaviour
- non-functional behaviour
  evaluates the operation of a system

-> collect quality-related information
-> reduces risk

"Software failure becomes Business failure."

No universal process for siftware testing

Type
- mission critical
- consumer app

Stages:

- plan
  - SME / product owners
  - derived from function or non
  - testing approach
  - schedule
  - criteria
  - test objectives
- design
  - list of prioritized test cases / high-level test cases
  - prepare test data
  - identify test environemtn
- implement
   - assets
   - creating detailled manual or automated test sets
   - test sets
   - building the test environment
- execute
  - run test sets according to test plan
  - continously or schedule
  - triogger manuall yorautoaticlly
  - take continous regression testing, execeute prevous test case to make sure the cahnges made don't cause errors
  - automated test cases are the way to avoid aottlenecks by testing itself
- analyse
  - gathering data from all other test stages
  - analyze the data to make informed decisions about next steps
  - close the loop: offer means to stakeholders for the decision go live or postpone
  - a failed doesn't mean a bug
  - consider the role or persona of the recipients


Categorizing testing

Test levels /granualiry or scope

- unit / component by developers
  -- mock 
- functionality
- integration
- system / end-to-end
  - behaviour
- acceptance testing

Test types

look at the test approach

not exclusive but equally relevant

- functional
  - validate a certain functionalty
- non-functional
  - validate performance
  - scaling


visibilit and access of the tester

- black box
- white box
  - cetain amount of testing to the code by the tester

- manual
  - by a person
- automated testing
  - by unattended robot


manual
- scripted
  - requires processing
  - repetitive actions
    - should become automated
- exploratory
  - requires thinking / creativity

automated
- API
  - testing the business logic
- UI Testing

Start testing early! Shift left testing!



recap the main ideas

Software testing is the process of verifying that a software meets certain requirements and behaves as expected;
Every industry nowadays is in the software business. Thus, software failure becomes business failure;
Testing reduces the risk of failure by helping detect defects before the product reaches the customer;
The main stages of a typical test process are the following



Glossary

Unit testing
Testing individual ‘code’ units, down to the level of methods and functions. It is also called component testing and is usually performed by the developer, in isolation with regards to other components.

Integration testing
–
Verifying if the interfaces between different components work as designed

System testing
–
Testing the behavior of the entire system or product. This is typically done by specialized testers or testing robots in a dedicated pre-production environment, with as few variations from the production environment

Acceptance testing
–
Assessing the overall interaction of the end users with the entire system or product

Functional testing
–
Testing a specific functionality of the product

Non-functional testing
–
Checking the non-functional aspects of a software application - e.g. performance, usability, security, scalability

Scripted manual testing
–
Testing in which the input data, the operation steps and the verification steps are predefined and need to be executed the same way every time

Exploratory testing
–
Testing in which the tester receives only a high-level charter and then it is up to her to explore the software application in detail

UI testing
–
Testing the user interface layer of the application to make sure that it behaves as expected for end users

API testing
–
Testing the business logic of an application through different interfaces and protocols

CI/CD
–
These acronyms stand for Continuous Integration and Continuous Delivery. In software development and testing, these cover the practice of integrating new code into the main branch as often as possible. In CI/CD, testing is extremely important.

ALM
–
Stands for Application Lifecycle Management. It covers all the stages in software development, starting with requirements management and software architecture and going through software testing and project management.






What is Test Manager?

…Test Manager is the component used for managing the test process and the different types of objects and their hierarchy, as well as for integrating with third-party ALM tools.



The Test Manager Hub

The main purpose of this component is to integrate the UiPath Test Suite with third-party ALM tools. 


