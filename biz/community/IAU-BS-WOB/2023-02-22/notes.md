
Ziel ist, das Stichwort "Low Code Plattformen" mit Leben zu füllen, und von den Technologien im eigenen Beruf abgrenzen zu können.


Enterprise Low-Code Application Platforms (LCAP)


Was ist die Definition von Gartner:

An Enterprise Low-Code Application Platform is an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application; Support for developing applications consisting of user interfaces, business logic, workflow and data services; Simplified application test, deployment and management.

Nehmen wir diese Definition mal auseinander:

- rapid
- custom application
- develop and deploy
- coding
- LowCode capabilities
- LowCode
- model-driven
- graphical programming
- scripting
- user interface, business logic, workflow, data services
- test
- deploy
- management


## Rapid application development

Wohin führt das Wort "rapid" in diesem Kontext? Gemeint ist hier RAD Rapid Application Development und zwei Quellenzitate sollen die Spannbreite der Definitionen abbilden:

> So what is rapid application development?
> Rapid application development (RAD) is an agile project management strategy popular in software development.
> https://www.lucidchart.com/blog/rapid-application-development-methodology

Diese Definition stellt das die Metholdologie in den Vordergrund.

> RAD is especially well suited for (although not limited to) developing software that is driven by user interface requirements. Graphical user interface builders are often called rapid application development tools. Other approaches to rapid development include the adaptive, agile, spiral, and unified models.
> https://en.wikipedia.org/wiki/Rapid_application_development

Hier kommt zusätzlich der Werkzeug-Charakter ins Spiel.

Ich persönlich mag einen Blick auf Werkzeuge und deren Oberflächen, also will ich das Bauen von GUIs weiterverfolgen:

> Graphical user interface builder
> a software development tool that simplifies the creation of GUIs by allowing the designer to arrange graphical control elements (often called widgets) using a drag-and-drop WYSIWYG editor. Without a GUI builder, a GUI must be built by manually specifying each widget's parameters in source-code, with no visual feedback until the program is run
> https://en.wikipedia.org/wiki/Graphical_user_interface_builder

Mit dem acronym WYSIWYG kommen wir einen Schritt weiter: What-you-see-is-what-you-get oder auf deutsch "Was Sie sehen, ist das, was Sie bekommen."
Weil die deutsche Sprache gerne Worte zusammensetzt, auch "Echtbilddarstellung" genannt!

> Anstatt einen bestimmten Code einzugeben, wird mit Bausteinen editiert.
> https://praxistipps.chip.de/was-ist-wysiwyg-einfach-erklaert_41432

Solche Editoren haben eine lange Geschichte in der IT, der Vorläufer von MS Word namens WordStar wird generell als erste WYSIWYG Software angesehen.

> WordStar was the first microcomputer word processor to offer mail merge and textual WYSIWYG. (…) WordStar would display a full line of dash characters onscreen showing where page breaks would occur during hardcopy printout. Many users found this very reassuring during editing, knowing beforehand where pages would end and begin, and where text would thus be interrupted across pages.
> https://en.wikipedia.org/wiki/WordStar

Für den Bau von Webseiten war um das Jahr 2000 herum vom Hersteller Macromedia die Software Dreamweaver marktbestimmend für die Erstellung von HTML-basierendem Output.


//CMS, WordPress, widgets, plugins


### custom applications

Im Gegensatz zu einer Commercial Off-The-Shelf (COTS) Solution, welche in ihren funktionalen Eigenschaften höchstens durch Konfigurierbarkeit oder customizing an die Anforderungen angepasst werden kann, ist eine custom application spezifisch auf Anforderungen zugeschnitten.


> Functional Suitability
> This characteristic represents the degree to which a product or system provides functions that meet stated and implied needs when used under specified conditions.
> https://iso25000.com/index.php/en/iso-25000-standards/iso-25010


Die Definition von LCAP nimmt also explizit Bezug auf die Erstellung von nicht OTS Applikationen.

## develop and deploy

