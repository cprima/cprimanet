---
checklists: []
---


primarily meant for RPA Developers looking to improve the interaction between human users and automations by creating rich user interfaces

https://academy.uipath.com/learningpath-viewer/4749/15/700/3
UiPath Apps is the low-code application platform for delivering engaging experiences powered by automation.


Let's talk about low-code development

Simply put, low-code development means building software applications in a visual way. Instead of writing lines of code, the development is based on drag-and-drop actions, pre-built components and connectors.

This can have a huge impact on the speed of building and deploying applications. Low-code development is expected to heavily influence digital transformation programs through the democratization of business application development.

…build a presentation layer allowing you to trigger autoamted processes…

Let's recap: How does UiPath Apps bring together automation and low-code development?

Just like any type of process, automated processes have input and output parameters. For example, a process that files a support ticket needs some client data and the reported issue as input. And the ticket number would be one of the output parameters.

There are different ways of facilitating the exchange of data between human users and automated processes or between different automated processes, such as UiPath Assistant, UiPath Action Center or web forms.

The unique value brought by UiPath Apps comes from the ease of building user interfaces that are accessible from multiple platforms, including Windows, Mac, Linux and mobile devices. Moreover, the apps can be embedded into existing desktop of cloud software.

Even if we discussed only about UiPath Apps in this lesson, you must know that it consist of two components.

They match the two big software stages: building the application or "design time", and running the application or "runtime".

There are two components of UiPath Apps: the first is Apps and is the service used to execute apps. The second one is App Studio and is the tool used to design the apps.

Apps
This is accessible from the left sidebar of UiPath Automation Cloud or UiPath Automation Suite (if UiPath Apps is enabled on the tenant). When accessing Apps, you will see the list of all the available applications. Depending on your permissions defined at app level, you can only run an app or run, edit, export and delete it.

UiPath Apps are Progressive Web Apps 10 (PWAs)

App Studio

App Studio opens automatically when you create a new app or when you edit an existing app. App Studio is a cloud-based web interface that requires no installation, being available from your local browser. This enables anyone to build a functional presentation layer through drag-and-drop actions and by linking the application components with automated processes published to Orchestrator and with their parameters.


Get Started With App Studio

Duration: 25 min
At the end of this lesson you should be able to:

Explain the concept of control in Apps Studio and differentiate between the types of controls.
Describe the basic customizations that can be performed for controls in Apps Studio through properties.
Explain how data flows between apps and automated processes.
Design a basic application using controls and data binding.

All the development capabilities in App Studio are built around controls. These are the building blocks of apps: you add them to the canvas, resize and customize them, then connect them to the automations.

There are three types of controls:

Input controls
Allow human users to provide an input to the application. This can be a button to start a process or a text field to enter the email address of a customer as an input parameter for the process.

Display controls 
Display the outputs of an event run (the ticket number) or provide context for a human user to be able to interact correctly with the app (for example, a label).

Container controls 
Used to group several controls and/or to separate different parts of an user interface, for example 4 text fields displaying customer data.


Setting control properties

Each control has three property tabs:


General
This property category configures how the control is displayed, its function, the parameter with which it is bound, and its state. Each control has its own particular properties.

Events
This category allows the configuration of events and rules involving the control, such as triggering a process, showing a message, opening an URL, and so on. 

Style
This property configures the look and feel of the controls such as border, font, margin and size.


Customizing any control is done by selecting it and accessing the tabs on the right.



Using automated processes from Orchestrator

One of the key features of UiPath Apps is the ability to easily connect an app to one or multiple automated processes. The app can be used as a graphical layer in which users can provide inputs to the process or display the process outputs.

Once a process has been published to Orchestrator, you can reference it from an app.


Data binding

Once the presentation layer of the application is done by adding and configuring controls, you can connect the controls to input and output parameters of the automated processes imported from Orchestrator. This is called data binding.



Controls, properties and data binding - this is all you need to know to start building a simple application.


Let's recap


Types of controls
–
Input controls are interactive. The data can be added manually by us or taken out from other systems or applications.

A few examples of Input controls are: Text Boxes, Buttons, Checkboxes and Date Pickers.



Display or output controls can only display data extracted from other sources such as other applications.

A few examples of Output controls are: Lists, Headers, Labels and Images.

