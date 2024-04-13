---
layout: presentation_v1.1.0
title: "The ${HOME}Lab"
date: 2023-03-25 00:00:00 +0100
abstract: Starting with a definition, digging into individual aspects
excerpt: Starting with a definition, digging into individual aspects
published: true
titleimagefull: /tec/log/homelab/images/cprima_a_sandbox_for_children_in_a_small_room_filled_with_bucke_6e10848b-9de8-48ec-80f6-bd0ffb971780.png
---

<section tagcloud>
    Twitter Bootstrap
    jQuery
    less
    GruntJS
    JSHint
    JSLint
    markdown
    sass
    jade
    coffeescript
    codekit
    livereload
    web-build
    jQuery UI
    mustache
    emmet.io
    bower
    browserstack
    npm
    RequireJS
    socket.io
    jQuery Mobile
    node.js
    Jasmine
 </section>

<section data-background-opacity="1.0" data-state="filterblurfoobarbaz" data-background="/tec/log/homelab/images/cprima_a_sandbox_for_children_in_a_small_room_filled_with_bucke_6e10848b-9de8-48ec-80f6-bd0ffb971780.png">
<h2>What is the ${HOME}Lab?</h2>

learning platform, playground, testbed, sandbox, …

caveat: usecases with 24/7 availability are by my definition not a "lab"

</section>

<section data-markdown>

where to go

- r/homelab

</section>

<section data-markdown>

# components

1. power

1. storage

1. network

1. compute

1. cablemanagement

1. heat

1. system management

1. racks

1. examples

1. (costs)

1. tools

</section>

<section> <!-- begin section -->
<section data-markdown>

## power

- voltage

- form factor

- consolidate powersupply in e.g.

  - 1 unit 12 V 30 A
  - 1 unit 5V 10 A

- chose network switch by voltage

- DC: "easy", permitted

- (fuses)

- typically out of scope of a homelab: hot-swappable, redundant power supplies, UPS

</section>

<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<h2 style="position: fixed; bottom: 0; width: 100%; margin: 0px 0px 64px 0px;">bar</h2>

</section>

<section  data-background="/tec/log/ElectricalEngineering/images/CircuitsAndElectronics.png">

</section>

<section data-markdown>

# Ohm's law

R = U / I

</section>

<section data-markdown>

# tricks

- step-down converter (buck converter)

- more efficient than step-up converter (boost converter)

- Raspberry Pi foundation: 5V 3A (with very clean power)

</section>

</section> <!-- end section -->

<section data-markdown>

## storage

easiest of all

- SD cards (Raspberry Pi)

- SSDs (SATA, NVMe)

- costs: almost linear with capacity

- shared storage, e.g. NAS or Samba 4 //don't enable SMB1 on main computer just because of Samba 3 in homelab

</section>

<section data-markdown>

## compute

- embrace the power-saving ARM architecture and laptop-typical computing power

- single-board computers (SBCs) like Raspberry Pi, Odroid, Rock64, …

- select for OS support: GNU/Linux keeps the cost down

- add Windows (and MacOS) for completeness, if needed

- cost-effective: Raspberry Pi, Lenovo ThinkCentre Tiny, (Intel NUC)

- try SFF small form factor over even Mini-ITX

</section>

<section data-markdown>

## network

- 1 Gbit/s is good enough for everybody! ;)

- the advantage of a physical homelab: When the LED is blinking, you know that something is happening.

- a travel router can be used to isolate the homelab from the rest of the network

- early decision: available from the internet yes/no?

- in 2024: still ipv4…

</section>

<!-- -->
<section data-markdown>

## Learning

hands-on

reduced complexity, reduced barrier

IT learning typically autonomous and self-paced, no teachers or courses as guidance.

</section>

<section data-markdown>

## cable management

- separate cable runs of power and data cables!

// welding instructor: roll out the cable

</section>

<section data-markdown>

## heat

</section>

<section data-markdown>

## system management

- Ansible, Puppet, Chef, (Salt), …

- monitoring: Prometheus, Grafana, Netdata …

- Windows: Embrace Chocoloatey!

- documentation

- backup?

- (virtualization) (Proxmox, …)

- https://pikvm.org/

</section>

<section data-markdown>

## costs

- 50 - 500+ €

- reuse old hardware

- buy refurbished

- cables and connectors add up!

- power consumption

</section>

<section data-markdown>

## racks

- IKEA!

- DIN rail

- music rack 19"

- wooden rack DIY

</section>

<section data-markdown>

## examples

- TuringPi

- Raspberry Pi cluster

- 19" rack

</section>

<section data-markdown>

## tools

- cable stripper(s)

- cable ties

- screwdrivers

- network crimp

- power drill

- …

</section>