Die Definition von LCAP verwendete das Adjektiv rapid in diesem Zusammenhang: …rapidly develop and deploy…

Für Werkzeuge zum Entwickeln, bauen / packetieren und dabei oft auch debuggen wird typischerweise das Wort IDE verwendet:

> An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.
> (…)
> The boundary between an IDE and other parts of the broader software development environment is not well-defined;
> https://en.wikipedia.org/wiki/Integrated_development_environment

Allerdings wird dieses Wort typischerweise eben NICHT im Zusammenhang mit LCAP (mit L wie LowCode) verwendet, sondern als umfangreicheres Werkzeug zum Editieren von Quellcode / source code, geschrieben/getippt/expanded. 

Der Blick auf die Liste mit dem Vergleich von IDEs zeigt, dass die Vokabel im Zusammenhang von Programmiersprachen verwendet wird, und in IDEs der Code getippt wird:

https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments


Hypothese: LCAP könnten also ein Begriff sein, der komplementär zu IDE zu verstehen ist.


### develop AND deploy

Dieser Teil der Definition ist im Zusammenhang mit dem letzten Satz zu verstehen, denn testing gehört im Ablauf zwischen develop und deploy. Im verwandten Begriff CI/CD zeigt sich jedoch auch, dass "D" mal als delivery, mal als deployment verwendet wird. Wie auch immer man das betrachtet: Das kompilieren, das Erstellen von Paketen oder in anderer geeigneter Art die Installierbarkeit sicherstellen.

Die Definition legt sich dadurch auch in der Wortwahl nicht auf eine Methodologie fest, welche bei der Verwendung von Vokabel einer bestimmten Methologie ansonsten impliziert würde.

Die LCAP Definition nennt also NICHT DevOps-Phasen wie Discover, Plan, Build, Test, Deploy, Operate, Observe, Continous Feedback.

> DevOps is a set of practices, tools, and a cultural philosophy that automate and integrate the processes between software development and IT teams
> https://www.atlassian.com/devops

Macht ja auch eigentlich Sinn, wenn es um tools zu gehen scheint, und nicht um Vorgehensweisen.


## abstracting and minimizing or replacing the coding

Nachdem das Wort rapid ja schon in wenigen Schritten zu WYSIWYG führte, geht die LCAP Definition jetzt einen Schritt weiter.

Gemeint ist außerdem, dass vorrangig visuall progrmmiert wird, wie die Defintionen für das im Buchstaben L enthaltene LowCode zeigen:

> Low-code is a visual approach to software development that enables faster delivery of applications through minimal hand-coding.
> https://www.ibm.com/topics/low-code


> Low-code is an application development method that elevates coding from textual to visual.
> https://www.mendix.com/low-code-guide/


Wegweisend war hier in 1991 Visual Basic von Microsoft

> Visual Basic was derived from BASIC and enables the rapid application development (RAD) of graphical user interface (GUI) applications, access to databases using Data Access Objects, Remote Data Objects, or ActiveX Data Objects, and creation of ActiveX controls and objects.
> https://en.wikipedia.org/wiki/Visual_Basic_(classic)

Mit etwas zeitlichem Abstand wurde auch für den Einsatz in Schulen "replacing the coding" als niedrigschwellige Heranführung an den Computer entwickelt:

https://en.wikipedia.org/wiki/Scratch_(programming_language)

https://scratch.mit.edu/projects/editor/?tutorial=name

Mit Projekten wie der Hardware micro:bit wird unverändert der pädagogische Einsatz an Grundschulen forciert, stets im Sinne auch der LCAP-Definition "abstracting and minimizing or replacing the coding"

https://en.wikipedia.org/wiki/Micro_Bit


https://bubble.io/blog/visual-programming/


Diese Varianten des visuallen Programmierens betonen _Blöcke_ als Basiselemente

https://en.wikipedia.org/wiki/Visual_programming_language


Im Unternehmenseinsatz finden sich typischerweise andere visuelle Darstellungsformen, etwa 

