---
layout: post
title: Automated Analysis of a YouTube Channel
component: 
date:   2022-01-01 00:00:00 +0100
abstract: ""
youtubeId: Frg5-22oChs
---

* TOC
{:toc}

Automated Analysis of a YouTube Channel https://www.youtube.com/c/andersjensenorg 

Importance of Audio as a success factor
Analysis of channel https://www.youtube.com/c/andersjensenorg 
Remedies
Recommended Reading/Watching

# Preface

Join Anders Jensen and me on a live session where

- we are going to wrap up first improvements for his video channel and his teaching business
- I share the condensed learning of my past 2 years
- and paint a roadmap for future improvements.

Participants will

- be able to derive actionable ideas from this journey for their own improvements
- distinguish elements of good audio to apply to their own online presence
- rank these by difficulty and affordability
- recognize basic terms and concepts of audio engineering

## Goals

- name the YouTube stats for nerds information relating to audio
- predict the YouTube processing ahead of an upload
- differentiate analog from digital components in a recording chain
- rank factors of audio by importance
- Execute a zielführend workflow/timeline of production and post-production

{% include youtubePlayer.html id=page.youtubeId %}

# Preparation

{% include checklist.html checklistnames="Dress Rehearsal Zoom Interview - Participant,Dress Rehearsal Zoom Interview - Host" heading="h2" %}

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




# Analysis of the YouTube channel

## YouTube recommendations

![foo](/tec/phy/YouTube/images/recommended-upload-encoding-settings.png){:class="resize"}

https://support.google.com/youtube/answer/1722171



# Remedies

## room sound

- ~audio mixing~
- ~high fidelity listening~
- voice acting / voice over recording

Sound

- direct
- reflected

![diffusion](/tec/log/audio/images/diffusion.png){:class="resize"}


{% include youtubePlayer.html id="JPYt10zrclQ" %}

treatments

- acoustic foam
- furniture
- curtains
- rug
- bookshelves
- acoustic panels
- acoustic bass traps
- sound diffusors

btw, there's a ceiling, too!

who to listen to?

- voiceover artists
- church technicians
- your ear

### clap test

>Reverberation is one of the most significant acoustic properties of a room. Knowing the reverberation time is essential in characterizing rooms, be they performance spaces, ordinary rooms or open office spaces.
>
>While the requirements for measuring reverberation are described in detail in the ISO 3382 and ASTM E2235 standards.
https://www.nti-audio.com/en/applications/room-building-acoustics/reverberation-time

>What is Reverberation Time?
>
>Sound produced in a room will repeatedly bounce off reflective surfaces such as the floor, walls, ceiling, windows or tables while gradually losing energy. When these reflections mix with each other, the phenomena known as reverberation is created. Reverberation is thus a collection of many reflections of sound.
>
>Reverberation time is a measure of the time required for reflecting sound to "fade away" in an enclosed area after the source of the sound has stopped. It is important in defining how a room will respond to acoustic sound.
>
>Get a feeling for reverberation times in various rooms, just by clapping your hands.
https://www.nti-audio.com/en/applications/room-building-acoustics/reverberation-time

>How is Reverberation Time defined?
>
>The reverberation time measurement is defined in the ISO 3382-1 standard for performance spaces, the ISO 3382-2 standard for ordinary rooms, and the ASTM E2235 standard.
>
>The reverberation time is the time the sound pressure level takes to decrease by 60 dB, after a sound source is abruptly switched off. Commonly-used abbreviation for reverberation time are T or RT60.
>
>Reverberation Time values vary in different positions within a room. Therefore, an average reading is most often taken across the space being measured.
https://www.nti-audio.com/en/applications/room-building-acoustics/reverberation-time


## Audio Settings on Windows

{% include checklist.html checklistnames="Audio Recording Inventory on Windows" heading="h3" %}

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

# backup


## How to setup a second computer to join meetings and evaluate loudness

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



# Skills and Workflows



## EQ

start with microphjone frequency response chart

Types of EQ

- Graphic EQ
- Parametric EQ

Parametric EQ

Use studio headphones

- Low-pass: Removes all frequencies above a set frequency
- High-pass: Removes all frequencies below a set frequency
- Low-shelf: Attenuates all frequencies below a set frequency
- High-shelf: Attenuates all frequencies above a set frequency
- Peak: Increase frequencies at a set frequency
- Notch: Decrease frequencies at a set frequency


> Remember to use a narrow Q factor when you’re cutting frequencies and use > a wide Q factor when boosting. But rules can be broken, just as long as > it sounds good.
> https://talkinmusic.com/how-to-eq-vocals/

no recipes, rather stretegies

> The most obvious approach to EQ is push up more of what you want to hear. Getting the right microphone for the voice and recording it well should mean little or no EQ is needed.
>…
>If the performer was sticky and click-y, you’ll be hard pressed to boost in the 2-5 kHz range and not bring out mouth noise in the process. In my experience EQ isn’t going to help you get rid of mouth noise, but it can definitely make it worse.
> https://theproaudiofiles.com/voice-processing-eq-cuts-boosts/

