---
layout: page
title:  "Technology employed by cprima.net"
permalink: /tec/index.html
categories: [ tec ]
---

## Physical technology components

> A specific technology infrastructure product or technology infrastructure product instance. For example, a particular product version of a Commercial Off-The-Shelf (COTS) solution, or a specific brand and version of server.
> https://pubs.opengroup.org/architecture/togaf9-doc/arch/apdxa.html


<dl>
  {% for component in site.data.taptc %}
  {% if component.visibility == 'public'  %}
      <dt><a href="{{ "/tec/phy/" | append: component.path | append:"/README.html" | prepend: site.baseurl | prepend: site.url }}">{{ component.vendor }}: {{ component.productname }}</a></dt><dd>{{ component.description }}<br />Source: <a href="{{ component.source }}">{{ component.source }}</a><br />Platform: {{ component.platform }}</dd>
  {% endif %}
  {% endfor %}
</dl>
