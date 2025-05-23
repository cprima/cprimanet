---
layout: presentation_v1.2.2
title: "Yet Another Raspberry Pi Cluster"
excerpt: "The slides of a lecture/presentation on 2016-03-20 @ Chemnitzer Linux Tage"
author: "Christian Prior"
dummycontent: false
theme: solarized
---

<!-- template                                   -->
<section>

<section style="text-align: center;" data-background="/biz/marketing/broadcastdesign/broadcastdesignFullHD.png">

</section>

<section style="text-align: center;" data-background="/biz/marketing/broadcastdesign/broadcastdesignFullHD.png" style="background-size: contain;">

</section>

<section style="text-align: center;">
<img src="{{ "/biz/marketing/broadcastdesign/broadcastdesignFullHD.png" | prepend: site.baseurl }}" alt="" style="float: right">
</section>

</section>


<!-- preface                                   -->
<section>

<section style="text-align: center;">
<h2>Slides available</h2>



<p><a href="{{ "/business/marketing/presentation/CLT_2016-03-20" | prepend: "http://www.helotism.de" }}" >
http://www.helotism.de \ ⏎<br />
/business/marketing/presentation/CLT_2016-03-20
</a></p>

</section>
<section data-markdown>
## about me
![]({{ "/business/marketing/presentation/images/about-cpr.svg" | prepend: site.baseurl }})

https://www.facebook.com/profile.php?id=100010639868228

https://github.com/cprior

</section>


<!-- http://bgrins.github.io/TinyColor/ -->
<section tagcloud data-state="">
<h2>Content of today's presentation</h2>
    <span tagcloud-color="#859900" tagcloud-link="1" tagcloud-weight="100">[Maker] </span>
    <span tagcloud-color="#aac300" tagcloud-link="4" tagcloud-weight="50">CNC, CAD&CAM </span>
    <span tagcloud-color="#cfee00" tagcloud-link="5" tagcloud-weight="80">development boards </span>
    <span tagcloud-color="#606e00" tagcloud-link="5" tagcloud-weight="90">power supply </span>
    <span tagcloud-color="#b58900" tagcloud-link="2" tagcloud-weight="100">[SysAdmin] </span>
    <span tagcloud-color="#dfa900" tagcloud-link="2" tagcloud-weight="90">Config&nbsp;Mgt </span>
    <span tagcloud-color="#604900" tagcloud-link="2" tagcloud-weight="70">monitoring </span>
    <span tagcloud-color="#dc322f" tagcloud-link="3" tagcloud-weight="100">[Data&nbsp;Analysis] </span>
    <span tagcloud-color="#b12826" tagcloud-link="3" tagcloud-weight="70">data&nbsp;provider </span>
    <span tagcloud-color="#871f1d" tagcloud-link="3" tagcloud-weight="40">visualization</span>
    <span tagcloud-color="#268bd2" tagcloud-link="3" tagcloud-weight="100">[Documentation] </span>
</section>



<section>
<h2>Helotism</h2>
Wiktionary.org: Helotism (zoology): A form of mutualism in which one species is forced to perform tasks for another, for their mutual benefit.
</section>

<section>

<h2>The Goals</h2>

<img src="{{ "/technology/physical/images/boards.svg" | prepend: site.baseurl }}" alt="boards" width="30%" style="float: right">

<ul style="width: 60%;">
<li>keeping up with IT changes</li>
<li>solid Linux sysadmin skills are the foundation for "Big Data"</li>
<li>getting most out of these boards</li>
<li>getting ahead of the complexity curve</li>
</ul>
</section>

</section>


<!-- business                                   -->
<section>

<section data-domain="business">
	<h2>The Roadmap</h2>
<link rel="stylesheet" type="text/css" href="/business/marketing/website/assets/DataTables/datatables.min.css"/>