> 1. what happened before? (mic frequency response)
> 1. Roll off the low-end starting around 90 Hz.
> 1. Reduce the mud around 250 Hz.
> 1. Add a high shelf around 9 kHz & a high roll off around 18 kHz.
> 1. Add a presence boost around 5 kHz.
> 1. Boost the core around 1 kHz to 2 kHz.
> 1. Reduce sibilance around 5 kHz to 8 kHz.
> 
> https://ledgernote.com/columns/mixing-mastering/how-to-eq-vocals/

EQ in the postprocesing workflow

- EQ cuts
- compression
- EQ boosts


> Roll off the low frequencies if the proximity effect is causing unusual > bassiness.
> Don’t roll off so much low end as the voice loses some of its umph.  Yes, > I’m using “umph” as a technical word.
> Boost in the 1KHz to 5KHz range for improving intelligibility and clarity.
> Boost in the 3Khz to 6Khz range to add brightness.  This can help with > speakers with poor intonation.
> Boost in the 4.5Khz to 6Khz range to add presence.  Note that too much > boosting in this area can produce a thin lifeless sound.
> Boost in the 100Hz to 250Hz for a boomy effect
> In case your head is about to explode from an information overload, remember these key points;
> The above points can contradict each other.  There is no hard and fast rule.  Mixing is as much an art as a science.  Trust your ears over everything else.
> It’s possible that once you EQ the vocal channel that it’s a little lacking in the low end.  Boost it a bit give it that full sound.  Again, trust your ears.  Close your eyes and ask yourself if it a) sounds natural and b) sounds clear.
> https://www.behindthemixer.com/how-eq-speech-maximum-intelligibility/



# knowledge, facts, data

## Audio Signal Levels

A microphone is an electrical device that converts the vibrations into electrical energy. The result is an induced voltage of around 2 mV (millivolt).

line level: (adequate for sending from one device to another)

![foo](/tec/log/audio/images/levels.png){:class="resize"}


## The Audio Frequency Spectrum

logarithmic scale

20-20k Hz hearing "but…"
200 - 6000 male voice
400 - 8000 Hz female voice

> while human hearing spans ten octaves, human speech only covers about five octaves.
> source: https://larryjordan.com/articles/eq-warm-a-voice-and-improve-diction/

ranges

> Our speaking voice has three frequency ranges that need to be understood;
> 1. Fundamentals.  The fundamental frequencies of speech occur roughly between 85Hz and 250Hz.
> 1. Vowels.  Vowels sounds contain the maximum energy and power of the voice, occurring between 350Hz and 2KHz.
> 1. Consonants.  Consonants occur between 1.5KHz and 4KHz.  They contain little energy but are essential to intelligibility.
> https://www.behindthemixer.com/how-eq-speech-maximum-intelligibility/

> - Low-End Noise - 20 Hz to 80 Hz
> - Boominess - 80 Hz to 300 Hz
> - Muddiness - 250 Hz to 500 Hz
> - Nasal Honk - 800 Hz to 1.5 kHz
> - Presence - 4.5 kHz to 9 kHz
> - Breathiness - 10 kHz to 15 kHz
> https://ledgernote.com/columns/mixing-mastering/how-to-eq-vocals/

## Loudness

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

## Reading Mcrophone Datasheets

A less readable part of datasheets of microphones might be the graphs about polar patterns and frequency responses.

### Polar Patterns

The polar pattern depicts the sencsitivity to sounds arriving from different angles. A polar graph uses angles as reference szstem, different from the more ubiquitous cartesian graphs with their x, z and mazbe z axis.
The practitioner can read from a microphone's polar pattern graph how to best position the micriphone so that it does not pick up for example typing noise from the keyboard. 

![microphone polar patterns](/tec/log/audio/images/microphone-polar-patterns.png){:class="resize"}

### Frequency Responses

With the microphone at the very beginning of a recording signal chain it is highly advisable before doing any later EQ "equalisation" changes to the frequency spectrum to study what the microphone did apply to the frequencies at the very beginning. If the practitioner knows that the microphone has what is commonly referred to as presence boost in the (roughly) 3 kHz to 6 kHz range: Then there will hardly be any need to further boost that range in post production.

The polar patterns also show in raw data what otherwise might get marketing terms applied to, like "Exciter" oder "ContourFX".

![microphone polar patterns](/tec/log/audio/images/microphone-datasheets-frequency-responses.png){:class="resize"}

# Skills, Workflows

## GUI Elements for ampli...

## Types of Audio Editing

7 types https://audioaural.com/what-are-the-7-types-of-audio-editing-techniques/

- amplification: increase the volume
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

## Equalisation: Changes to the Frequency Spectrum

- lowpass
- highpass
- bell boost
- ...

Sibilance

## Electric Signals, Noise, Discretization

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

# Off-The-Shelf Technology

## Audio Signal Chain


- hardware
- cable types
- level types
  - speaker
  - line
  - instrument
  - microphone


## Audio Cables and Plugs


![foo](/tec/log/audio/images/cables_audio_35-RCA-XLR.jpg){:class="resize"}

![foo](/tec/log/audio/images/AudioInterfaceNeutrikJacksXLR63.jpg){:class="resize"}



## Youlean Loudness Meter

## OBS Multi-Track Recording



# Applications

## Makefile for youtube-dl


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

## Audacity and Room Reverb

## UiPath Process for YLM Automation

## DaVinci Resolve Fairlight Audio Page

{% include youtubePlayer.html id="Rp-6F8SWFSY" %}
