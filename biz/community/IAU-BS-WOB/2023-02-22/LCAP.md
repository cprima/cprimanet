---
layout: presentation_v1.1.0
title: "LCAP: Enterprise Low-Code Application Platform"
date:   2023-03-25 00:00:00 +0100
abstract: Starting with a definition, digging into individual aspects
excerpt: Starting with a definition, digging into individual aspects
published: true
_titleimagefull: /biz/community/thisyearinrpa/resources/images/trends-from-tags-2022-Q4.png
---


<style>
    blockquote.lcap { background-color: #eee8d5; font-size: 1.3em; text-align: left; font-family: 'LinLibertineRegular'; font-style: normal; line-height: 110%; }
    blockquote.lcap .current-fragment { background-color: #b58900; color: #002b36; }
    blockquote.lcap .highlight { background-color: #b58900; color: #002b36; }
    h2.wikipediabg { margin-top: 24px; font-size: 1em; }
</style>


<!-- #Intelligent Automation and Low-Code################################################################################ //-->
<section>


<!-- <section>
<h2>foo bar</h2>
<div class="container">
  <div class="col">1</div>
  <div class="col">2</div>
</div>
</section>//-->

<section>
<h2>Intelligent Automation and Low-Code</h2>
<img src="{{ "/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png" | prepend: site.baseurl }}" alt="" class="resize">
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png">
<h2>Low-Code and Intelligent Automation</h2>
<p>RPA and Low-Code: Sister technologies in the Intelligent Automation space</p>
<blockquote class="lcap">The <strong>Execution</strong> capability … include smart workflow and low-code platforms, and robotic process automation (RPA). This capability is a foundation for end-to-end automated process delivery. It acts as a glue, connecting the technologies across the capabilities.</blockquote>
<p>Source: Pascal Bornet et al. (2020) Intelligent Automation,WSPC.</p>
</section>

</section>


<!-- #LCAP as per Gartner################################################################################ 
biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_What-is-an-Enterprise-Low-Code-Application-Platforms_cropped.png
//-->
<section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_What-is-an-Enterprise-Low-Code-Application-Platforms.png">
<h2>LCAP as per Gartner</h2>
</section>

<section data-background-opacity="0.3" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_What-is-an-Enterprise-Low-Code-Application-Platforms.png">
<h2>What is LCAP?</h2>
<img src="{{ "/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_What-is-an-Enterprise-Low-Code-Application-Platforms_cropped.png" | prepend: site.baseurl }}" alt="" class="resize">
</section>

<!--<section>
<h2>LCAP as per Gartner</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform</strong> is an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. <strong>At a minimum,</strong> an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application; <strong>Support for</strong> developing applications consisting of user interfaces, business logic, workflow and data services; <strong>Simplified</strong> application test, deployment and management.</blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>

</section>//-->

<section>
<h2>The LCAP-Definition — step by step</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform is</strong> <span class="fragment fade-in-then-semi-out">an application platform that is used to</span><span class="fragment fade-in-then-semi-out"> rapidly develop and deploy</span><span class="fragment fade-in-then-semi-out"> custom applications</span><span class="fragment fade-in-then-semi-out"> by abstracting and minimizing or replacing the coding needed in development.</span><span class="fragment fade-in-then-semi-out"> At a minimum, an LCAP must include:</span><span class="fragment fade-in-then-semi-out"> Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span><span class="fragment fade-in-then-semi-out"> Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span><span class="fragment fade-in-then-semi-out"> Simplified application test, deployment and management.</span></blockquote>
<p><span class="fragment fade-in-then-semi-out">Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</span></p>
</section>


<section>
<h2>LCAP definition as a tree</h2>
<img src="{{ "/biz/community/IAU-BS-WOB/2023-02-22/resources/diagrams/LCAPDefinitionAsTreeDiagram.png" | prepend: site.baseurl }}" alt="" style="">
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c1r1  #circle_c1r1 { fill: #859900 !important}
</style>
<div id="c1r1">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
</section>


</section>


<!-- ################################################################################# //-->
<section>

<section>
<h1>Rapid application development</h1>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/lucidchart.com_grapid-application-development-methodology.png">
<h2>What is Rapid Application Development?</h2>
<aside class="notes">
Wohin führt das Wort "rapid" in diesem Kontext? Gemeint ist hier RAD Rapid Application Development und zwei Quellenzitate sollen die Spannbreite der Definitionen abbilden:
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/lucidchart.com_grapid-application-development-methodology.png">
<h2>What is Rapid Application Development?</h2>
<p>Here: Focus on methodology</p>
<blockquote class="lcap">So what is rapid application development?<br />
Rapid application development (RAD) is an agile project management strategy popular in software development</blockquote>
<p>Source: https://www.lucidchart.com/blog/rapid-application-development-methodology</p>
<aside class="notes">
Variante a): Focus on Methodology
Scrum, Kanban, Extreme Programming (XP)
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Rapid_application_development.png">
<h2 class="wikipediabg">What is Rapid Application Development?</h2>
<aside class="notes">
Variante b): Focus on Tools
Hier kommt zusätzlich der Werkzeug-Charakter ins Spiel.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Rapid_application_development.png">
<h2>What is Rapid Application Development?</h2>
<p>Here: Focus on tools</p>
<blockquote class="lcap">RAD is especially well suited for (although not limited to) developing software that is driven by user interface requirements. <span class="highlight">Graphical user interface builders</span> are often called rapid application development <strong>tools</strong>. Other approaches to rapid development include the adaptive, agile, spiral, and unified models.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Rapid_application_development</p>
<aside class="notes">
Variante b): Focus on Tools
Hier kommt zusätzlich der Werkzeug-Charakter ins Spiel.
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c5r1  #circle_c5r1 { fill: #859900 !important}
</style>
<div id="c5r1">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
RAD done, jetzt Graphical user interface builder
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Graphical_user_interface_builder.png">
<h2 class="wikipediabg">Graphical user interface builder</h2>
<aside class="notes">
Ich persönlich mag einen Blick auf Werkzeuge und deren Oberflächen, also will ich das Bauen von GUIs weiterverfolgen:
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Graphical_user_interface_builder.png">
<h2>Graphical user interface builder</h2>
<blockquote class="lcap">a software development tool that simplifies the creation of GUIs by allowing the designer to arrange graphical control elements (often called widgets) using a drag-and-drop <span class="highlight">WYSIWYG</span> editor. Without a GUI builder, a GUI must be built by manually specifying each widget's parameters in source-code, with no visual feedback until the program is run</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Graphical_user_interface_builder</p>
<aside class="notes">
Mit dem acronym WYSIWYG kommen wir einen Schritt weiter:
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/praxistipps.chip.de_was-ist-wysiwyg-einfach-erklaert.png">
<h2>WYSIWYG</h2>
<aside class="notes">
What-you-see-is-what-you-get oder auf deutsch "Was Sie sehen, ist das, was Sie bekommen."
Weil die deutsche Sprache gerne Worte zusammensetzt, auch "Echtbilddarstellung" genannt!
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/praxistipps.chip.de_was-ist-wysiwyg-einfach-erklaert.png">
<h2>WYSIWYG</h2>
<blockquote class="lcap">Anstatt einen bestimmten Code einzugeben, wird mit Bausteinen editiert.</blockquote>
<p>Source: https://praxistipps.chip.de/was-ist-wysiwyg-einfach-erklaert_41432</p>
<aside class="notes">
What-you-see-is-what-you-get oder auf deutsch "Was Sie sehen, ist das, was Sie bekommen."
Weil die deutsche Sprache gerne Worte zusammensetzt, auch "Echtbilddarstellung" genannt!
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_wikiWordStar.png">
<h2 class="wikipediabg">WYSIWYG mit WordStar, circa 1980</h2>
<aside class="notes">
Solche Editoren haben eine lange Geschichte in der IT, der Vorläufer von MS Word namens WordStar wird generell als erste WYSIWYG Software angesehen.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_wikiWordStar.png">
<h2>WYSIWYG mit WordStar, circa 1980</h2>
<blockquote class="lcap">WordStar was the first microcomputer word processor to offer mail merge and textual WYSIWYG. (…)<br />
WordStar would display a full line of dash characters onscreen showing where page breaks would occur during hardcopy printout. Many users found this very reassuring during editing, knowing beforehand where pages would end and begin, and where text would thus be interrupted across pages.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/WordStar</p>
<aside class="notes">
Solche Editoren haben eine lange Geschichte in der IT, der Vorläufer von MS Word namens WordStar wird generell als erste WYSIWYG Software angesehen.
</aside>
</section>

