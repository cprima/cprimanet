---
layout: post
title: How to setup a second computer to join meetings and evaluate loudness
component: 
date:   2022-02-01 00:00:00 +0100
abstract: ""
---


In an online meeting all participants should have a similar loudness level. The easiest way for everybody to adjust their microphone is if the loudness is measured and visible to all. To achieve this, a special account joins the meeting and instead of a webcam picture transmits a loudness meter.

Prereqisites on a PC:

A good software stack to achieve this is to

1. install Sizer
1. install OBS
1. install VB-Audio's Virtual Audio Cable
1. install Youlean Loudness Meter 2
1. install Zoom/MS Teams/Skype

Next step ist to configure Virtual Audio Cable

Open the Windows Sound Settings, for example by pressing the Windows key together with R and typing control mmsys.cpl sounds and set

- Sound > Recording > Cable > Properties > Levels: Output = 100
- Sound > Recording > Cable > Properties > Advanced: Default Format = 1 channel 16bit 48000 Hz

With that being set it is possible to configure YLM

- File > Preferences: Driver Type = Direct Sound
- File > Preferences: Input Device = Cable Output
- File > Preferences > Meter Input Channel Settings: L = Cable L, R = Cable R
- View Menu > Graphics: GUI Scaling = 100%
- right-click YLM window at lower right corner > 16:9 > 1280x720
- Channel Configuration: Mono
- Enable short term loudness graph
- Enable true peak clipping indication

From this point on YLM will listen to our Virtual Audio Cable and analyze the incoming audio.

Then it is the moment to configure Zoom to listen to this Virtual Audio Cable as its microphone:

- Settings > Audio: Microphone = Cable
- Settings > Audio > Microphone: Volume = 100%

Finally, configure OBS to show the properly sized window of YLM als a webcam:

- Settings > Video: Base (Canvas) Resolution = 1280x720
- Settings > Video: Output (Scaled) Resolution = 1280x720
- Sources > Add > Window Capture: Window = [Youlean Loudness Meter 2.exe]
- Start Virtual Camera

Now this PC is ready to join Zoom Meeting and show a visualization of the loudness of whatever is spoken or played in the meeting!

- Start Video
- Select OBS Virtual Cam
