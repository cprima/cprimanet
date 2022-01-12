---
layout: post
title: Automated Analysis of a YouTube Channel
component: 
date:   2022-01-01 00:00:00 +0100
abstract: ""
youtubeId: jKJqcME6dPk
---

Automated Analysis of a YouTube Channel https://www.youtube.com/c/andersjensenorg 

Importance of Audio as a success factor
Analysis of channel https://www.youtube.com/c/andersjensenorg 
Remedies
Recommended Reading/Watching

# preface

## Goals

- name the YouTube stats for nerds information relating to audio
- predict the YouTube processing ahead of an upload
- differentiate analog from digital components in a recording chain
- rank factors of audio by importance
- Execute a zielführend workflow/timeline of production and post-production


# How it started

![Picture description](/biz/consulting/images/LinkedInAndersJensenAskingSoundEngineer.png){:class="resize"}

## Step 1: Reading the incident report

- volume is being turned up
- the room has qualities attributed to it
- off-the-shelf technology is mentioned
- audio-quality is described as having white noise

## verfifying the incident report

- room is quiet, but has reverb
- white noise is a good general description but the correct term
- the audio signal chain is only parially described

## ticket triage

- more information is needed,
- contact reporter

## Recap

### signal chain

- hardware
- cable types
- level types
  - speaker
  - line
  - instrument
  - microphone

#### levels

A microphone is an electrical device that converts the vibrations into electrical energy. The result is an induced voltage of around 2 mV (millivolt).

line level: (adequate for sending from one device to another)

![foo](/tec/log/audio/images/levels.png){:class="resize"}


#### cables

![foo](/tec/log/audio/images/cables_audio_35-RCA-XLR.jpg){:class="resize"}

![foo](/tec/log/audio/images/AudioInterfaceNeutrikJacksXLR63.jpg){:class="resize"}


### audio editing

7 types https://audioaural.com/what-are-the-7-types-of-audio-editing-techniques/

- amplification: increase the volumen
- compression: change the dynamics
- limiting: limit sound above a certain level
- panning: move the sound in and between left and right stereo channel
- equalization: changes to the frequency spectrum; low-cut, high-cut, bell boost
- normalization: //fixme
- stereo imaging: "from mono to stereo" //fixme


Compressors and Limiters reduce Dynamic Range, while Expander and Gates increase it

https://ask.audio/articles/mixing-concepts-what-is-dynamics-why-you-should-care

- noise gate
- expander

# Analysis of the YouTube channel

## YouTube recommendations

![foo](/tec/phy/YouTube/images/recommended-upload-encoding-settings.png){:class="resize"}

https://support.google.com/youtube/answer/1722171

## dl

```bash
YTCHANNELBASEURL=https://www.youtube.com/channel/
YTCHANNELID=UCPdtz4gd_iYebJFYq9N8pWA
BATCH_FILE=urls.txt
ARCHIVE_FILE=archive.txt
SLEEP_REQUESTS=8
MIN_SLEEP_INTERVAL=8
MAX_SLEEP_INTERVAL=128
SUBTILES_LANG=en
LIMIT_RATE=5M
TROTTLED_RATE=50K

.PHONY: list_channel_videos
list_channel_videos:
        @echo "# pipe the output to e.g. >> $(BATCH_FILE)"
        @yt-dlp --get-filename --no-warnings --quiet \
        --output "https://www.youtube.com/watch?v=%(id)s" \
        $(addprefix $(YTCHANNELBASEURL),$(YTCHANNELID))

.PHONY: list_channel_videos2
list_channel_videos2:
        @echo "# pipe the output to e.g. >> $(BATCH_FILE)"
        @yt-dlp --get-filename --no-warnings --quiet \
        --output "%(id)s,%(upload_date)s_%(acodec)s_%(asr)s_%(title)s.%(ext)s,%(id)s" \
        $(addprefix $(YTCHANNELBASEURL),$(YTCHANNELID))

.PHONY: download_videos
download_videos:
        yt-dlp --limit-rate $(LIMIT_RATE) --throttled-rate $(TROTTLED_RATE) \
        --min-sleep-interval $(MIN_SLEEP_INTERVAL) \
        --max-sleep-interval $(MAX_SLEEP_INTERVAL) \
        --sleep-requests $(SLEEP_REQUESTS) \
        --continue --ignore-errors --no-overwrites \
        --output "%(upload_date)s_%(acodec)s_%(asr)s_%(title)s.%(ext)s" \
        --batch-file $(BATCH_FILE) --download-archive $(ARCHIVE_FILE) \
        --write-url-link --write-info-json --write-description --write-info-json \
        --write-thumbnail --write-auto-subs --sub-lang $(SUBTILES_LANG)
```