<section>
<h2>WYSIWYG mit DreamWeaver, circa 2000</h2>
<img src="{{ "/biz/community/IAU-BS-WOB/2023-02-22/resources/images/3306449347_739bdcec71_b.jpg" | prepend: site.baseurl }}" alt="" style="">
<p>Source: https://www.flickr.com/photos/lauradahl/3306449347, Copyright Laura Dahl</p>
<aside class="notes">
Für den Bau von Webseiten war um das Jahr 2000 herum vom Hersteller Macromedia die Software Dreamweaver marktbestimmend für die Erstellung von HTML-basierendem Output.
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c6r1  #circle_c6r1 { fill: #859900 !important}
</style>
<div id="c6r1">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
Graphical user interface builder done
</aside>
</section>


<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Integrated_development_environment.png">
<h2 class="wikipediabg">Von Α bis Ω: …Develop and Deploy…</h2>
<aside class="notes">
Die Definition von LCAP verwendete das Adjektiv rapid in diesem Zusammenhang: …rapidly develop and deploy…
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Integrated_development_environment.png">
<h2>Von Α bis Ω: …Develop and Deploy…</h2>
<blockquote class="lcap">An integrated development environment (IDE) is a software application that <strong>provides comprehensive facilities</strong> to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. (…)<br />
The boundary between an IDE and other parts of the broader software development environment is not well-defined;</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Integrated_development_environment</p>
<aside class="notes">
Für Werkzeuge zum Entwickeln, bauen / packetieren und dabei oft auch debuggen wird typischerweise das Wort IDE verwendet: 
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Comparison_of_integrated_development_environments.png">
<h2 class="wikipediabg">IDE: ≠ Low-Code</h2>
<aside class="notes">
Allerdings wird dieses Wort typischerweise eben NICHT im Zusammenhang mit LCAP (mit L wie LowCode) verwendet, sondern als umfangreicheres Werkzeug zum Editieren von Quellcode / source code, geschrieben/getippt/expanded. 
Der Blick auf die Liste mit dem Vergleich von IDEs zeigt, dass die Vokabel im Zusammenhang von Programmiersprachen verwendet wird, und in IDEs der Code getippt wird:
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/atlassian.com_devops.png">
<h2>LCAP avoids a methodology</h2>
<aside class="notes">
Die Gartner Definition vermeidet die Festlegung auf eine Projekt Methode