<script src="{{ "/business/marketing/website/assets/DataTables/datatables.min.js" | prepend: site.baseurl }}"></script>
<script src="{{ "/business/marketing/website/assets/js/d3.v3.min.js" | prepend: site.baseurl }}"></script>

<script>


$(document).ready(function() {
    d3.text('{{ "/business/planning/roadmap.csv" | prepend: site.baseurl }}', function (datasetText) {
  var rows = d3.csv.parseRows(datasetText);

  var tbl = d3.select("#roadmapcontainer")
    .append("table")
    .attr("class", "display")
    .attr("id","tableID");


// headers
  tbl.append("thead").append("tr")
    .selectAll("th")
    .data(rows[0])
    .enter().append("th")
    .text(function(d) {
        return d;
    });

   // data
    tbl.append("tbody")
    .selectAll("tr").data(rows.slice(1))
    .enter().append("tr")

    .selectAll("td")
    .data(function(d){return d;})
    .enter().append("td")
    .text(function(d){return d;})
        $('#tableID').dataTable( {
        paging: true,
        pageLength: 2,
        pagingType: "full_numbers",
        responsive: true,
        columnDefs: [
            { targets: [0, 1, 2, 4], visible: true},
            { targets: '_all', visible: false }
        ]
        } );
    });
});

</script>
<div id="roadmapcontainer"></div>

</section>

<section data-domain="business">
<h2>The Repo</h2>

<p>https://github.com/helotism</p>

<ul>
<li>all-in one repo</li>
<ul><li>hardware</li>
<li>software</li>
<li>promotion</li></ul>
<li>Issues welcome! ;)</li>
</ul>


</section>

<section data-markdown data-domain="business">
##Jekyll Website

helotism.de

```YAML
#_config.yml
destination:  ./business/marketing/website/_site
```

</section>

<section data-markdown data-domain="business">
## ERP
![]({{ "/business/production/HowThingsAreMade.svg" | prepend: site.baseurl }})
</section>

<section data-domain="business">
<!-- https://github.com/hakimel/reveal.js/issues/841 -->
<h2>TOGAF: Architecture Development Method</h2>

<img src="{{ "/business/planning/images/togaf-ADM.png" | prepend: site.baseurl }}" alt="TOGAF ADM" width="30%" style="float: right">
<ul style="width: 60%;">

<li>P Prerequisites</li>
<li>A Vision</li>
<li>B Business Plan/Action</li>
<li>C Information System Plan/Actual</li>
<li>D Technology Plan/Actual</li>
<li>E Opportunities and Solutions</li>
<li>F Migration Planning</li>
<li>G Implementation Governance</li>
<li>H Change Management</li>
<li>R Requirements</li>
</ul>
</section>
<section data-markdown data-domain="business">
##TOGAF: "Domains" & Building Blocks
![]({{ "/business/planning/images/PRDV_TOGAF-Cube_BusinessDataApplicationTechnology.jpg" | prepend: site.baseurl }})
</section>



</section>


<!-- technology                                   -->
<section>
<section data-markdown data-domain="technology">
##Maker

- DXF
- chipping vs. 3D-printing
- CAD4c Computer-Aided Design for clamping

</section>

<section data-domain="technology">
<h2>Enthusiast's Small Batch Manufacturing</h2>

<ul style="width:24%; list-style-type: none; ">
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160310-WA0000_640x.jpg" | prepend: site.baseurl }}' alt="This material is easy to mill…"></li>
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160310-WA0004_640x.jpg" | prepend: site.baseurl }}' alt="…but quite expensive so nesting was important."></li>
</ul>
<ul style="width:24%; list-style-type: none; ">
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160310-WA0002_640x.jpg" | prepend: site.baseurl }}' alt="Quite some work ahead!"></li>
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160310-WA0005_640x.jpg" | prepend: site.baseurl }}' alt="Chamfered parts."></li>
</ul>
<ul style="width:24%; list-style-type: none; ">
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160310-WA0001_640x.jpg" | prepend: site.baseurl }}' alt="Additional hardware attached."></li>
<li><img src='{{ "/business/marketing/presentation/images/custom-tackle-prior/IMG-20160222-WA0002_640x.jpg" | prepend: site.baseurl }}' alt="Testrun paiting technique."></li>
</ul>

