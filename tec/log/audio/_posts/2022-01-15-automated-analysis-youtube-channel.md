---
layout: post
title: Automated Analysis of a YouTube Channel
component: 
date:   2022-01-01 00:00:00 +0100
abstract: ""
youtubeId: Frg5-22oChs
---

<!--
## Todo
pop filter?
dynamic/condenser/…
What if x/y/z went wrong? -> checklist
plugins, dry/wet
clipping
mic stand
speaking technique
dynamic range
mono/stereo/5.1 surround
original sound

postprocessing workflow:
- what signal chain went in?
- what did go wrong?
  - what is "wrong"?
- what is the target platform?
- cleanup wanted/needed/time available for it?
  - (noise suppression)
  - EQ
  - Compressor
  - Normalization
- listen back
//-->

<!--
https://www.youtube.com/watch?v=Rp-6F8SWFSY
//-->

<!--
## Future Steps for Anders
recording audio tracks separately
loudness in interviews
gate
cleanup plugins for the recue?
//-->

<!--
## Props
gears
breadboard amplifier https://circuitdigest.com/electronic-circuits/lm386-audio-amplifier-circuit
Raspberry Pi on/off-switch
multi-pattern microphone
decibel meter
minimal recommended gear
external recorder


//-->

<!--
YouTube: 1 mono audio channel
Interview: 2 (mix minus) mono

YouTube: hardly multitrack audio

Minimal gear recommendation

//-->

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

## Room Acoustics, Reverberation Time and Clap Test

<audio controls> 
  <source src="/tec/log/audio/assets/RoomAcousticsReverberationTimeAndClapTest.mp3"  type="audio/mpeg">
  <source src="/tec/log/audio/assets/RoomAcousticsReverberationTimeAndClapTest.ogg"  type="audio/ogg">
  <source src="/tec/log/audio/assets/RoomAcousticsReverberationTimeAndClapTest.wav"  type="audio/wav">
  Your browser does not support HTML5 audio.
</audio>


The journey to improve the audio quality of a recorded narration for webinars or in videoconferences does not start with buying equipment. Because equipment is used inside a room and the room is where it starts.

The requirements to record for webinars are very similar to those of the voice actors, or voice over artists. And they are quite different from music producers or audio mixers. And quite different from high fidelity music listeners. So this kind of narrows down from whom to take advice from.
Another good source of advice are audio engineers in churches, by the way. And with a bit of training our own ears are another authoritative judge!


Within the room there will be direct sound and reflected sound from the walls and surfaces. The physical properties of these surfaces make or break a good room acoustic! Only so-called anechoc chambers have no reflected sound and they are not a good thing to strive for, by the way.

The reflected sound will hit our microphone again and decrease the quality of our recording. This reflected sound is THE most important aspect that needs to be controlled. Worst case is to sit between two hard walls which reflect our spoken word multiple times into the microphone until it dies down in volume.

And let's not forget that there is a reflective ceiling, too!

To reduce reflections both absorption and diffusion will improve the room acoustics. Examples for absorptive materials are:

- acoustic foam
- furniture
- curtains
- rugs
- acoustic bass traps
and of course
- sound blankets

Diffusive materials are

- bookshelves
- sound diffusors

A measurable property of the room is its reverberation time, which can be measured in according to ISO standards -- or performed with simple tools which is good enough in our context.

First, what is exactly meant with reverberation time?

Reverberation is the acumulated reflection of sound. It is what we hear in a bathroom.
Reveberation time is the time it needs to fade away.

Most common method is to measure the RT60 which is the time in seconds until a loud sound decays by 60 decibels.

All this is another way of saying: Do a clap test, there is even an app for this!

Either the app or our own recording with our existing microphone into a software that displays a waveform will give us a measurement in seconds.

Then we do a few improvements, and measure again, and listen to our recording again.

In my room I have both hard and absorbant materials. But as the sound of my voice does not bounce back from the hard surfaces into the microphone I have not negative effect by the hard wooden cupboard doors. So a good room for audio recording does not need to be covered in foam all around!

The biggest problem of my room is that the heating pipes transmit sound from the teenagers room underneath. Reverberation time does not fix THAT. Maybe I will give them a gamer's headset next christmas! ;)

Going by an RT60 measurement means that it is easy to find out when to stop improving the room acoustic, and focus on other aspects of good audio in webinars!

### Resources