Die Definition legt sich dadurch auch in der Wortwahl nicht auf eine Methodologie fest, welche bei der Verwendung von Vokabel einer bestimmten Methologie ansonsten impliziert würde.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/atlassian.com_devops.png">
<h2>LCAP avoids a methodology</h2>
<blockquote class="lcap">DevOps is a set of practices, tools, and a cultural philosophy that automate and integrate the processes between software development and IT teams</blockquote>
<p>Source: https://www.atlassian.com/devops</p>
<aside class="notes">
Dieser Teil der Definition ist im Zusammenhang mit dem letzten Satz zu verstehen, denn testing gehört im Ablauf zwischen develop und deploy. Im verwandten Begriff CI/CD zeigt sich jedoch auch, dass "D" mal als delivery, mal als deployment verwendet wird. Wie auch immer man das betrachtet: Das kompilieren, das Erstellen von Paketen oder in anderer geeigneter Art die Installierbarkeit sicherstellen.
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c4r1  #circle_c4r1 { fill: #859900 !important}
</style>
<div id="c4r1">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
rapidly develop and deploy: done
</aside>
</section>





<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/ibm.com_low-code.png">
<h2>Abstracting and Minimizing or Replacing the Coding</h2>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/ibm.com_low-code.png">
<h2>Abstracting and Minimizing or Replacing the Coding</h2>
<blockquote class="lcap">Low-code is a visual approach to software development that enables faster delivery of applications through minimal hand-coding.</blockquote>
<p>Source: https://www.ibm.com/topics/low-code</p>
<aside class="notes">
Nachdem das Wort rapid ja schon in wenigen Schritten zu WYSIWYG führte, geht die LCAP Definition jetzt einen Schritt weiter.

Gemeint ist außerdem, dass vorrangig visuall progrmmiert wird
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_low-code-guide.png">
<h2>Abstracting and Minimizing or Replacing the Coding</h2>
<aside class="notes">
Auch der Hersteller Mendix betont diesen Aspekt
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_low-code-guide.png">
<h2>Abstracting and Minimizing or Replacing the Coding</h2>
<blockquote class="lcap">Low-code is an application development method that elevates coding from textual to visual.</blockquote>
<p>Source: https://www.mendix.com/low-code-guide</p>
<aside class="notes">
Auch der Hersteller Mendix betont diesen Aspekt
</aside>
</section>