</section>

</section>


<section>

<section data-domain="technology">
	<h2>Development Boards</h2>

The market for development boards is confusing: https://en.wikipedia.org/wiki/Comparison_of_single-board_computers is a good overview.

</section>

<section data-markdown data-domain="technology">

##Development Boards: Common Features

- Computation: Processor and Memory
- Communication through Ethernet/…
- Powersupply: Consumption, buttons
- Interaction via GPIO
- Fixture: Mounting holes and dimensions
- Storage: SD cards and beyond
- Synchronization: RTC time

</section>

<section data-domain="technology">
	<h2>Dimensions</h2>
	<p>-> see repo</p>
</section>

<section data-markdown data-domain="technology">
##Power Consumption

Rule of thumb:

- 1 Pi idle == 2.5W (5V * 0,5 A)
- 1 Pi under load, no USB == 5W (5V * 1 A)

Caveat: GPIO-pins are no USB ports ;)
- 5V passed straight through from USB
- 3.3V rail max 50mA
- GPIO pins 16ma in total

</section>

<section data-domain="technology">
	<h2>Minnowboard</h2>
	<p>UEFI</p>
</section>

<section data-markdown data-domain="technology">
##Operating System

1. archlinuxarm.org
  * all saltstack dependencies met
2. archlinuxarm.org
  * up-to-date systemd (229-3 in march 2016)
3. archlinuxarm.org
  * pre-compiled ;)
4. Raspbian/DietPi/Debian Jessie
  * Raspbian "Jessie" December 2015, systemd "216"
</section>

</section>


<section>

<section data-markdown data-domain="technology">
##Circuits
![]({{ "/technology/logical/images/MIT_CircuitsElectronics_Lec1_outline.svg" | prepend: site.baseurl }})
</section>

<section data-markdown data-domain="technology">
##Alles wegabstrahieren!
![]({{ "/business/marketing/presentation/images/cpr_travel_pictures_2013-08-28_IMG_0533_1024-360.jpg" | prepend: site.baseurl }})
</section>


<section data-markdown data-domain="technology">
##Noise
![]({{ "/technology/logical/images/ElectricalWireNoise.svg" | prepend: site.baseurl }})
</section>

<section data-markdown data-domain="technology">
##Discretization
![]({{ "/technology/logical/images/ElectricalDiscretization.svg" | prepend: site.baseurl }})
</section>

<section data-markdown data-domain="technology">
##Debouncing
![]({{ "/technology/logical/images/ElectricalSwitchDebounce.svg" | prepend: site.baseurl }})
</section>

</section>


<section>

<section data-markdown data-domain="technology">
##Powersupply

- prevent brown-out
- one switch for all boards

</section>

<section data-markdown data-domain="technology">
##On-Off-Switch


- hardware
- code

![]({{ "/technology/physical/myrack-v0.5/circuit/helotism_powersupply_bb_640x312.png" | prepend: site.baseurl }})

