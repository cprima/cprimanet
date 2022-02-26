---
layout: presentation_v1.0.3
title: "Sample Presentation"
excerpt: "excerpt"
author: "Christian Prior-Mamulyan"
dummycontent: false
theme: solarized
---



<section data-background-image="/biz/marketing/visualidentity/template_svg_1080p.png">
  <h2>Background Image</h2>
  <p>foo</p>
</section>

<section data-background-image="/biz/marketing/visualidentity/template_svg_1080p.png">
<h2>r-stack fragments</h2>
<div class="r-stack">
  <img class="" src="/tec/log/audio/images/compressor_uncompressed.png" width="1280" height="540">
  <img class="fragment" src="/tec/log/audio/images/compressor_1to2.png" width="1280" height="540">
  <img class="fragment" src="/tec/log/audio/images/compressor_1to4.png" width="1280" height="540">
  <img class="fragment" src="/tec/log/audio/images/compressor_1to10.png" width="1280" height="540">
  <img class="fragment" src="/tec/log/audio/images/compressor_makeupgain.png" width="1280" height="540">
  <img class="fragment" src="/tec/log/audio/images/compressor_uncompressed.png" width="1280" height="540">
</div>
</section>

<section>
<section data-auto-animate data-background-image="/biz/marketing/visualidentity/template_svg_1080p.png">
  <h1>Auto-Animate</h1>
</section>
<section data-auto-animate>
  <h1 style="color: red;">Auto-Animate</h1>
</section>

<section data-auto-animate data-background-image="/biz/marketing/visualidentity/template_svg_1080p.png">
  <h1>Implicit Animation</h1>
</section>
<section data-auto-animate>
  <h1>Implicit Animation</h1>
  <h1>Animation</h1>
</section>

<section data-auto-animate>
  <h1>Animation</h1>
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <h1>Animation</h1>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>

<section data-auto-animate>
  <h1>Animation</h1>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
    ]
  </code></pre>
</section>
<section data-auto-animate>
  <h1>Animation</h1>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
      { name: 'earth', diameter: 12742 },
      { name: 'jupiter', diameter: 139820 }
    ]
  </code></pre>
</section>
<section data-auto-animate>
  <h1>Animation</h1>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let circumferenceReducer = ( c, planet ) => {
      return c + planet.diameter * Math.PI;
    }

    let planets = [
      { name: 'mars', diameter: 6779 },
      { name: 'earth', diameter: 12742 },
      { name: 'jupiter', diameter: 139820 }
    ]

    let c = planets.reduce( circumferenceReducer, 0 )
  </code></pre>
</section>

</section>

<section tagcloud data-state="" data-domain="application">
<h2>Typical Scope of Solutions</h2>
    <span tagcloud-color="#859900" tagcloud-link="#" tagcloud-weight="100">[Remote Execution] </span>
    <span tagcloud-color="#aac300" tagcloud-link="#" tagcloud-weight="50">Software Installation </span>
    <span tagcloud-color="#859900" tagcloud-link="#" tagcloud-weight="80">Targeting </span>
    <span tagcloud-color="#b58900" tagcloud-link="#" tagcloud-weight="100">[Cfg Mgt] </span>
    <span tagcloud-color="#dfa900" tagcloud-link="#" tagcloud-weight="50">Defined State </span>
    <span tagcloud-color="#604900" tagcloud-link="#" tagcloud-weight="70">Idempotence </span>
    <span tagcloud-color="#604900" tagcloud-link="#" tagcloud-weight="60">File Management </span>
    <span tagcloud-color="#dfa900" tagcloud-link="#" tagcloud-weight="40">Confidential Data </span>
    <span tagcloud-color="#dc322f" tagcloud-link="#" tagcloud-weight="100">[Event-Driven Infrastructure] </span>
    <span tagcloud-color="#b12826" tagcloud-link="#" tagcloud-weight="40">Presence of Remote Systems </span>
    <span tagcloud-color="#871f1d" tagcloud-link="#" tagcloud-weight="60">React to Monitored State Changes </span>
    <span tagcloud-color="#268bd2" tagcloud-link="#" tagcloud-weight="100">[Documentation] </span>
    <span tagcloud-color="#268bd2" tagcloud-link="#" tagcloud-weight="50">Auditing </span>
</section>


<section>
    <section id="fragments">
        <h2>Fragments</h2>
        <p>Hit the next arrow...</p>
        <p class="fragment">... to step through ...</p>
        <p><span class="fragment">... a</span> <span class="fragment">fragmented</span> <span class="fragment">slide.</span></p>
    </section>
    <section>
        <h2>Fragment Styles</h2>
        <p>There's different types of fragments, like:</p>
        <p class="fragment grow">grow</p>
        <p class="fragment shrink">shrink</p>
        <p class="fragment fade-out">fade-out</p>
        <p>
            <span style="display: inline-block;" class="fragment fade-right">fade-right, </span>
            <span style="display: inline-block;" class="fragment fade-up">up, </span>
            <span style="display: inline-block;" class="fragment fade-down">down, </span>
            <span style="display: inline-block;" class="fragment fade-left">left</span>
        </p>
        <p class="fragment fade-in-then-out">fade-in-then-out</p>
        <p class="fragment fade-in-then-semi-out">fade-in-then-semi-out</p>
        <p>Highlight <span class="fragment highlight-red">red</span> <span class="fragment highlight-blue">blue</span> <span class="fragment highlight-green">green</span></p>
    </section>
</section>

<section data-autoslide="2000">
<h2>autoslide</h2>
  <p>After 2 seconds the first fragment will be shown.</p>
  <p class="fragment" data-autoslide="2000">After 2 seconds the first fragment will be shown.</p>
  <p class="fragment" data-autoslide="10000">After 10 seconds the next fragment will be shown.</p>
  <p class="fragment">Now, the fragment is displayed for 2 seconds before the next slide is shown.</p>
</section>





<script>
  function ready() {
    Reveal.configure({ controls: false });
    Reveal.configure({ progress: false });
    Reveal.configure({ center: false });
  }

  document.addEventListener("DOMContentLoaded", ready);
</script>