<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Visual-Basic-classic.png">
<h2 class="wikipediabg">Visual Coding, ~1990</h2>
<aside class="notes">
visuell zu programmieren hat eine lange Vorgeschichte
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Visual-Basic-classic.png">
<h2>Visual Coding, ~1990</h2>
<blockquote class="lcap">Visual Basic was derived from BASIC and enables the rapid application development (RAD) of graphical user interface (GUI) applications, access to databases using Data Access Objects, Remote Data Objects, or ActiveX Data Objects, and creation of ActiveX controls and objects.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Visual_Basic_(classic)</p>
<aside class="notes">
Wegweisend war hier in 1991 Visual Basic von Microsoft
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/scratch.mit.edu_LowCodeClickable.png">
<h2>Visual Coding, in Primary Schools, part 1</h2>
<aside class="notes">
Mit etwas zeitlichem Abstand wurde auch für den Einsatz in Schulen "replacing the coding" als niedrigschwellige Heranführung an den Computer entwickelt:
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_iMicro-Bit.png">
<h2 class="wikipediabg">Visual Coding, in Primary Schools, part 2</h2>
<aside class="notes">
Mit Projekten wie der Hardware micro:bit wird unverändert der pädagogische Einsatz an Grundschulen forciert, stets im Sinne auch der LCAP-Definition "abstracting and minimizing or replacing the coding"
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Visual-programming-language.png">
<h2 class="wikipediabg">Visual Coding, block-based</h2>
<aside class="notes">
Diese Varianten des visuallen Programmierens betonen _Blöcke_ als Basiselemente
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Flow-based-programming.png">
<h2 class="wikipediabg">Visual Coding, flow-based</h2>
<aside class="notes">
Im Unternehmenseinsatz finden sich typischerweise andere visuelle Darstellungsformen, etwa 
</aside>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Node-RED.png">
<h2 class="wikipediabg">Visual Coding, flow-based, NodeRED</h2>
<aside class="notes">
Im privaten Einsatz findet sich nsw in dr Heimautomatisierung oder NodeRED als Beipsiel für lfow-basiertes visuelles programmeiren
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Windows-Workflow-Foundation.png">
<h2 class="wikipediabg">Visual Coding, flow-based, Windows Workflow Foundation</h2>
<aside class="notes">
In der RPA-Welt bestens bekannt ist Windows Workflow Foundation
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_what-is-visual-programming.png">
<h2>What is VisualProgramming?</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_what-is-visual-programming.png">
<h2>What is VisualProgramming?</h2>
<blockquote class="lcap">Visual programming is a programming language that lets humans describe processes using illustration.<br />
Whereas a typical text-based programming language makes the programmer think like a computer, a visual programming language abstracts the development complexity and minimizes the need to write lines of code. This way, it enables programmers to describe the process in terms that make sense to humans.</blockquote>
<p>Source: https://www.outsystems.com/glossary/what-is-visual-programming/</p>
<aside class="notes">
Ziel ist, mit der Abstrahierung eine weniger formelle Vorbildung vorauszusetzen:
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c3r1x  #circle_c3r11 { fill: #859900 !important}
#c3r1x  #circle_c3r12 { fill: #859900 !important}
</style>
<div id="c3r1x">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
abstracting, minimizing replacing coding: done
</aside>
</section>


</section>





<!-- #Low-Code Capabilities################################################################################ //-->
<section>

<section>
<h1>Low-Code Capabilities</h1>
<aside class="notes">

</aside>
</section>