# Remedies

## room sound

### clap test


## Loudness GUI

Controlling the loudness during the duration of a recording is a standard workflow in videoproduction.

Here a overview of commonly implemented GUI graphical user interface functionality is shown.

This video shows the software Davinci Resolve.

This video shows the software Audacity.

To make a future edit as easy as possible it is a good idea to work on a copy of the audio track.

There is a handle to change the level of a single clip with the mouse.

The whole track also has a level, here adjustable by a slider and direct entry.

A double click resets the setting.

The beginning of the clip may get a Fade-In.
And the end of the clip may get a Fade-Out.

But now the most important part:

Along the timeline at desired positions "keyframes" are inserted.

Each keyframe may get an individual level,

- either by dragging it with the mouse,
- or by a slider,
- or direct entry.

In between the keyframes the software calculates the intermediate value, by default with a linear algorithm.

Every program with more than just a basic feature set will also offer an ease-in and/or ease-out influce for finer control of an otherwise abrupt new state.
This software implements this feature with Bezier curve handles.
Although for audio projects this particular control it is less important than in -- for example animation.


Recommended Reading/Watching


## Hardware knowhow

reading datasheets

## skills


# backup

## analog audio *shudder*?



Why is the microphone such a strange thing for us IT guys?

As programmers, IT technicians or system administrators we are used to highly complex systems, comprised of hardware, operating system, programming languages with their respective runtimes or interpreters, peripheral devices and software.

These machines are based on basic physical laws, electrons and their digitization.

![foo](/tec/log/ElectricalEngineering/images/MIT_CircuitsElectronics_Lec1_outline.svg){:class="resize"}


To illustrate the various disciplines in physics, electrical engineering and computer sciende let's have a look at the blackboard in the lecture "Circuits and Electronics" by Professor Anant Agarwal at the Massachusets Institure of Technology: About half a dozen disciplines fill his blackboard, and on the left we are dealing with simple electronic circuits and their behaviour that can be expressed in Volt, Ampere and Ohm.


![foo](/tec/log/ElectricalEngineering/images/ElectricalWireNoise.svg){:class="resize"}

Here is a visualization of the effect of noise when transmitting a combination of two signals.

Coming from the high-level digital world on the right side of the blackboard we IT people can dive into the analog world for example when experimenting with an Arduino or the GPIO pins of a Raspberry Pi.

![foo](/tec/log/ElectricalEngineering/images/ElectricalDiscretization.svg){:class="resize"}

Looking at the example again we see that just to determine if such a signal expresses a binary "on" or "off" poses a challenge -- as everybody knows who tried to implement a bare-bones shutdown-button for the Raspberry Pi.

This is pretty for from the usual "Hello World!" example in our favorite programming languages!

Now I am coming back full circle:

The microphone is such a basic electrical device, producing electrical signals measured in 1/1000 of a Volt.

![foo](/tec/log/audio/images/levels.png){:class="resize"}

Here is a chart of the signals strengths with the equivalents of Volt and Decibels referenced in Voltage. (Yes, there is a straightforward conversion!)
The microphone "transduces" a pretty low signal! One millivolt plus minus a half!

![foo](/tec/log/ElectricalEngineering/images/MIT_CircuitsElectronics_Lec1_outline.svg){:class="resize"}

And on the way to our software on the operating system of our choice we need to traverse the whole blackboard of Professor Agarwal!

