---
---

In the UiPath ReFramework, **Orchestrator Queues** provide a high-level infrastructure for managing and processing items, while **data types and variables within the UiPath workflow** implement lower-level methods and properties to handle these items individually within the automation. Here the differences between the functionality managed by Orchestrator and the data types used within UiPath to interact with Queue items.

### 1. Functionality Implemented in Orchestrator

Orchestrator provides several high-level functionalities for managing queues and transactions, including:

- **Queue Management**:
  - Orchestrator allows users to create and configure queues, where each queue holds a list of items (transactions) to be processed by robots.
  - Within Orchestrator, queues can have retry policies, SLA deadlines, priorities, and can be monitored for completion, errors, and throughput.
- **Transaction Handling**:
  - Orchestrator automatically tracks the status of each transaction item in a queue. Statuses include `New`, `In Progress`, `Successful`, `Failed`, and `Abandoned`.
  - Orchestrator also handles retry logic if configured, so items that encounter `System.Exception` errors can be automatically retried without additional logic in the workflow.
- **Logging and Analytics**:
  - Each transaction's outcome (success or failure) is logged in Orchestrator, allowing users to view detailed reports and analyze process performance.
  - Orchestrator logs each error message and allows filtering and exporting of transaction records for reporting and analysis.
- **Error Handling**:

  - Orchestrator differentiates between `Application/System Exceptions` (e.g., network errors) and `BusinessRuleExceptions` (e.g., data validation issues), allowing developers to configure separate handling and retry strategies for `Application/System Exceptions`.

- **Scalability and Parallel Processing**:
  - Queues in Orchestrator support distributed processing, enabling multiple robots to work on the same queue and process items in parallel. This allows for greater scalability and improved processing efficiency.

In summary, Orchestrator manages the overall lifecycle, logging, and retry policies of queue items at a high level, as well as the status of each transaction item.

### 2. Data Types and Methods/Properties in UiPath

Within UiPath workflows, specific data types and methods are used to interact with Orchestrator queues. Key data types include:

- **QueueItem**:

  - `QueueItem` is the main data type used to represent individual items retrieved from an Orchestrator queue.
  - **Properties**:
    - `SpecificContent`: A `Dictionary(Of String, Object)` that holds the main data payload of the transaction item. This property is used to access custom fields within each transaction (e.g., `"InvoiceNumber"`, `"Amount"`).
    - `Output`: Another dictionary used to store the results or outputs of the transaction that can be pushed back to Orchestrator.
    - `Progress`: A string property that represents the current progress status of the transaction. This can be updated throughout the processing of an item.
    - `Status`: Indicates the current status of the `QueueItem` in Orchestrator (e.g., `New`, `InProgress`, `Successful`), but it is read-only in the UiPath workflow. The status is managed by Orchestrator itself.
  - **Methods**:
    - `SetTransactionStatus`: Allows the robot to set the outcome of the transaction (Success, Fail with Application Exception, or Fail with BusinessRuleException) and mark it appropriately in Orchestrator.

- **Orchestrator API Methods for Queue Items**:

  - `Get Transaction Item`: Retrieves the next available `QueueItem` from the specified queue in Orchestrator. This method is used in the `Get Transaction Data` state in ReFramework.
  - `Add Queue Item`: Adds a new item to an Orchestrator queue. This is used in processes where robots need to create new work items dynamically.
  - `Set Transaction Status`: Updates the status of a `QueueItem` after processing it. This method can set a transaction to `Successful`, `Failed` (with either `System.Exception` or `BusinessRuleException`).

- **DataRow as an Alternative**:
  - In cases where processes use Excel files, databases, or data tables as transaction sources instead of Orchestrator queues, a `DataRow` can represent each transaction item.
  - **Properties**:
    - `Item(columnName)`: Accesses a specific column value within the row, which is similar to accessing `SpecificContent` in a `QueueItem`.
    - `Table`: References the `DataTable` that the `DataRow` belongs to, useful for relational operations within in-memory data.
  - `DataRow` is typically processed similarly to `QueueItem` within the ReFramework, although without Orchestrator’s automatic status handling and retry features.