<section>
<h2>The LCAP-Definition</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform is</strong> an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: <span class="highlight">Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span> Support for developing applications consisting of user interfaces, business logic, workflow and data services; Simplified application test, deployment and management.</blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>
<aside class="notes">
Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Model-view-controller.png">
<h2 class="wikipediabg">Model–view–controller (MVC)</h2>
<aside class="notes">
In der IT wird das Wort model nicht auf dem Laufsteg verortet, sondern oft als Teil vom Model–view–controller design pattern.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Model-view-controller.png">
<h2>Model–view–controller (MVC)</h2>
<blockquote class="lcap">Model–view–controller (MVC) is a software architectural pattern[1] commonly used for developing user interfaces that divide the related program logic into three interconnected elements. This is done to separate internal representations of information from the ways information is presented to and accepted from the user.<br />
Traditionally used for desktop graphical user interfaces (GUIs), this pattern became popular for designing web applications.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Model–view–controller</p>
<aside class="notes">
In der IT wird das Wort model nicht auf dem Laufsteg verortet, sondern oft als Teil vom Model–view–controller design pattern.
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/agilemodeling.com_mda.png">
<h2>Model-driven</h2>
<aside class="notes">
ABER Vorsicht, das ist ein Holzweg! Model-driven architectures sind etwas anderes:
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/agilemodeling.com_mda.png">
<h2>Model-driven</h2>
<blockquote class="lcap">The Model-Driven Architecture (MDA) defines an approach to modeling that separates the specification of system functionality from the specification of its implementation on a specific technology platform. In short it defines a guidelines for structuring specifications expressed as models</blockquote>
<p>Source: http://agilemodeling.com/essays/mda.htm</p>
<aside class="notes">
Diese vorstehende Definition beschreibt eine Art template, und keinesfalls ein Datenbank-Modell!
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_model-driven-development.png">
<h2>Model-driven</h2>
<aside class="notes">
Hier wird der template-Charakter nochmal stärker präzisiert zu einer Art "widget toolkit"
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_model-driven-development.png">
<h2>Model-driven</h2>
<blockquote class="lcap">MDD is a software development methodology that allows users to build complex applications through simplified abstractions of pre-built components</blockquote>
<p>Source: https://www.mendix.com/model-driven-development/</p>
<aside class="notes">
Hier wird der template-Charakter nochmal stärker präzisiert zu einer Art "widget toolkit"
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Widget-toolkit.png">
<h2 class="wikipediabg">Widget Toolkit</h2>
<aside class="notes">
Auch "widget toolkits" können wir nochmal genauer unter die Lupe nehmen
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Widget-toolkit.png">
<h2>Widget Toolkit</h2>
<blockquote class="lcap">A widget toolkit, widget library, GUI toolkit, or UX library is a library or a collection of libraries containing a set of <span class="highlight">graphical control elements</span> (called widgets) used to <span class="highlight">construct the graphical user interface</span> (GUI) of programs.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Widget_toolkit</p>
<aside class="notes">
graphical control elements (called widgets) used to construct the graphical user interface (GUI)
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_model-driven-development.png">
<h2>The Model is a User-Friendly Veneer</h2>
<aside class="notes">
Der Hersteller Mendix wird nochmal deutlicher, wss ein model ist:
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_model-driven-development.png">
<h2>The Model is a User-Friendly Veneer</h2>
<blockquote class="lcap">In model-driven, low-code development, <span class="highlight">the model is a user-friendly veneer that encloses a pre-built application component</span> (pieces of functionality). Each self-contained building block handles all the technical aspects of that component—from logic to user interface to the security and integration concerns—allowing them to operate together seamlessly. The result is a powerful drag-and-drop visual model of abstracted functionality that plays nicely with other components.</blockquote>
<p>Source: https://www.mendix.com/model-driven-development/</p>
<aside class="notes">
Das model ist eine benutzerfreundliche Hülle um eine vorgefertige Komponente
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/dictionary.cambridge.org_dictionary-veneer.png">
<h2>The Model is a User-Friendly Veneer</h2>
<aside class="notes">
Weil die Vokabel nicht zum üblichen office Wortschatz gehört: "veneer" bedeutet auf Deutsch "Furnier": In der Holzverarbeitung wird mit einer dünnen Furnier-Schicht eine hochwertige Oberfläche auf ein Trägermaterial gelegt 
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_No-code-development-platform.png">
<h2 class="wikipediabg">No-Code</h2>
<aside class="notes">
Bei dieser Gelegeneheit soll Low-Code aber auch von No-Code abgegrenzt werden
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_No-code-development-platform.png">
<h2>No-Code</h2>
<blockquote class="lcap">No-code development platforms (NCDPs) allow programmers and non-programmers to create application software through graphical user interfaces and configuration instead of traditional computer programming. No-code development platforms are closely related to low-code development platforms as both are designed to expedite the application development process. However, <span class="highlight">unlike low-code, no-code development platforms require no code writing at all</span>, generally offering prebuilt templates that businesses can build apps with.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/No-code_development_platform</p>
<aside class="notes">
Bei dieser Gelegeneheit soll Low-Code aber auch von No-Code abgegrenzt werden
</aside>
</section>

<section>
<h2>Low-Code: With Scripting</h2>

<blockquote class="lcap">An Enterprise Low-Code Application Platform is an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with <span class="highlight">scripting</span>) to develop a complete application; Support for developing applications consisting of user interfaces, business logic, workflow and data services; Simplified application test, deployment and management.</blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>
<aside class="notes">
Die LCAP Definition "…with scripting" zielt auf diesen Unterschied ab: Bei LowCode kann auch immer noch traditionell code geschrieben werden.
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c4r221  #circle_c4r221 { fill: #859900 !important}
</style>
<div id="c4r221">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
Support for… done
</aside>
</section>




<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/iso25000.com_standards-iso-25010.png">
<h2>Custom Applications</h2>
<aside class="notes">
Commercial off-the-shelf or commercially available off-the-shelf (COTS) products are packaged or canned (ready-made) hardware or software, which are adapted aftermarket to the needs of the purchasing organization, rather than the commissioning of custom-made, or bespoke, solutions.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/iso25000.com_standards-iso-25010.png">
<h2>Custom Applications</h2>
<blockquote class="lcap">Functional Suitability<br />
This characteristic represents the degree to which a product or system provides functions that meet stated and implied needs when used under specified conditions.</blockquote>
<p>Source: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010</p>
<aside class="notes">
Custom apps, also known as bespoke or custom-made apps, are developed specifically for a particular client or organization. They are tailored to meet clients' specific needs, requirements, and preferences. They are typically built from scratch using programming languages such as Java, C#, Python and frameworks like React, Angular, Vue.js, and .Net Core.

They are not available for the general public and can only be used by the organization or client who commissioned them.