- flow based a.k.a. node based https://en.wikipedia.org/wiki/Flow-based_programming

https://en.wikipedia.org/wiki/Node-RED


In der RPA-Welt bestens bekannt ist Windows Workflow Foundation

> https://en.wikipedia.org/wiki/Windows_Workflow_Foundation




Ziel ist, mit der Abstrahierung eine weniger formelle Vorbildung vorauszusetzen:

> Visual programming is a programming language that lets humans describe processes using illustration.
> Whereas a typical text-based programming language makes the programmer think like a computer, a visual programming language abstracts the development complexity and minimizes the need to write lines of code. This way, it enables programmers to describe the process in terms that make sense to humans.
> https://www.outsystems.com/glossary/what-is-visual-programming/







## model-driven approach

In der IT wird das Wort model nicht auf dem Laufsteg verortet, sondern oft als Teil vom Model–view–controller design pattern.

> Model–view–controller (MVC) is a software architectural pattern[1] commonly used for developing user interfaces that divide the related program logic into three interconnected elements. This is done to separate internal representations of information from the ways information is presented to and accepted from the user.
> Traditionally used for desktop graphical user interfaces (GUIs), this pattern became popular for designing web applications.
https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller


ABER Vorsicht, das ist ein Holzweg!

Model-driven architectures sind etwas anderes:

> The Model-Driven Architecture (MDA) defines an approach to modeling that separates the specification of system functionality from the specification of its implementation on a specific technology platform. In short it defines a guidelines for structuring specifications expressed as models
> http://agilemodeling.com/essays/mda.htm

Diese vorstehende Definition beschreibt eine Art template, und keinesfalls ein Datenbank-Modell!

> MDD is a software development methodology that allows users to build complex applications through simplified abstractions of pre-built components
> https://www.mendix.com/model-driven-development/

Hier wird der template-Charakter nochmal stärker präzisiert zu einer Art "widget toolkit"

> A widget toolkit, widget library, GUI toolkit, or UX library is a library or a collection of libraries containing a set of graphical control elements (called widgets) used to construct the graphical user interface (GUI) of programs.
> https://en.wikipedia.org/wiki/Widget_toolkit


Wenn also tendenziell die graphische Oberfläche gemeint ist, dann bewegt sich die LCAP-Definition also im View- oder auch Controller- Aspekten des falschen Freundes design pattern.








## Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application

Gartner definiert an dieser Stelle also LowCode als "pre-built components" oder "graphical programming"



Der Hersteller Mendix wird nochmal deutlicher:

> Abstraction
> In model-driven, low-code development, the model is a user-friendly veneer that encloses a pre-built application component (pieces of functionality). Each self-contained building block handles all the technical aspects of that component—from logic to user interface to the security and integration concerns—allowing them to operate together seamlessly. The result is a powerful drag-and-drop visual model of abstracted functionality that plays nicely with other components.
> https://www.mendix.com/model-driven-development/

Weil die Vokabel nicht zum üblichen office Wortschatz gehört: "veneer" bedeutet auf Deutsch "Furnier":

> a thin layer of decorative wood or plastic used to cover a cheaper material
> https://dictionary.cambridge.org/dictionary/english/veneer



# No Code

An dieser Stelle fällt auf, dass zur richtigen Einordnung von LowCode noch ein Begriff fehlt:

> No-code development platforms (NCDPs) allow programmers and non-programmers to create application software through graphical user interfaces and configuration instead of traditional computer programming. No-code development platforms are closely related to low-code development platforms as both are designed to expedite the application development process. However, unlike low-code, no-code development platforms require no code writing at all, generally offering prebuilt templates that businesses can build apps with.
> https://en.wikipedia.org/wiki/No-code_development_platform

Im Kern: "no-code development platforms require no code writing at all"

Die LCAP Definition "…with scripting" zielt auf diesen Unterschied ab: Bei LowCode kann auch immer noch traditionell code geschrieben werden.