[raspberry-pi-geek.com On-Off-Switch](http://www.raspberry-pi-geek.com/Archive/2013/01/Adding-an-On-Off-switch-to-your-Raspberry-Pi "Adding an On/Off switch to your Raspberry Pi")

</section>

<section data-markdown data-domain="technology">
##scale out

</section>

<section data-markdown data-domain="technology">
##Python logic…

```Python
b = mraa.Gpio(20)
b.dir(mraa.DIR_IN)
b.isr(mraa.EDGE_FALLING, handleInterrupt, handleInterrupt)
```

```Python
def handleInterrupt(args):
    #print("handleInterrupt")
    button20.pressed = True #that's a fact, but...
    button20.pressed_debounced = False
    interrupted_at = datetime.datetime.now()
    debounce_until = interrupted_at + datetime.timedelta(0,3)

    while True:
      if (datetime.datetime.now() > debounce_until):
          #print("past debounce")
          journal.send('GPIO20 pressed DEBOUNCED.', FIELD2='GPIO20')
          button20.pressed_debounced = True
          return
      else:
          #print("not debounced yet")
          journal.send('GPIO20 pressed, not debounced', FIELD2='GPIO20')
      time.sleep(0.5) #inside this interrupt handler only
```
</section>


<section data-markdown data-domain="technology">
##…and systemd daemonization.

```INI
[Unit]
Description=An GPIO interrupt listener
After=local-fs.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'cd /opt/helotism/powersupply-env; \
                        source bin/activate; \
                        python ./mraa_interrupt.py'

[Install]
WantedBy=multi-user.target
```
</section>

</section>


<!-- application                                   -->

<section>

<section data-markdown data-domain="application">
##SaltStack Ecosystem
![]({{ "/application/physical/images/saltstack-ecosystem.svg" | prepend: site.baseurl }})
</section>

<section data-markdown data-domain="application">

##SaltStack top file

```YAML
base:          # environment
  'web*':      # targeted minions
    - apache   # state file 'apache.sls'
```

- the top.sls is a special state file as "entry point" into the fileserver

- "apache" references ```./apache.sls``` file

</section>

<section data-markdown data-domain="application">

##SaltStack state file

```YAML
#apache.sls
{% raw %}{% if grains['os'] == 'Debian' %}
apache: apache2
{% elif grains['os'] == 'RedHat' %}
apache: httpd
{% endif %}{% endraw %}
```

- Jinja2 template language

- one should read the fine manual: http://jinja.pocoo.org/docs/dev/

</section>

<section data-markdown data-domain="application">

##SaltStack environments

```YAML
file_roots:
  dev:
    - /srv/salt/dev
  base:
    - /srv/salt
```

- environments are configured in the master config file

</section>

<section data-markdown data-domain="application">
##SaltStack fileserver
```YAML
fileserver_backend: #first filename match wins
  - roots
  - git

gitfs_remotes:
  - git://github.com/example/first.git
  - https://github.com/example/second.git
    - root: salt            #subdirectory
    - mountpoint: salt://sub/dir
    - base: myTag05         #git branch
  - file:///root/third

#top_file_merging_strategy: merge #same
#env_order: ['base', 'dev', 'prod']
```

- these are powerful configuration mechanisms: "infrastructure as code" served from a Git repo

- many ways to segment or override

</section>

<section data-markdown data-domain="application">
##Sample Salt Usage

```bash
#remote execution?
salt '*' cmd.run 'uname -a'
```

```bash
#listing and accepting keys
salt-key -L
salt-key -A
```

```bash
#salt.modules.test.ping
salt '*' test.ping
```

```bash
#targeting by grains
salt -G 'os:(RedHat|Debian)' test.ping
```

```bash
#more sound than test.ping
salt-run manage.up
```

```bash
#apply common.sls on all (accepted) minions
salt '*' state.sls common
#This is the "endgame" in salt
salt '*' state.highstate
#remote execution!
salt '*' cmd.run 'uname -a'
```

</section>

</section>




<!-- prospect                                   -->
<section>
<section data-markdown >
##ToDo: Scale-down and Simplify

- three RPi 2 or RPi3
- bootstrap.sh script from ArchLinux ARM iso to "cluster"
- keep formfactor to a minimum
  - still a switch is needed
  - and a button
  - and a RTC

</section>

<section data-markdown >
##ToDo: More Hardware Diversity

- PINE64
- GBit ethernet wanted

</section>

<section data-markdown data-domain="application">
##ToDo: Config Mgt and IoT
![Microsoft Applications on Linux]({{ "/business/marketing/presentation/images/kickstarter_micro-python.jpg" | prepend: site.baseurl }})
</section>


</section>