</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c5r2  #circle_c5r2 { fill: #859900 !important}
</style>
<div id="c5r2">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
custom applications: done
</aside>
</section>

</section>



<!-- #Support for################################################################################ //-->
<section>

<section>
<h1>Support for…</h1>
</section>


<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c2r3  #circle_c2r3 { fill: #859900 !important}
</style>
<div id="c2r3">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">

</aside>
</section>

<section>
<h2>The LCAP-Definition</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform is</strong> an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application; <span class="highlight">Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span> Simplified application test, deployment and management.</blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_User-interface.png">
<h2 class="wikipediabg">User Interface</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_User-interface.png">
<h2>User Interface</h2>
<blockquote class="lcap">The term "user interface" is often used in the context of (personal) computer systems and electronic devices.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/User_interface</p>
<aside class="notes">
Gemeint sein kann nur ein Graphical User Interface der Applikation sein.
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_gui-graphical-user-interface.png">
<h2>Graphical User Interface</h2>
<aside class="notes">
Gemeint sein kann nur ein Graphical User Interface der Applikation sein.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/gartner.com_gui-graphical-user-interface.png">
<h2>Graphical User Interface</h2>
<blockquote class="lcap">A graphics-based operating system interface that uses icons, menus and a mouse (to click on the icon or pull down the menus) to manage interaction with the system. … A comprehensive GUI environment includes four <span class="highlight">components: a graphics library, a user interface toolkit, a user interface style guide and consistent applications</span></blockquote>
<p>Source: https://www.gartner.com/en/information-technology/glossary/gui-graphical-user-interface</p>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/doc.qt.io_qt-6qt-gui.png">
<h2>Qt Quick Controls QML Types </h2>
<aside class="notes">
Solche Bestandteile eines user interface toolkits sind dann die building blocks für eine "custom application".
Und sollten im Requirements Management fest im Blick sein, um die richtigen Erwartungen zu dokumentieren.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/doc.qt.io_qt-6qt-gui.png">
<h2>Qt Quick Controls QML Types </h2>
<ul>
<li>Layouts</li>
<li>Button</li>
<li>Calendar</li>
<li>CheckBox</li>
<li>Container</li>
<li>ListElement</li>
<li>Menu</li>
<li>Popup</li>
<li>ProgressBar</li>
<li>TextField</li>
<li>ToolTip</li>
<li>and many more</li>
</ul>
<aside class="notes">
Als ein Beispiel für ein interface toolkit hier ein Auszug dessen, was Qt als "types" bereitstellt:
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Business-logic.png">
<h2 class="wikipediabg">Business Logic and Workflows</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Business-logic.png">
<h2>Business Logic and Workflows</h2>
<blockquote class="lcap">In computer software, business logic or domain logic is the part of the program that encodes the real-world business rules that determine <span class="highlight">how data can be created, stored, and changed</span>.<br />It is contrasted with the remainder of the software that might be concerned with lower-level details of managing a database or displaying the user interface, system infrastructure, or generally connecting various parts of the program.</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Business_logic</p>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_IPO-model.png">
<h2 class="wikipediabg">IPO-Model</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_IPO-model.png">
<h2>IPO-Model</h2>
<blockquote class="lcap">The input–process–output (IPO) model, or input-process-output pattern, is a widely used approach in systems analysis and software engineering for describing the structure of an information processing program or other process. …<br />A computation based on the requirement (process)</blockquote>
<p>Source: https://en.wikipedia.org/wiki/IPO_model</p>
<aside class="notes">

</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c4r3  #circle_c4r3 { fill: #859900 !important}
</style>
<div id="c4r3">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">

</aside>
</section>


<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Workflow.png">
<h2>Workflow</h2>
<aside class="notes">
Der Begriff 'workflow' muss aber erst präzisiert werden, denn zunächst ist damit nicht nur IT oder Software gemeint.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Workflow.png">
<h2>Workflow</h2>
<blockquote class="lcap">A workflow consists of an orchestrated and repeatable pattern of activity, enabled by the systematic organization of resources into processes that transform materials, provide services, or process information.<br />
…may refer to a document, service, or product…</blockquote>
<p>Source: https://en.wikipedia.org/wiki/Workflow</p>
<aside class="notes">
Der Begriff 'workflow' muss aber erst präzisiert werden, denn zunächst ist damit nicht nur IT oder Software gemeint.
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Workflow-engine.png">
<h2 class="wikipediabg">Workflow Engine</h2>
<aside class="notes">
Schauen wir beim verwandten Begriff Workflow Engine nach, auf das hier Wesentliche gekürzt:
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Workflow-engine.png">
<h2>Workflow Engine</h2>
<blockquote class="lcap">A workflow engine manages and monitors the state of activities in a workflow, (…) and determines which new activity to transition to according to defined processes (workflows). … A workflow engine facilitates the flow of information, tasks, and events. (…)<br />
Workflow engines mainly have three functions:<br />
<ol><li>Verification…</li>
<li>Determine the authority of users…</li>
<li>Executing condition script: After passing the previous two steps, the <span class="highlight">workflow engine executes the task, and</span> if the execution successfully completes, it returns the success, if not, it reports the error…</li>
</ol></blockquote>
<p>Source: https://en.wikipedia.org/wiki/Workflow_engine</p>
<aside class="notes">
Schauen wir beim verwandten Begriff Workflow Engine nach, auf das hier Wesentliche gekürzt:
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Workflow-management-system.png">
<h2 class="wikipediabg">Workflow Management System</h2>
<blockquote class="lcap">…Windows Workflow Foundation…</blockquote>
<aside class="notes">
Schauen wir nach konkreten Produkten für diese Funktionalitäten so findet sich neben Bizagi, Camunda oder Salesforce.com auch

