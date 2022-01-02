---
layout: page
title:  "Applications ... by cprima.net"
permalink: /app/index.html
categories: [ app ]
---

## Physical application components

> An encapsulation of application functionality aligned to implementation structure, which is modular and replaceable. It encapsulates its behavior and data, provides services, and makes them available through interfaces.
> https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap03.html#tag_03_04


<dl>
  {% for component in site.data.acpac %}
  {% if component.visibility == 'public'  %}
      <dt><a href="{{ "/" | append: component.path | append:"/README.html" | prepend: site.baseurl | prepend: site.url }}">{{ component.owner }}: {{ component.name }}</a></dt><dd>{{ component.description }}<br />Status: {{ component.lifecycle_status }}</dd>
  {% endif %}
  {% endfor %}
</dl>
