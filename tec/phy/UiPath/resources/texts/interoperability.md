

#{{include.headingmodifier}} From Orechestrator Queues on to emails, databases or spreadsheets

- how to traverse from one item to the next
  - transaction data, transaction item
  - transaction number
  - datatypes
  - one-shot vs loop
  - batch size
- Queue

Default: Orchestrator Queue
Rather: Orhestrator Queue dequeue operation. Dev must "fill"/enqueue the Queue first -- not implemented in REFramework template.
@see IPO input>process>output

TransactionData datatable

if emails then redefine as List of MailMessages
if spreadsheet then read spreadsheet as datatable rows


placeholder dt_TransactionData as variable in Main.xaml


CAVEAT: "transaction item" has NOT "database transaction integrity"
> A database transaction symbolizes a unit of work performed within a database management system (or similar system) against a database, and treated in a coherent and reliable way independent of other transactions. A transaction generally represents any change in a database. Transactions in a database environment have two main purposes:
>
> To provide reliable units of work that allow correct recovery from failures and keep a database consistent even in cases of system failure. For example: when execution prematurely and unexpectedly stops (completely or partially) in which case many operations upon a database remain uncompleted, with unclear status.
> To provide isolation between programs accessing a database concurrently. If this isolation is not provided, the programs' outcomes are possibly erroneous.
> …
> A database transaction, by definition, must be atomic (it must either be complete in its entirety or have no effect whatsoever), consistent (it must conform to existing constraints in the database), isolated (it must not affect other transactions) and durable (it must get written to persistent storage).[1] Database practitioners often refer to these properties of database transactions using the acronym ACID.
> @see: https://en.wikipedia.org/wiki/Database_transaction