> Windows Workflow Foundation
Jede Implementation von workflows wird ihre eigenen Stärken und Schwächen haben. Eine BPMN-basierte workflow enginge wird sich mit lang laufenden workflows deutlich leichter tun als flüchtige Implementationen ohne state persistence.
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c5r3  #circle_c5r3 { fill: #859900 !important}
</style>
<div id="c5r3">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
workflow: done - kommen wir zu data
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/developer.android.com_data-layer.png">
<h2>Data Services</h2>
<aside class="notes">
Ob als Eingabe und Ausgabe nach IPO/EVA oder als Speicherort im MVC: Daten werden logisch oder physisch bei Applikationen mit GUI von der domain logic zugegriffen, oder bei Automatisierungen von workflows verarbeitet.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/developer.android.com_data-layer.png">
<h2>Data Services</h2>
<blockquote class="lcap">Data layer architecture<br />
The data layer … zero to many data sources.</blockquote>
<p>Source: https://developer.android.com/topic/architecture/data-layer</p>
<aside class="notes">
Im Kontext von LCAP werden oft data sources mit GUI Elementen verknüpft. So kann bsw ein ListElement des interface toolkits mit einer Tabelle verknüpft werden, um dann ein Dropdown-Element zu befüllen.
</aside>
</section>


<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c6r3  #circle_c6r3 { fill: #859900 !important}
</style>
<div id="c6r3">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
damit hätten die den vorletzten Teil der Definition auch seziert 
</aside>
</section>


</section>






<!-- #Simplification################################################################################ //-->
<section>

<section>
<h1>Simplification</h1>
<aside class="notes">

</aside>
</section>


<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c2r4  #circle_c2r4 { fill: #859900 !important}
</style>
<div id="c2r4">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">

</aside>
</section>

<section>
<h2>The LCAP-Definition</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform is</strong> an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application; Support for developing applications consisting of user interfaces, business logic, workflow and data services; <span class="highlight">Simplified application test, deployment and management.</span></blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/ibm.com_software-testing.png">
<h2>Simplified Application Test</h2>
<aside class="notes">
Die LCAP Definition betont vermutlich deshalb "simplified", weil die QA quality assurance durch testing in ihrer Komplexität der eigentlichen Entwicklung wohl kaum nachsteht.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/ibm.com_software-testing.png">
<h2>Simplified Application Test</h2>
<blockquote class="lcap">Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do.</blockquote>
<p>Source: https://www.ibm.com/topics/software-testing</p>
<aside class="notes">
Die LCAP Definition betont vermutlich deshalb "simplified", weil die QA quality assurance durch testing in ihrer Komplexität der eigentlichen Entwicklung wohl kaum nachsteht.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/ibm.com_types-software-testing.png">
<h2>Types of Software Testing</h2>
<blockquote class="lcap">There are many different types of software tests, each with specific objectives and strategies:<br />
<ul>
<li>Acceptance testing</li>
<li>Integration testing</li>
<li>Unit testing</li>
<li>Functional testing</li>
<li>Performance testing</li>
<li>Regression testing</li>
<li>Stress testing</li>
<li>Usability testing</li>
</ul>
</blockquote>
<p>Source: https://www.ibm.com/topics/software-testing</p>
<aside class="notes">
Schon allein die typischen Arten von Software Testing zeigen die Vielfalt:
</aside>
</section>

