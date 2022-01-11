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
- differentiate analog from digital …
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

