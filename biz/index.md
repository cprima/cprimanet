---
layout: page
title:  "Biz ... by cprima.net"
permalink: /biz/index.html
categories: [ biz ]
---

## Business

> how things are produced
>
> health-realted sport aspects


<dl>
  {% for component in site.data.bapro %}
  {% if component.visibility == 'public'  %}
      <dt><a href="{{ "/" | append: component.path | append:"/README.html" | prepend: site.baseurl | prepend: site.url }}">{{ component.owner }}: {{ component.name }}</a></dt><dd>{{ component.description }}</dd>
  {% endif %}
  {% endfor %}
</dl>