<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c3r4  #circle_c3r4 { fill: #859900 !important}
</style>
<div id="c3r4">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">
testing done, kommen wir zu deployment und management
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Software-maintenance.png">
<h2 class="wikipediabg">Deployment and Management</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/wikipedia.org_Software-maintenance.png">
<h2>Deployment and Management</h2>
<blockquote class="lcap">Software deployment is all of the activities that make a software system available for use.
</blockquote>
<p>Source: > https://en.wikipedia.org/wiki/Software_deployment</p>
<blockquote class="lcap">Software maintenance in software engineering is the modification of a software product after delivery to correct faults, to improve performance or other attributes.<br />
A common perception of maintenance is that it merely involves fixing defects.
</blockquote>
<p>Source: > https://en.wikipedia.org/wiki/Software_maintenance</p>
<aside class="notes">
Aktuelle deployment Prozesse sind typischerweise vollautomatisiert, und haben als Installationsziel mitunter auch nur kurzlebige virtuelle Serversysteme, die nur für die Dauer der Nutzung exitsieren. 
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_app-lifecycle-deployment.png">
<h2>Deployment and Management</h2>
<aside class="notes">
Eingebettet in zyklische Modelle ist Deployment und Management ein wiederkehrender Prozess, welcher von den LCA Platformen entsprechen untersützt werden soll.
</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/mendix.com_app-lifecycle-deployment.png">
<h2>Deployment and Management</h2>
<blockquote class="lcap">Mendix applications run on the platform’s cloud-native stateless runtime architecture that conforms to Twelve-Factor App principles with support for modern cloud platforms such as Docker, Kubernetes and Cloud Foundry. As a result, Mendix apps benefit from auto-scaling, auto-provisioning, auto-healing, low infrastructure overhead, CI/CD, and cloud interoperability out of the box.</blockquote>
<p>Source: https://www.mendix.com/evaluation-guide/app-lifecycle/deployment/</p>
<aside class="notes">
The Twelve Factors
I. Codebase 
II. Dependencies 
III. Config 
IV. Backing services 
V. Build, release, run 
VI. Processes 
VII. Port binding 
VIII. Concurrency 
IX. Disposability 
X. Dev/prod parity 
XI. Logs 
XII. Admin processes 
</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_what-kind-of-monitoring-and-analytics-does-outsystems-offer.png">
<h2>Deployment and Management</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_what-kind-of-monitoring-and-analytics-does-outsystems-offer.png">
<h2>Deployment and Management</h2>
<blockquote class="lcap">Comprehensive auditing and monitoring tools built into OutSystems enable a proactive management of application performance and make it easier to detect problems by allowing the identification of performance issues in real-time.</blockquote>
<p>Source: https://www.outsystems.com/evaluation-guide/what-kind-of-monitoring-and-analytics-does-outsystems-offer/</p>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_configuration-management-for-outsystems-applications.png">
<h2>Deployment and (Configuration-) Management</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_configuration-management-for-outsystems-applications.png">
<h2>Deployment and (Configuration-) Management</h2>
<blockquote class="lcap">OutSystems enables all sorts of runtime configurations, such as scheduling of batch jobs, database connections, web-service endpoints, business properties and versions.</blockquote>
<p>Source: https://www.outsystems.com/evaluation-guide/configuration-management-for-outsystems-applications/</p>
<aside class="notes">

</aside>
</section>

<section data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_identity-and-access-management.png">
<h2>Deployment and (Identity-) Management</h2>
<aside class="notes">

</aside>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/community/IAU-BS-WOB/2023-02-22/resources/screenshots/outsystems.com_identity-and-access-management.png">
<h2>Deployment and (Identity-) Management</h2>
<blockquote class="lcap">Identity and access management<br />
OutSystems offers full support for identity management, including user management, and groups.<br />
Governance of applications is achieved by configuring groups and assigning them to end-users.</blockquote>
<p>Source: https://www.outsystems.com/evaluation-guide/identity-and-access-management/</p>
<aside class="notes">

</aside>
</section>


<section>
<h2>LCAP in 20 circles: We are here</h2>
<style>
.circle { fill: #cb4b16 !important}
#c5r4  #circle_c5r4 { fill: #859900 !important}
</style>
<div id="c5r4">{% include_relative resources/visualizations/LCAPDefinitionRoadmap_.svg %}</div>
<aside class="notes">

</aside>
</section>

</section>





<section>
<h2>Intelligent Automation and Low-Code</h2>
<img src="{{ "/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png" | prepend: site.baseurl }}" alt="" class="resize">
<aside class="notes">

</aside>
</section>



<section>
<h2>The LCAP-Definition</h2>

<blockquote class="lcap"><strong>An Enterprise Low-Code Application Platform is</strong> an application platform that is used to rapidly develop and deploy custom applications by abstracting and minimizing or replacing the coding needed in development. At a minimum, an LCAP must include: Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application; Support for developing applications consisting of user interfaces, business logic, workflow and data services; Simplified application test, deployment and management.</blockquote>
<p>Source: https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</p>
<aside class="notes">

</aside>
</section>