Positioning controls
–
Customized page layout can be easily created using Container Layout control.
The positioning of our controls within a page or container can be accomplished using the Alignment & Layout options.


Page and Container controls can dictate the position of controls within them by using the direction (Vertical/Horizontal) and Alignment attributes in the Layout section. By default, controls fit themselves in one line. If the "Allow wrapping" property is set, the controls wrap themselves to multiple lines if needed.


Resizing controls
–
The size of controls is set by default. Auto allows the control to take the size of the content within it. For example, if a button control's width and height are set to 'Auto', the size of the button grows/shrinks based on the text in the button.



Specific height and width can also be set. Min Width/Height and Max Width/Height are available under more (...) in the size section.



The units of measurement are %, px (pixels), and em (relative to the font-size of the element). For example, 3em means 3 times the size of the current font).


Customizing controls
–
Customizing the font: you can change the way text appears in your app by adjusting the Font Family, Font Size, Font Color, and Font Style (Bold, Italic, Underline) attributes.



Customizing the borders: the border section has three properties: Border Thickness, Border Color and Corner Radius. Pixels are the unit of measurement for these attributes.



Spacing out controls: controls and containers can be spaced out using Margins and Paddings. Margins provide spacing around the controls. Paddings provide spacing between the control and the content within it.


Using automated processes in an app and data binding
–
Automated processes can be imported from Orchestrator and easily connected to apps. Once a process is imported it can be triggered from the application, used as a front end to provide inputs to the process or as a visual canvas to display outputs to your users. This is known as data binding.


Events and Rules

At the end of this lesson you should be able to:

Explain how Events and Rules can be used to add a logical layer in an application.
Design an intermediate app that uses simple Events, Rules, and multiple processes. 
What are Events and Rules in Apps Studio?

Events and Rules enable you to create increasingly complex apps. Events are recorded when a user interacts with an app or control. Rules allow your app to take a predefined action when a certain event occurs. This provides an efficient way to configure the behavior of your application on user interactions, such as clicking on a button.


When designing apps, you often want to provide instructions in the following logic:

If "X" happens then perform "Y"...

...where X is an "event" and Y is a "rule".

Here are a few examples:

- When the "Submit deposit" button is clicked, start this process.
- When the value of the "Cash In" textbox changes to a value below 0, change the label color to red.
- When the help icon is clicked, open the browser to show a documentation page.
- When a tab button is clicked, change the page container to show a different page


By specifying what rules to execute when an event occurs, your app transforms from being a simple display of information to an interactive console.



Important: In order to make all elements available for data binding, make sure to run any newly added processes to your app at least once from your UiPath Assistant or by starting an attended job from Orchestrator.

Let's recap


Main takeaways
–
Events are triggers that get activated when a user interacts with an app or control.
Rules allow your app to take an action when a certain event occurs.
The Bank Teller App we built was connected to 3 different automated processes which can be triggered one by one by a human user. The processes used were "Get Customer Details", "Get Risk" and the loan "Defer" process.
The input for the "Get Customer Details" and "Get Risk" processes is the customer ID added by the human user. The processes start once the search button is pressed. These two processes run one after another and then display their results in the app.
The input for the "Defer" process consists of the contract number and number of months for which the deferral process should be done for. Once the data is added in the fields and the "Defer" button is pressed, the process starts.
It is good design practice to separate containers within the app by using dividers so that data can be easily read. In addition to this, pages can be created within the same app by using the Page Host feature of apps. This can accommodate multiple functionalities each with its own page and sets of fields.
New processes can be added to your app from the Resources section of Apps Studio.
When a process is highlighted, all its input and output arguments can be viewed in the properties panel.
The parameters for each process regarding how the processes should run can be set up from the "Events" tab. Here, you can also chain multiple processes so that when a process is completed, a second one gets trigger by using the “Start process” event.

Events

As we have seen in the video demos, events are triggers that get activated when a user interacts with an app or a control. Each control supports a single event, for example:

Event
Controls
Clicked On
Button, Header, Label, Icon, Image
Value Changed
Checkbox, Date picker, Dropdown, Slider, Switch, Text Area, Textbox, List
Loaded
Page, Table


Rules

Rules allow apps to take an action when a certain event occurs.
Let's recall a few rule examples that we have seen in the video demos:

Rule
Description
Open a Page 	Opens a page of the app as a pop-over or as the contents of a page container. 
Close Pop-Over/Bottom Sheet
Closes the current Pop-Over.
Show Message
Show a message as a toast notification.
Show/Hide Spinner
Show or hide a spinner overlay to show the app as busy.
Start Process
Starts an Automation Process.




Expressions


At the end of this lesson you should be able to:

Explain what expressions are and how they work.
List the functions and the named operators available in Apps Studio.
Expressions are made up of logical operations allowing you to transform, modify, and compute the data within an app, returning a result used in the same app. 

Let's look at several scenarios where they can be used:


bullet
Process data stored in variables, outputs, and other control values from the Resources panel.


bullet
Concatenate pieces of text (strings).


bullet
Perform comparative operations.


bullet
Accommodate simple scenarios using the If function.


bullet
Perform arithmetic operations.


bullet
Control hidden, disabled, font/background color properties.


bullet
Reference a selected record or field from another control.

How do expressions work?

Expressions rely on functions and named operators to perform operations. Expressions can be used both in controls and rules in UiPath Apps.

Below you can find the out-of-the-box set of functions in the App Studio designer:

Functions

How do expressions work?

Expressions rely on functions and named operators to perform operations. Expressions can be used both in controls and rules in UiPath Apps.

Below you can find the out-of-the-box set of functions in the App Studio designer:

Functions

Concat
–
Combines multiple strings into a single string.

Contains
–
Returns 'True' if a string contains a text fragment. 

EndsWith
–
Returns 'True' if a string ends with a text fragment.

If
–
Returns one value if a condition is met and another value if the condition isn't met

IsBlank
–
Returns 'True' if the value of a control (for example, a string) is empty.

Length
–
Returns the length of a text string.

StartsWith
–
Returns 'True' if a string starts with a text fragment.



Named operators

Category	Operator
Addition and subtraction	+, -
Comparison
<, <=, >, >=
Concatenation	&
Equality	==, !=
Exponentiation	^
Logical	&&, and, AND, | |, or, OR, !, not, NOT
Multiplication and division	*, /, %





Working with Files and Persistent Data


At the end of this lesson you should be able to:

Explain how you can upload, download and edit files in apps using Orchestrator storage buckets.
Describe the ways in which you can create apps which retrieve and process values stored in UiPath Data Service.
Working with files stored in Orchestrator

Orchestrator storage buckets provide a per-folder storage solution for automation projects and apps, thus removing the need for external storage.

By designing apps using this feature, you can upload new files at runtime or download files from storage buckets.

How is this done in UiPath Apps?

The connection with the storage bucket is done through a specific type of control: the File Picker. If the file referenced is an image, it will be shown as such inside the app.


Working with UiPath Data Service entities

UiPath Data Service is the component of the UiPath Platform used for persistent data storage. The integration between UiPath Apps and UiPath Data Service enables the development of apps which use data stored as entities in UiPath Data Service.

There are different UiPath Apps functions and rules to interact with Data Service entities:


Functions


Filter
–
The function returns all records that result in true. These expressions can reference fields/columns by name.


Sort
–
Sorts the rows of a given array or range by the values in one or more columns.


Lookup
–
Returns the first entity record that matches the condition.


New
–
Creates a new in-memory entity. 


Rules

The Create/Update Entity Record can be configured when using any control within Apps. To configure this rule, expressions need to be used.

This rule can accept the following inputs:  


bullet
A reference to the entity itself 


bullet
A specific entity to update 

The Delete Entity Record can be configured in the case of any control.
To configure this rule you must use the Lookup function.



Let's recap

Testing the app
–
Testing your app before deployment is best practice, ensuring complete app functionality. This can be done by clicking the "Preview" button from App Studio.


Publishing the app
–
Once testing the app testing has concluded and everything works as expected the app can be deployed by clicking the "Publish" button. The app access link will update and an entry will be added to the publishing History.

Permission management
–
For each app, permissions can be granted at the application level. The entire organization or only specific users can set to have use only permission. Additionally, users can be added to be co-authors and help in developing the application.

Running the app as a desktop application
–
UiPath Apps are designed to be run in the browser but you can create a Windows executable to run them as well. To run a UiPath App as a Windows application, select "Install this site as an app" from your browser.

