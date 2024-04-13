---
layout: post
title: "Tabbed Inline interface"
component:
date: 2023-10-15 00:00:00 +0100
abstract: ""
---

Lorem ipsum...

{% include tabbed-inline-interface.html id="example1" tabs="PHP,Python,Java" syntaxes="php,python,java" %}

More text...

<p>Mauris sed tortor sed odio fermentum auctor. Suspendisse potenti. Donec eget quam eu ex facilisis facilisis.</p>

<script>
    function showContent(id) {
        const group = id.split('-')[0];
        const contents = document.querySelectorAll(`pre[id^="${group}"]`);
        const buttons = document.querySelectorAll(`div[onclick^="showContent('${group}"]`);
        
        contents.forEach(content => content.classList.remove('active-content'));
        buttons.forEach(button => button.classList.remove('active-tab'));
        
        document.getElementById(id).classList.add('active-content');
        buttons.forEach(button => {
            if (button.getAttribute('onclick').includes(id)) {
                button.classList.add('active-tab');
            }
        });
    }
</script>