{% include youtubePlayer.html id="JPYt10zrclQ" %}


https://www.nti-audio.com/en/applications/room-building-acoustics/reverberation-time

http://www.larsondavis.com/learn/building-acoustics/Reverberation-Time-in-Room-Acoustics


### my room

https://imgur.com/a/NHX2XGe

## Audio Settings on Windows

{% include checklist.html checklistnames="Windows 10 Audio Recording Inventory" heading="h3" %}

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


# knowledge, facts, data

## Audio Signal Levels

The term Digital Sound Recording might be misleading from the very beginning: It starts and ends in the Analog Domain of the physical world, digital is only the middle part. Both the microphone and the loudspeaker are analog devices.

The microphone actually produces a continous electrical signal, done by converting vibrations into electrical energy, and a very low signal that is: The result is an induced voltage of a few millivolt -- that is one thousandth of a volt. This microphone level is LOW!

All this gives us a hint that a microphone is best understood with the mindset of an electrical engineer.

![chart of audio signal levels: microphone, line, instrument and speaker](/tec/log/audio/images/levels.png){:class="resize"}

<!--
Mic level signal (low) = 0.0001 V = 0.1 mV = -80dBV

Shure SM11 output is an example.
Mic level signal (average or typical) = 0.001 V = 1 mV = -60 dBV

Shure SM58 output is an example.
Mic level signal (high or "hot") = 0.01 V = 10 mV = -40 dBV

Shure MX418 output is an example.  Also the Shure 588SDX output, set to high impedance, is an example.
Auxiliary level signal (AUX) = 0.1 V = 100 mV = -20 dBV

Shure SCM268 output, RCA jack, is an example.
Line level signal = 1.0V = 1,000 mV = 0 dBV

Shure SCM810 main output is an example.
Power amplifier signal (loudspeaker level) = 10V = +20dBV

QSC GX3 amplifier output is an example. 
https://service.shure.com/s/article/audio-signal-levels-general-guidelines?language=en_US
//-->

The chart shows nicely how low mc level is in comparison to the two variants of line level.

Lets leave the other factor "impedance" aside and focus just on this millivolt thing: Such a signal cannot be reliably transported over a distance longer than a few feet. Rather it needs to be brought up to line level rather sooner than later. 

Line level is almost 1000 times higher than mic level. That is quite a factor!

Line level is adequate to send a signal from one device to another.

![foo](/tec/log/audio/images/AudioInterfaceNeutrikJacksXLR63.jpg){:class="resize"}

So the combojack for an outer microphone level XLR plug and a center line level starts to look different!

Closely related to all this is the electrical impedance of the low-impedance or high-impedance variants, and their transmission over balanced or unbalanced cables. The balanced XLR cable has 3 pins for a good reason -- but that is another topic.


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


By the way, the reason why we record in 44.100 Hz or for videos 48.000 Hz is that this is 2 times 20.000 Hz plus a bit of extra for the sampling filter to work.

-> Nyquist frequency


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

## Reading Microphone Datasheets

A less readable part of datasheets of microphones might be the graphs about polar patterns and frequency responses. But that part is 

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

Preface:

In the context of audio, Dynamic Range is the difference in Decibel between the quietest and loudest part.
It can refer to both the dynamic range of the audio track(s) in a video,
or the capabilities of a signal chain consisting of hardware and software.

The quietest part of a signal chain is called noise floor and each piece of equipment has one -- even a cable.

The dynamic range can be altered by compression and expansion:
Compressors (and in its extreme form Limiters) reduce Dynamic Range, while Expander (and in its extreme form Gates) increase it.

Wait, what? A Noise Gate does INcrease what exactly? Heh -- the dynamic range!

By the way, in an audio )post-)processing workflow they have their place, and quite often chained after each other.


https://ask.audio/articles/mixing-concepts-what-is-dynamics-why-you-should-care

- noise gate
- expander

### Compressor

> A compressor is an electrical amplifier that reduces the dynamic range of a signal. Basically, it brings the loud and quiet parts closer together in terms of volume. Most compressors have a few standard controls. Threshold determines how loud the incoming signal needs to be before it gets any treatment. Ratio adjusts how much the incoming signal, that is above the threshold, is compressed. The higher the ratio, the more squished the sound. Attack/Release controls how long it takes the compressor to react to the incoming signal. Lastly, input gain simply makes the pretreatment sound louder, allowing more of the signal to be above threshold, resulting in more compression.
> https://www.dancemusicnw.com/compressors-expanders-gates-explained/

