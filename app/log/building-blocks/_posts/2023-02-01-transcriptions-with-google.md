---
layout: presentation_v1.1.0
title: "Audio Transcriptions with Google"
categories: [ application_logical_building-blocks ]
date:   2023-02-01 00:00:00 +0100
abstract: lorem ipsum
excerpt: Record ideas on the move, preprocess at home, generate transcript in the cloud
_titleimagefull: /app/log/building-blocks/images/transcriptions-with-google/audacity_inputfiles-combined-normalized-silenceremoved_1080p.png
---

<!-- template                                   -->

<section>

<!--
<section>
<h2>foo bar baz</h2>
<div class="container">
<div class="col">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
<div class="col">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>

</div>
</section>
//-->

<section style="text-align: center;" >
<h2 style="">Make a bunch of audio recordings</h2>

<img  class="r-stretch" src="{{ "/app/log/building-blocks/images/transcriptions-with-google/file-explorer-view_with-sample-wav-files.png" | prepend: site.baseurl }}" alt="boards" />


</section>

<section style="text-align: center;" data-background-gradient="radial-gradient(#fdf6e3, #eee8d5)">
<h2>Write a bash script (in WSL)</h2>
<img  class="r-stretch" src="{{ "/app/log/building-blocks/images/transcriptions-with-google/bash-script-as-Makefile.png" | prepend: site.baseurl }}" alt="boards" />
</section>

<section style="text-align: center;" >
<h2>Run the script on *wav files</h2>
<img  class="r-stretch" src="{{ "/app/log/building-blocks/images/transcriptions-with-google/bash-script-output.png" | prepend: site.baseurl }}" alt="boards" />
</section>

<section style="text-align: center;" data-background="/app/log/building-blocks/images/transcriptions-with-google/google-bucket-view.png">
<h2>Upload to a Google bucket</h2>
</section>

<section style="text-align: center;" data-background="/app/log/building-blocks/images/transcriptions-with-google/console-cloud-google-speech-transcriptions-list.png">
<h2>console.cloud.google.com/speech/transcriptions</h2>
</section>

<section style="text-align: center;" data-background="/app/log/building-blocks/images/transcriptions-with-google/console-cloud-google-speech-transcriptions-download.png">
<h2>Download transcription</h2>
</section>


</section>


<section>

<section style="text-align: center;" data-background-gradient="radial-gradient(#fdf6e3, #eee8d5)">
<h2>Improved script with ffmpeg audio filters</h2>
<img  class="r-stretch" src="{{ "/app/log/building-blocks/images/transcriptions-with-google/bash-script-as-Makefile_enhanced_v2.png" | prepend: site.baseurl }}" alt="boards" />
</section>


<section style="text-align: center;" >
<h2>The improved code</h2>
<pre class="bash"><code>
combine-wav-files-to-flac:
        rm -f _combined.flac
        rm mylist.txt
        find . -iname "2*wav" -printf "file %p\n" | sort -n > mylist.txt
        ffmpeg -hide_banner -f concat -safe 0 -i mylist.txt -c:a flac -af "
        silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:
        stop_periods=-1:stop_duration=2:stop_threshold=-40dB,
        loudnorm=i=-14.0" -ar 48000 _combined.flac

</code></pre>

<p>The documentation for the filters can be found at<br />
<a href="https://ffmpeg.org/ffmpeg-filters.html#silenceremove">https://ffmpeg.org/ffmpeg-filters.html#silenceremove</a> and <br />
<a href="https://ffmpeg.org/ffmpeg-filters.html#silenceremove">https://ffmpeg.org/ffmpeg-filters.html#silenceremove</a></p>

<p>ffmpeg allows to filter silent parts based on a bunch of threshold parameters, and also does loudness normalization.</p>

</section>

<section style="text-align: center;" data-background-gradient="radial-gradient(#fdf6e3, #eee8d5)">
<h2>The process steps visualized</h2>
<img  class="r-stretch" src="{{ "/app/log/building-blocks/images/transcriptions-with-google/audacity_inputfiles-combined-normalized-silenceremoved_720p.png" | prepend: site.baseurl }}" alt="" />
</section>



</section>