<section>
<h2>Intelligent Automation and Low-Code</h2>
<img src="{{ "/tec/log/homelab/images/cprima_a_sandbox_for_children_in_a_small_room_filled_with_bucke_6e10848b-9de8-48ec-80f6-bd0ffb971780.png" | prepend: site.baseurl }}" alt="" class="resize">
</section>

<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<h2 style="position: fixed; bottom: 0; width: 100%; margin: 0px 0px 64px 0px;">bar</h2>
<div class="container">
<div class="col" style="padding-top: 20px; height: 100vh; background-image: linear-gradient(to right, rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,0));"><h3>Code</h3><p style="text-align: left; top: 50%; position: absolute; transform: translateY(-50%); padding-left: 100px; width: 35%;">foo<br />Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</div>
<div class="col"></div>

</div>
</section>

<section style="height:100%; width:100%;" class="center" data-background="/tec/log/ElectricalEngineering/images/powersupply-12V-30A.jpg">
<h2 style="position: fixed; bottom: 0; width: 100%; margin: 0px 0px 64px 0px;">bar2</h2>
<div class="container">
<div class="col">&nbsp;
</div>
<div class="col" style="padding-top: 20px; height: 100vh; background-image: linear-gradient(to right, rgba(238,232,213,0), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9), rgba(238,232,213,.9));"><h3>Code</h3><p style="text-align: left; top: 50%; position: absolute; transform: translateY(-50%); padding-left: 200px;">foo<br />Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br />baz</p>
</div>

</div>
</section>
<section>
<h2>bar</h2>
</section>

<section data-background-opacity="0.1" data-state="filterblur" data-background="/biz/IT/IntelligentAutomation/resources/images/intelligent-automation-capabilities.png">
<h2>Low-Code and Intelligent Automation</h2>
<p>RPA and Low-Code: Sister technologies in the Intelligent Automation space</p>
<figure>
    <blockquote class="lcap" cite="https://www.example.com">The <strong>Execution</strong> capability … include smart workflow and low-code platforms, and robotic process automation (RPA). This capability is a foundation for end-to-end automated process delivery. It acts as a glue, connecting the technologies across the capabilities.</blockquote>
    <figcaption>Source: <cite>Pascal Bornet et al. (2020) Intelligent Automation,WSPC.</cite></figcaption>
</figure>
</section>

<section>
<h2>The LCAP-Definition — step by step</h2>
<figure>
    <blockquote class="lcap" cite="https://www.gartner.com/reviews/market/enterprise-low-code-application-platform<"><strong>An Enterprise Low-Code Application Platform is</strong> <span class="fragment fade-in-then-semi-out">an application platform that is used to</span><span class="fragment fade-in-then-semi-out"> rapidly develop and deploy</span><span class="fragment fade-in-then-semi-out"> custom applications</span><span class="fragment fade-in-then-semi-out"> by abstracting and minimizing or replacing the coding needed in development.</span><span class="fragment fade-in-then-semi-out"> At a minimum, an LCAP must include:</span><span class="fragment fade-in-then-semi-out"> Low-code capabilities (such as a model-driven or graphical programming approach with scripting) to develop a complete application;</span><span class="fragment fade-in-then-semi-out"> Support for developing applications consisting of user interfaces, business logic, workflow and data services;</span><span class="fragment fade-in-then-semi-out"> Simplified application test, deployment and management.</span></blockquote>
    <figcaption>Source: <cite>https://www.gartner.com/reviews/market/enterprise-low-code-application-platform</cite></figcaption>
</figure>
</section>

<section>
<h2>animate appearance</h2>
<ul>
    <li class="animate__bounceInUp">Add it to any text element</li>
    <li class="animate__bounceInUp">Like list items, or headers.</li>
    <li class="animate__bounceInUp">It adds some attention.</li>
</ul>
</section>

<section class="center present" style="top: 178.5px; display: block;" data-fragment="0" data-appearance-can-start="true">
    <h2>Inside fragments</h2>
    <p class="animate__fadeInDown animate__animated">Like this <span class="animate__fadeInDown animate__faster animate__animated" style="font-size: 0.9em; animation-delay: 300ms;">(click next)</span>:</p>
    <div class="fragment visible current-fragment" data-fragment-index="0">
        <ul>
            <li class="animate__bounceInUp" style="animation-delay: 0ms;">Add it to any text element</li>
            <li class="animate__bounceInUp" style="animation-delay: 300ms;">Like list items, or headers.</li>
            <li class="animate__bounceInUp" style="animation-delay: 600ms;">It adds some attention.</li>
        </ul>
    </div>
</section>