### Differences between Orchestrator Functionality and UiPath Data Types

| Feature                   | Managed by Orchestrator                                         | Managed by UiPath Data Types                                                    |
| ------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Queue Management**      | Yes, including retries, SLAs, priority, and parallel processing | No                                                                              |
| **Transaction Status**    | Yes, updated based on SetTransactionStatus from UiPath          | Accessed via `QueueItem.Status` but cannot change locally                       |
| **Retry Logic**           | Configurable in Orchestrator                                    | Manual retries would need custom logic if done locally                          |
| **Logging and Analytics** | Managed and stored in Orchestrator logs                         | Only additional log messages for debugging can be added in the workflow         |
| **Transaction Data**      | Stored in the Queue as `SpecificContent` and `Output` fields    | Accessed through `QueueItem.SpecificContent` in UiPath                          |
| **Error Handling**        | Differentiates `System.Exception` and `BusinessRuleException`   | Must specify error types in UiPath, though exceptions bubble up to Orchestrator |

### Error Handling in Orchestrator for Queue Items

In Orchestrator, error handling and retry logic for `QueueItems` works as follows:

1. **System.Exception (Application Exception)**:

   - When a `System.Exception` (or any other exception that’s not a `BusinessRuleException`) occurs during the processing of a `QueueItem`, Orchestrator **can retry the transaction** if retry logic is enabled for the queue.
   - Orchestrator’s Queue settings include an option to configure the number of retries for items that fail due to `System.Exception`.
   - If a `System.Exception` occurs and retries are enabled, Orchestrator will automatically create a new attempt for that transaction item after a specified interval. Each attempt is treated as a new `QueueItem`, but Orchestrator tracks the retry count.
   - The retry limit is configurable in Orchestrator’s Queue settings, allowing you to control how many times a failed transaction should be retried.

2. **BusinessRuleException**:
   - When a `BusinessRuleException` is thrown in the UiPath workflow, Orchestrator **does not retry the item**, regardless of the Queue’s retry settings.
   - A `BusinessRuleException` is treated as a **non-retriable** failure because it typically indicates a logical or data-related issue that cannot be resolved by simply retrying (e.g., missing required information, invalid data formats, or violated business rules).
   - In the ReFramework, `BusinessRuleException` is used to indicate that a transaction failed due to a predictable and irrecoverable condition, and retrying the item would not change the outcome.
   - Instead of retrying, Orchestrator will mark the `QueueItem` as **Failed** and log the `BusinessRuleException` details, allowing the item to be reviewed or handled later as needed.

### Why This Distinction Matters

This distinction is important because it allows developers to classify errors based on their recoverability:

- **System.Exceptions** often represent transient or environmental issues (like network timeouts or file access errors), where a retry might succeed.
- **BusinessRuleExceptions** represent logical conditions or validation errors that are unlikely to change on a retry, making it more efficient to skip retries for these cases.

In summary, **only `System.Exception` errors are eligible for retry in Orchestrator** if configured. `BusinessRuleException` items are logged as failed without retry attempts, in alignment with their nature as non-recoverable errors.

### Summary

- **System.Exception**: Orchestrator can automatically retry these exceptions if retries are enabled in the Queue settings.
- **BusinessRuleException**: Orchestrator does **not** retry items that fail due to `BusinessRuleException`. These are treated as final failures without retry.

- **Orchestrator** provides high-level management for the queue lifecycle, transaction status, error handling, retry logic, and logging.
- **UiPath Data Types (QueueItem)** provide access to the specific transaction data and allow local handling of item-specific operations but rely on Orchestrator for overarching control over the queue and item status.

These aspects work together to allow the ReFramework to handle large, distributed, and potentially error-prone processes in a reliable, manageable, and scalable way.