Threshold
Ratio
Attack time
Release time <-------------
Knee
Make-up gain or output gain

<!--
The fundamental controls of audio compressors.
Understanding the technical aspects and terminology of audio compression will allow you to work more comfortably with a wide range of compressors.

 

Threshold

The threshold is the level at which compression begins. Once a threshold level is set, any audio below the threshold will be unaffected, but any audio above the threshold will be compressed by the ratio set. “Imagine a guitarist that’s strumming at a constant volume, then hits a few notes super hard in the middle of the song. You would want the compressor to be set where the threshold grabs only that loudest part of the track,” says Rodocker.

 

Ratio

The ratio is the amount of attenuation — or downward compression — that will be applied once a signal reaches the threshold. Peter explains that “the volume of audio is measured in decibels (dB), so if you set a 3:1 compression ratio, every 3dB of input signal above the threshold will produce 1dB of output signal.”

 

Attack time

The attack time is how long it takes the audio signal to be fully compressed to the ratio set after it has crossed the threshold. “It’s going to affect the first part of the sound you hear,” says Rodocker. “So you can set a slower attack to create some punch from an instrument that’s softer, like a keyboard, or a fast attack to quickly compress the sound of a loud guitar pick.”

A musician recording bass using a tube compressor.
A producer monitoring audio being recorded in their studio
Release time
The release time is how long it takes the audio signal to revert from being affected to uncompressed. At low levels of gain reduction, fast release speeds sound the most natural. However, extreme compression with a fast release time can result in a pumping effect — or a sudden increase in volume — that can make the track sound uneven in some genres of music.

 

Knee

The knee is how quickly the compressor transitions from not compressing the signal to compressing it. A soft knee will sound smoother because the compression doesn’t begin as quickly, while a hard knee will sound more dramatic. “Bass guitar and vocals would sound better using a soft knee, but I would use a hard knee for any kind of percussive instrument, like the piano or kick drums,” says producer, engineer, and mixing artist Gus Berry.

 

Make-up gain or output gain

The level of the signal coming out of a compressor won’t be as high as it was when it went in because the compressor is actively turning down parts of the signal. Make-up gain is used to turn the overall level of the signal back up. “The way you do this is to play the material while bypassing and activating the compressor, adjusting the make-up gain to where they sound more or less the same level,” advises Rodocker.

https://www.adobe.com/creativecloud/video/discover/audio-compressor.html
//-->


<!--

https://www.izotope.com/en/learn/audio-dynamics-101-compressors-limiters-expanders-and-gates.html
//-->


{% include youtubePlayer.html id="4gNRGqHzMKc" %}



### Expander and Gate

<!--
>An expander is essentially the opposite of a compressor. It’s used to increase the dynamic range of a signal, drawing the loud and quiet parts further apart. Since expanders are so similar to compressors, their controls are usually the same. The only differences are how those controls behave. Threshold now determines how quiet a signal needs to be before it gets treated, ratio now represents expansion rather than compression, and the attack & release functions are reversed. In fact, many compressors have an expander setting built into them!
https://www.dancemusicnw.com/compressors-expanders-gates-explained/

A gate is much like an expander, only with a MUCH higher ratio. Any signal that is below the threshold is effectively muted, while anything above the threshold passes through unscathed. It’s like a door that only opens for a signal strong enough to pass through. There are usually attack & release controls that function just like an expanders. Gates also tend to have a hold control that regulates how long the gate stays open after the input signal drops back below the threshold.
//-->

A Gate, or noise gate, is like an inverted compressor: Instead of limiting signals above a given threshold, the gate lowers a signal below a given threshold.

<!--
Audio Gating 101
The main controls you’ll find on a standard, basic gate are threshold, attack, release and sometimes hold. When additional controls such as range and ratio are introduced into the picture, gating becomes expansion.

Essentially, gates and expanders are both just a variation on the same thing. Think of a gate as an expander with a high ratio, and an expander as a gate with a low ratio. This is similar to the difference between a limiter and a compressor. In fact, a limiter is basically the exact opposite of a gate, while an expander is basically the opposite of a compressor.

https://theproaudiofiles.com/what-is-a-noise-gate/
//-->


## Equalisation: Changes to the Frequency Spectrum


Sibilance



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