<section class="center present" data-autoappear="" style="top: 137px; display: block;" data-appearance-can-start="true">
                <h2>Autoappear mode</h2><small>Sometimes (for example with Markdown), adding classes to elements is a chore. Appearance can automatically add animation classes to specific elements (tags or other selectors) in the presentation (with the option <code>autoappear</code>) or per slide (with <code>data-autoappear</code>), like this slide.</small>
                <ul>
                    <li class="animate__animated animate__fadeInLeft">This is list item 1</li>
                    <li class="animate__animated animate__fadeInLeft" style="animation-delay: 300ms;">This is list item 2</li>
                    <li class="animate__animated animate__fadeInLeft" style="animation-delay: 600ms;">This is list item 3</li>
                </ul>
                <p><small>Seems not to work when transition via spacebar //CPM</small></p>
</section>

<section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with some text and a [link](https://hakim.se).
    ---
    ## Slide 2
    ---
    ## Slide 3
  </textarea>
</section>

<section data-markdown>
    <script type="text/template">
    <!-- .slide: class="center" -->
    ## Test
        Markdown content
    </script>
</section>

<section data-markdown>
  <script type="text/template">
  <!-- .slide: data-background="#ff0000" -->
    Markdown content
  </script>
</section>

<section data-markdown>
  <script type="text/template">
    ## foo
    - Item 1 <!-- .element: class="fragment" data-fragment-index="2" -->
    - Item 2 <!-- .element: class="fragment" data-fragment-index="1" -->
  </script>
</section>

<section>Horizontal Slide</section>
<section>
    <section>Vertical Slide 1</section>
    <section>Vertical Slide 2</section>
</section>

<section class="center no-bg">
<div style="width: 80%; margin: 0 auto;"><h2 class="r-fit-text">Chapter h2</h2></div>
<p>RPA and Low-Code: Sister technologies in the Intelligent Automation space</p>
</section>

<section data-auto-animate>
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>

<section class="center no-bg" data-auto-animate data-transition="none">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4712 #circle_c1r1 {color: #b48900;  fill: #b48900; transform: translate(1000px, 0px)}
</style>
<svg id="myid4712" width="1280" height="64" version="1.1" viewBox="0 0 1280 64" xmlns="http://www.w3.org/2000/svg" style="">
 <g transform="translate(0,0)">
  <path d="m0,32 h1222" stroke="#586e75" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" />
  <g fill="#cb4b16">
   <circle data-id="circle_c1r1" id="circle_c1r1" cx="32" cy="32" r="32" />
   <circle id="circle_c2r1" cx="437" cy="32" r="32" />
   <circle id="circle_c3r1" cx="842" cy="32" r="32" />
   <circle id="circle_c4r1" cx="1248" cy="32" r="32" />
  </g>
 </g>
</svg>
<h2>&nbsp;</h2>
</section>

<section class="center no-bg" data-auto-animate data-transition="none">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4713 #circle_c1r1 {color: #b48900;  fill: #b48900; transform: translate(0px, 0px)}
</style>
<svg id="myid4713" width="1280" height="64" version="1.1" viewBox="0 0 1280 64" xmlns="http://www.w3.org/2000/svg" style="">
 <g transform="translate(0,0)">
  <path d="m0,32 h1222" stroke="#586e75" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" />
  <g fill="#cb4b16">
   <circle data-id="circle_c1r1" id="circle_c1r1" cx="32" cy="32" r="32" />
   <circle id="circle_c2r1" cx="437" cy="32" r="32" />
   <circle id="circle_c3r1" cx="842" cy="32" r="32" />
   <circle id="circle_c4r1" cx="1248" cy="32" r="32" />
  </g>
 </g>
</svg>
<h2>&nbsp;</h2>
</section>

<section data-auto-animate data-transition="none">
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>

<section class="center no-bg">
<h2>test svg</h2>
<?xml version="1.0" encoding="UTF-8"?>
<style>
    #myid4714 #circle_c3r1 {color: #b48900;  fill: #b48900}
</style>
<!-- div id="myid4714">{# % include_relative resources/visualizations/drawing.svg % #}</div -->
<h2>&nbsp;</h2>
</section>

<section>
	<h2>Tablas con información</h2>
	<table>
    	<thead><tr>
            <th>Ciudad</th>
            <th>Año de fundación</th>
            <th>Población</th>
        </tr></thead>
        <tbody><tr>
            <td>Gijón</td>
            <td>Siglo V a. C.</td>
            <td>274290</td>
        </tr>
        <tr>
            <td>Oviedo</td>
            <td>761</td>
            <td>221870</td>
        </tr></tbody>
    </table>
</section>

<section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with some text and a [link](https://hakim.se).
    ---
    ## Slide 2
    ---
    ## Slide 3
  </textarea>
</section>

<section data-markdown>
  <script type="text/template">
    ## foo
| Title | List | Notes |
| --- | --- | --- |
| This is long line for one Location1 | List 1 <!-- .element: style="font-size:50%;" --> | |
| This is long line for one Location2 | List 2 | |
<!-- .element.table: style="font-size:50%;" -->
  </script>
</section>
