



#{{include.headingmodifier}} Reliability: Fault tolerance despite presence of faults and Recoverability in the event of an interruption or failure

##{{include.headingmodifier}} Walkthrough Statemachine and retries


##{{include.headingmodifier}} Objectives

- Reliability
  - fault tolerance with retries of "System Exceptions a.k.a. Application Exceptions". This needs to be _planned_ and _contrasted_ against Business Rule Expections. _Diagramming_ the implemented state machine in comparison to textbook examples gives a high-level insight.

##{{include.headingmodifier}} Concept

//Planning requires understanding

- System Exceptions vs. Business Rule Exceptions
- state machine in theory and REFramework
- retry strategies outside of REFramework
- high-level understanding of the retry behaviour in the REFramework
- deepdive into the control flow


The REFramework aims to improve the fault tolerance of automated processes, adressing the needs of both business and IT people. The two disinctive "System Exceptions" and "Business Rule Exceptions" mechanisms need to be planned and their respective focus contrasted against each other. Business Rules Exceptions need to be aligned with the business process owner.

##{{include.headingmodifier}} Misc

###{{include.headingmodifier}} Exemplary usecases

SE: retry-mechanism, monitoring, system administration, 3rd party application support

BRE: rejection of faulty input data, handover to human, "as-designed" partial implementation of business logic

###{{include.headingmodifier}} Synonyms

Business Rule Exception, Business Exception

System Exception, Application Exception

###{{include.headingmodifier}} Name clashes

variables

language constructs

###{{include.headingmodifier}} Definitions

The official documentation defines the two Exceptions as following:

> Exceptions that happen during the framework’s execution are divided into two categories:
> - Business Exceptions: This kind of exception is implemented by the class BusinessRuleException and it should be thrown when there are problems related to the rules of the business process being automated. For example, if a process expects to receive an email with an attachment, but the attachment does not exist, the process would not be able to continue. In this case, a developer can use the Throw activity to throw a BusinessRuleException, which indicates that there was a problem that prevented the rules of the process from being followed. Note that BusinessRuleExceptions must be explicitly thrown by the developer of the workflow, and they are not automatically thrown by the framework or by the activities.
> - System Exceptions: If anexception is not related to the rules of the process itself, it is considered a system exception. Examples of system exceptions include an activity that timed-out due to slow network connection or a selector not found because of a browser crash.
>
> @see: REFramework Documentation-EN.pdf


##{{include.headingmodifier}} State machine in theory and REFramework

###{{include.headingmodifier}} Generic Statemachine diagram

todo: generic
![ISO 25001:2007 Software Product Quality Model](/biz/IT/Software-Engineering/resources/FSM-generic-example.svg){:class="resize"}

todo: onEntry onExit
![ISO 25001:2007 Software Product Quality Model](/biz/IT/Software-Engineering/resources/FSM-generic-example.svg){:class="resize"}


###{{include.headingmodifier}}  Observations of the Statemachine in the UiPath REFramework template:


![ISO 25001:2007 Software Product Quality Model](/tec/phy/UiPath/assets/FSM-UiPath-REFramework.svg){:class="resize"}

In this specific implementation of a State Machine* there are
- 2 types of actions that are associated with a state:
  - an Entry action that is executed when entering a state
  - an Exit action that is executed when exiting a state
  - the execution order is Entry -> Exit -> Transition
- Guard clauses implement conditional transitions and determine which state is transitioned to next

In the REFramework template we do not find the following other State Machine features (although they are possible if a usecase might require):
- a trigger (e.g. a hotkey listener in an attended process)
- Exit actions
- code that evaluates the current state
Not that these are needed -- I rather list them for the sake of completeness.

The REFramework notably DOES HAVE
- empty trigger in every state. This makes the State Machine executing Entry, Exit and Transition right after each other
- and as the Exit actions are also empty the transitions are executed right after the Entry action
- Guard Clauses in form of conditions control the flow of the "auto transitioning"

The auto-transitioning feature of the REFramework is based on variables within the scope of the Main workflow: The variables (sic!) SystemException, BusinessRuleException or TransactionItem are evaluated in a transition condition.


*) In software engineering, a State Machine is also called Finite State Machine, because it can only be in one state of a finite number of states.

```
08:15:42.7289 Info {"message":"statemachine execution started",…
08:15:43.6470 Info {"message":"executing Entry",…
08:15:43.6614 Info {"message":"executing Exit",…
08:15:43.6704 Info {"message":"performing transition",…
08:15:43.6952 Info {"message":"statemachine execution ended",…

```

End Process is of Final State




### retry strategies outside of and within the REFramework

Retry patterns commonly implemented in various types of software. An excursion into web development serves as an illustrative introduction and reference to RPA processes.

In its most simple form a client requests from a server and a response is returned.

Similarly, a RPA Robot may perform a task in a system and if all goes optimal the system will react as expected. The task could be a single transaction item from a queue, or a single email that is processed, or a single row from a table.

The repetivite nature of a typical RPA processes though requires a loop.

Now in REFramework the reliability of the process is greatly improved by reacting to the response and alternatively:

- in case of a thrown Business Rule Exception to cancel the execution of the currently looped item
- or when a System Exception was thrown to retry immediately for a configurable amount of times

REFramework implements this behaviour slightly different depending on the current state the state machine is in.
Different from what the standard UML diagram might visually suggest the retry is actually implemented by executing the task again, with an incremented retry count as the only difference.

The REFramework template does not implement any so-called backoff strategy, where a request is sent in an increasing amount of time. In web development this gives an overloaded server the chance to response to a backlog of requests, and a client implementing such a backoff strategy does not contribute to the already overloaded server.

Another common pattern is that of a circuit breaker, when the retries are limited to such an extend that a system deemed unavailable is triggering a software fuse that stops the process as a whole.
In the Classic REFramework template this was implemented as the retry number.
In the Modern REFramework templates the configurability is more granular with

- retry number
- max
- max




![Retry Behaviour in REFramework](/biz/IT/Software-Engineering/resources/retry-patterns.png){:class="resize"}

### high-level understanding of the control flow


![Retry Behaviour in REFramework](/tec/phy/UiPath/assets/pictures/REFramework_RetryBehaviour_highlevel.png){:class="resize"}

