Testing

1. Unit Testing
   Objective: Test individual actions or components of the RPA script in isolation.

1. Functional Testing
   Objective: Validate that the RPA script performs the intended task correctly from start to finish.

1. Integration Testing
   Objective: Ensure that the RPA script interacts correctly with external systems and applications.

1. User Acceptance Testing
   Objective: Confirm that the RPA script meets the requirements and expectations of the end users.

1. Regression Testing
   Objective: Verify that the RPA script continues to function correctly after changes have been made.

1. Performance Testing
   Objective: Evaluate the speed and efficiency of the RPA script under various conditions.

1. Security Testing
   Objective: Identify and address potential security vulnerabilities in the RPA script.

1. Compatibility Testing
   Objective: Ensure that the RPA script works correctly on different operating systems, browsers, and devices.

1. Usability Testing
   Objective: Assess the user-friendliness and ease of use of the RPA script.

1. Accessibility Testing
   Objective: Confirm that the RPA script is accessible to users with disabilities.

1. Compliance Testing
   Objective: Ensure that the RPA script complies with relevant laws, regulations, and industry standards.

1. Localization Testing
   Objective: Verify that the RPA script works correctly in different languages and regions.

1. Recovery Testing
   Objective: Test the ability of the RPA script to recover from failures and errors.

1. Scalability Testing
   Objective: Evaluate the ability of the RPA script to handle increasing workloads and data volumes.

1. Robustness Testing
   Objective: Assess the RPA script's ability to handle unexpected inputs and conditions.

Implement testing

- ensure availability of test systems
  - access management
  - freshness of test data
  - test environment setup (test orchestrator/tenant/folder, test robots, test assets)
  - test data management
- ensure testability of the RPA script
  - configurability
  - argument handling
  - workflow structure
    - modularity
    - window / application / browser handling
  - Dispatcher / Performer: queue input or not
- test data
  - test data preparation
    - happy path
    - non-happy path
  - test data management
    - test data storage
    - .variations
      - .gitignore
- test execution
  - UiPath Studio
  - Orchestrator trigger / jobs
    - challenges of arguments
  - Postman
  - Test Manager

Configurability

- variants of Config.xlsx
- assets, credentials
- assets as feature flags
  - "feature \*"
- converting config file entries to assets
- config file as argument
- config file sheets
- Framework/InitAllSettings.xaml
