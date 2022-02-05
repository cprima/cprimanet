---
layout: post
title: How to acoustically treat the homeoffice
date:   2022-01-31 00:00:00 +0100
abstract: "Ideas to acoustically treat the homeoffice for voice recording"
---


## Preface

Priorities for livestreaming -- and online workshop are live streaming by nature:

![priorities internet audio lighting cameras background](/tec/log/images/priorities_inetnet-audio-lighting-cameras-background.png)

1. internet connection
1. audio
1. lighting
1. camera
1. background

Regarding "audio": Setup for voice recording! Bear the conflict of interest with the desire for a "polished studio thumbnail picture".

Do:

- setup for tireless hourlong experience by participants/viewers
- consciously educate yourself in production technology over the months
- prepare for success: Plan to pay a video editor. Reduce his efforts by delivering good-quality raw material

Don't:

- setup for music production / mastering
- setup for HiFi listening experince
- setup for aestetics only

Good sound is created at the time of recording.
Don't leave issues for fixing in post-production!

In case that _good room acoustics_ clash with _aesthetics_ consider two setups: Record e.g. the intro with nice aesthetics, and afterwards the content/workshop/live-streaming part with added room treatment.

>excursion 
>
>The human voice as instrument/music/arrangement/sound/…

## Evaluate the As-Is Situation

1. what is the room echo like?
2. is there unwanted noise?
3. (do I have noisy equipment?)

Take inventory of the room:

- hard surfaces bad, fluffy surfaces good
- take dimensions of corners, edges and walls/ceiling/floor
- …

Collect material that might be available in the household/workshop already.

- fixtures
- blankets / cushions
- clamps
- hooks

### Room echo and the clap test

To evaluate the room echo the clap-test is a reproducible method to _measure_ the situation as-is -- and after some modifications.

How to perform a clap test?

- record a short clap (by hands, or with a movie clapboard)
- evaluate the waveform: How many milliseconds until the loudness is "completely silent"?

This can be done e.g. with Audacity.

![audacity waveform clap test](/tec/log/audio/images/waveforms.png)

On Android there is also the app "myRaumklang", available via GooglePlay at [https://play.google.com/store/apps/details?id=de.myraumklang.myraumklang](https://play.google.com/store/apps/details?id=de.myraumklang.myraumklang)

### Listen back to the recording

Listen back with (good) closed headphones!

- beyerdynamic DT-770 PRO/80 Ohm https://www.thomann.de/de/beyerdynamic_dt770_pro80_ohm.htm
- Audio-Technica ATH-M50 X https://www.thomann.de/de/audio_technica_ath_m50_x.htm

### Noisy equipment

Better shut off that extra computer and mute the smartphone!

## Room Setup

Behind the mic and behind yourself is important. Optimizing for _voice recording_, not for listening back!

Affordable and maybe even already available items to influence the room are:

- moving blankets ftw [https://www.amazon.de/gp/product/B0844W5BSY/](https://www.amazon.de/gp/product/B0844W5BSY/)
- curtains, blankets
- sofa and sofa cushions
- (corners and edges)

Dampening textile materials will go a long way: I found that a sofa, thicker and thinner curtains and upon request a moving blanket on the wall behind the microphone do work well -- although the rest of the room has quite hard wooden surfaces.

![3D screenshot of room](/tec/log/audio/images/WOB38A8-audio.png)

The picture above shows brownish curtains, a dark moving blanket and the blueish sofa. Works for me! If the room was larger I would use a fluffy carpet.

The dampening material needs to be placed according to the polar pattern of the microphone.

>excursion: example of closet-recording
>
>"So my thought process is to get as much absorbant material…"
>
>Booth Junkie
>https://youtu.be/5Se381sERrY?t=149

### Reduce unwanted noise

- keyboard
- fans
- …

I found the Logitech K780 a quiet silent keyboard, and ditched my beloved "DasKeyboard"s for it full-time: [https://www.amazon.de/gp/product/B01GV6HP0E](https://www.amazon.de/gp/product/B01GV6HP0E)

A good protective case is [https://www.amazon.de/gp/product/B07PJHLY7R/](https://www.amazon.de/gp/product/B07PJHLY7R/).


>excursion: microphone patterns
>
>![da](/tec/log/audio/images/microphone-polar-patterns.png)

## Audio Slang for the Processing Chain

- speaker level
- line level (adequate for sending from one device to another)
- instrument level
- microphone level

"line level", if not then quickly up to line level. And check all gear in the audio chain for correct configuration.

Fixing something with the below already counts as "fixing in post". Room acoustics should be setup withput the help of any (build-in) effect, filters, processors or adjustments.

- loudness
- noise
- compressor limiter, EQ, gate

![BlackmagicAtemSoftwareControlAudioDynamics](/tec/log/audio/images/BlackmagicAtemSoftwareControlAudioDynamics.png)

excursion: dynamic range

## Evaluate the result

YouTube stats for nerds

![YouTube-stats-for-nerds_cprima-dpdhl](/tec/log/audio/images/YouTube-stats-for-nerds_cprima-dpdhl.png)

In the screenshot the content loudness a bit too silent, -12dB below YouTube's reference scale. And 12dB is a lot! YouTube will not automatically raise the audio level. But it will make loud videos quieter, which might result in noticeable quality loss.

![YouleanLoudnessMeter_cprima-dpdhl](/tec/log/audio/images/YouleanLoudnessMeter_cprima-dpdhl.png)

Same audio track, now in Youlean Loudness Meter 2. Typically between -23dB and -17dB should be aimed for.

![Audacity-ACX-Checks_cprima-dpdhl](/tec/log/audio/images/Audacity-ACX-Checks_cprima-dpdhl.png)

Same audio track, analyzed in Audacity with ACX-Checks. Linked to from [[Audacity Forum](https://wiki.audacityteam.org/wiki/Audiobook_Mastering)](https://wiki.audacityteam.org/wiki/Audiobook_Mastering).


//How to identify post-prod errors? (clicks, …)


## Reach out to others

Here I got schooled and I loved the result:
https://forum.audacityteam.org/viewtopic.php?f=63&t=116034

>I have two favorite bad examples. Early on, someone went to great pains to build a simulation of a television news set. It was impressive with colors, angles, and lighting just right. The effect carried right up to the first time somebody said something. Instant kids recording in the bathroom.
>
>kozikowski

https://www.kozco.com/tech/audacity/TestClip/Record_A_Clip.html