## develop a complete application; Support for developing applications consisting of user interfaces, business logic, workflow and data services

Zwar steht da ein Semikolon dazwischen, aber "user interface … logic … data" kann als eine Seite der Gleichung "complete application" gesehen werden.

Eine LCAP also soll alle diese Aspekte unterstützen. Schauen wir uns die genauer an:





### interface

> The term "user interface" is often used in the context of (personal) computer systems and electronic devices.
> https://en.wikipedia.org/wiki/User_interface

Gemeint sein kann nur ein Graphical User Interface der Applikation sein.

> A graphics-based operating system interface that uses icons, menus and a mouse (to click on the icon or pull down the menus) to manage interaction with the system. … A comprehensive GUI environment includes four components: a graphics library, a user interface toolkit, a user interface style guide and consistent applications
> https://www.gartner.com/en/information-technology/glossary/gui-graphical-user-interface


Als ein Beispiel für ein interface toolkit hier ein Auszug dessen, was Qt als "types" bereitstellt:

Qt Quick Controls QML Types 
Qt GUI
https://doc.qt.io/qt-6/qtgui-index.html

- Layouts
- Button
- Calendar
- CheckBox
- Container
- ListElement
- Menu
- Popup
- ProgressBar
- TextField
- ToolTip
- and many more

Solche Bestandteile eines user interface toolkits sind dann die building blocks für eine "custom application".
Und sollten im Requirements Management fest im Blick sein, um die richtigen Erwartungen zu dokumentieren.


### business logic and workflows

> In computer software, business logic or domain logic is the part of the program that encodes the real-world business rules that determine how data can be created, stored, and changed.
> It is contrasted with the remainder of the software that might be concerned with lower-level details of managing a database or displaying the user interface, system infrastructure, or generally connecting various parts of the program.
> https://en.wikipedia.org/wiki/Business_logic

In dieser Definition scheint das zuvor genannte, aber beim Begriff 'model' nicht passende MVP design pattern wieder deutlich durch: Die business logic oder domain logic entspricht dem C / Controller.

Oder mit dem IPO-Model (auf deutsch EVA-Prinzip) verglichen:

> The input–process–output (IPO) model, or input-process-output pattern, is a widely used approach in systems analysis and software engineering for describing the structure of an information processing program or other process.
> …
> A computation based on the requirement (process)
> https://en.wikipedia.org/wiki/IPO_model



Der Begriff 'workflow' muss aber erst präzisiert werden, denn zunächst ist damit nicht nur IT oder Software gemeint.

Aber in nur wenigen Schritten wird erstaunlich Bekanntes in Relation gesetzt werden können.

> A workflow consists of an orchestrated and repeatable pattern of activity, enabled by the systematic organization of resources into processes that transform materials, provide services, or process information.
> …may refer to a document, service, or product…
> https://en.wikipedia.org/wiki/Workflow


Schauen wir beim verwandten Begriff Workflow Engine nach, auf das hier Wesentliche gekürzt:

> Workflow engine
> A workflow engine is … key component in workflow technology and typically makes use of a database server.
>
>A workflow engine manages and monitors the state of activities in a workflow, such as the processing and approval of a loan application form, and determines which new activity to transition to according to defined processes (workflows). … A workflow engine facilitates the flow of information, tasks, and events.…
>
> Workflow engines mainly have three functions:
> 1. …
> 2. …
> 3. Executing condition script: After passing the previous two steps, the workflow engine executes the task, and if the execution successfully completes, it returns the success, if not, it reports the error…
> https://en.wikipedia.org/wiki/Workflow_engine

Schauen wir nach konkreten Produkten für diese Funktionalitäten so findet sich neben Bizagi, Camunda oder Salesforce.com auch
> Windows Workflow Foundation
> https://en.wikipedia.org/wiki/Workflow_management_system

Jede Implementation von workflows wird ihre eigenen Stärken und Schwächen haben. Eine BPMN-basierte workflow enginge wird sich mit lang laufenden workflows deutlich leichter tun als flüchtige Implementationen ohne state persistence.