![foo](/tec/log/ElectricalEngineering/images/ElectricalWireNoiseAudiolike.svg){:class="resize"}

And on the way we inevitably are dealing with the same problems as before, noise and / or the need to digitize the signal (not only into binary 1 or zero but commonly into 16 bit, er even 24 or 32 bit).

All this is just my long-winded approach to re-state best practices in dealing with audio recordings from a microphone:

![foo](/tec/log/audio/images/audio-signal-chain.svg){:class="resize"}

Produce the cleanest possible signal, raise it as quickly to line level, and use hardware dedicated to high quality conversion from the analog world to the digital world.

Next time you are using a microphone, remember the picture of noise sitting on top of a signal, and remeber the blackboard of Professor Agarwal!


//todo: incorporate analog playout
//analog reconstruction of two consecutive digital samples peaking at 0 dBFS may result in an analog wave that peaks higher than either of the samples
//https://www.mixinglessons.com/dbtp-decibel-true-peak/


## Loudness and YouTube

intro: loud commercials

goal: relevance for YouTuber and what are the key concepts behind it

//caveat: peak audio AND loudness

toc

- what is loudness, what is loud
  - perception
  - (Fletcher Munson Curve)
  - we hear the mids more prominently than bass and highs
- excursion: music production, TV
- European Broadcast Union (EBU) OR EU, consumer protection, 2010
  - now https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-4-201510-I!!PDF-E.pdf
  - also: playlist shuffle
  - example overcompressed track https://magroove-files.s3.amazonaws.com/magroove-blog/wp-content/uploads/2019/08/Nivel-em-LUFS-de-diferentes-faixas-de-%C3%A1udio-768x480.jpg
- peak, RMS, LUFS, …
  - negative numbers because referenced to full scale of the maximum that a system can handle
  - RMS is not adjusted to human hearing
  - LUFS k-weight https://youlean-129cf.kxcdn.com/wp-content/uploads/2020/05/Screen-Shot-2020-05-03-at-7.06.08-PM-3.png https://youlean.co/how-to-hack-lufs-normalization/
  - high LUFS "means compression" == loss of dynamic range
- statistics over time
  - short-term
  - integrated
- true peak


- production loudness
- distribution loudness

To remain on the practical side of things:
- example LUFS graph over time
- YouTube rules, and other platforms

- YouTube rules -> YLM features

- resulting action / Applying This Knowledge
  - separate master mixes for each platform
  - or rely on "them" to turn it down
  - measure after the adjustments! 


Youlean Loudness Meter 2 (Free and Pro)
Mastering The Mix LEVELS (Paid)
iZotope Insight 2 (Paid)
Waves WLM Plus Loudness Meter (Paid)


## How to setup a second computer to join meetings for loudness evaluation

On a PC:

1. install Sizer
1. install OBS
1. install Virtual Audio Cable
1. install Youlean Loudness Meter 2
1. install Zoom/MS Teams/Skype

Configure Virtual Audio Cable

- Sound > Recording > Cable > Properties > Levels: Output = 100
- Sound > Recording > Cable > Properties > Advanced: Default Format = 1 channel 16bit 48000 Hz

Configure YLM

- File > Preferences: Driver Type = Direct Sound
- File > Preferences: Input Device = Cable Output
- File > Preferences > Meter Input Channel Settings: L = Cable L, R = Cable R
- View Menu > Graphics: GUI Scaling = 100%
- right-click YLM window at lower right corner > 16:9 > 1280x720
- Channel Configuration: Mono
- Enable short term loudness graph
- Enable true peak clipping indication

Configure OBS

- Settings > Video: Base (Canvas) Resolution = 1280x720
- Settings > Video: Output (Scaled) Resolution = 1280x720
- Sources > Add > Window Capture: Window = [Youlean Loudness Meter 2.exe]
- Start Virtual Camera

Configure Zoom

- Settings > Audio: Microphone = Cable
- Settings > Audio > Microphone: Volume = 100%

Join Zoom Meeting

- Start Video