### data services

Ob als Eingabe und Ausgabe nach IPO/EVA oder als Speicherort im MVC: Daten werden logisch oder physisch bei Applikationen mit GUI von der domain logic zugegriffen, oder bei Automatisierungen von workflows verarbeitet.

> Data layer architecture
> The data layer … zero to many data sources.
> https://developer.android.com/topic/architecture/data-layer

Im Kontext von LCAP werden oft data sources mit GUI Elementen verknüpft. So kann bsw ein ListElement des interface toolkits mit einer Tabelle verknüpft werden, um dann ein Dropdown-Element zu befüllen.

Aufgepasst: Gleich zwei Mal hintereinander konnte ein Querverweis gesetzt werden. Anscheinend ist das Bild schon recht "rund".

#### connectors


Es fehlen auch nur noch zwei Aspekte

## Simplified application test

> Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do.
> https://www.ibm.com/topics/software-testing

Die LCAP Definition betont vermutlich deshalb "simplified", weil die QA quality assurance durch testing in ihrer Komplexität der eigentlichen Entwicklung wohl kaum nachsteht.

Schon allein die typischen Arten von Software Testing zeigen die Vielfalt:

> Types of software testing
> There are many different types of software tests, each with specific objectives and strategies:
> 
> Acceptance testing: Verifying whether the whole system works as intended.
> Integration testing: Ensuring that software components or functions operate together.
> Unit testing: Validating that each software unit performs as expected. A unit is the smallest testable component of an application.
> Functional testing: Checking functions by emulating business scenarios, based on functional requirements. Black-box testing is a common way to verify > functions.
> Performance testing: Testing how the software performs under different workloads. Load testing, for example, is used to evaluate performance under > real-life load conditions.
> Regression testing: Checking whether new features break or degrade functionality. Sanity testing can be used to verify menus, functions and commands at > the surface level, when there is no time for a full regression test.
> Stress testing: Testing how much strain the system can take before it fails. Considered to be a type of non-functional testing.
> Usability testing: Validating how well a customer can use a system or web application to complete a task.
> https://www.ibm.com/topics/software-testing



## deployment and management.

> Software deployment is all of the activities that make a software system available for use.
> https://en.wikipedia.org/wiki/Software_deployment

> Software maintenance in software engineering is the modification of a software product after delivery to correct faults, to improve performance or other attributes.[1][2]
> A common perception of maintenance is that it merely involves fixing defects. However, one study indicated that over 80% of maintenance effort is used for non-corrective actions.[3] This perception is perpetuated by users submitting problem reports that in reality are functionality enhancements to the system.[citation needed] More recent studies put the bug-fixing proportion closer to 21%.
> https://en.wikipedia.org/wiki/Software_maintenance


> Mendix applications run on the platform’s cloud-native stateless runtime architecture that conforms to Twelve-Factor App principles with support for modern cloud platforms such as Docker, Kubernetes and Cloud Foundry. As a result, Mendix apps benefit from auto-scaling, auto-provisioning, auto-healing, low infrastructure overhead, CI/CD, and cloud interoperability out of the box.
> https://www.mendix.com/evaluation-guide/app-lifecycle/deployment/

> Comprehensive auditing and monitoring tools built into OutSystems enable a proactive management of application performance and make it easier to detect problems by allowing the identification of performance issues in real-time.
> https://www.outsystems.com/evaluation-guide/what-kind-of-monitoring-and-analytics-does-outsystems-offer/

> OutSystems enables all sorts of runtime configurations, such as scheduling of batch jobs, database connections, web-service endpoints, business properties and versions.
> https://www.outsystems.com/evaluation-guide/configuration-management-for-outsystems-applications/

> Identity and access management
> OutSystems offers full support for identity management, including user management, and groups.
> Governance of applications is achieved by configuring groups and assigning them to end-users.
> https://www.outsystems.com/evaluation-guide/identity-and-access-management/

