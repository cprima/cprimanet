---
layout: post
title: "Sound Good in Webinars: Setup, Analysis and Evaluation of Improved [YouTube] Audio"
component: biz
date:   2022-02-25 00:00:00 +0100
abstract: ""
---

# Preview: Key Takeaways

{% include youtubePlayer.html id="zOoyFPlM3qQ" %}

Good sound for webinars or video conferences starts at the beginning of an audio signal chain with the *room sound* and the *microphone*. The room sound *is* greatly influenced by *reflective*, absorptive and *diffusive* qualities of the materials within. The microphone's *polar pattern* and frequency response feeds on *mic level* into the production workflow. A dedicated *audio interface* solves the analog-digital conversion in *hardware*; by the way acceptable hardware involved *is not* wireless. Distributing to YouTube demands for tight control of the normalized loudness and true peak, which can be achieved with compressor, limiter and e.g. the software Youlean Loudness Meter. While doing so an applied EQ ("equalizer") *curve* may "fix in post" some deficiencies at the beginning of the audio signal chain. Whether that happens analog at the beginning of the signal chain or digitally in post-production: Audio recording is best understood on the basis of electrical signals and their visual representations like *waveforms* and frequency spectrums.

# After the event

[![feedback form](/biz/images/form-feedback-postevent_120x212.png){: style="float:right"}](https://docs.google.com/forms/d/e/1FAIpQLSdJOUW52YTXPjJp9c0w-mRzv5DbOEd5DeYEvW95uNz3OqgGTQ/viewform)

## Feedback

Please leave feedback (anonymously) in a [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdJOUW52YTXPjJp9c0w-mRzv5DbOEd5DeYEvW95uNz3OqgGTQ/viewform).

There is no need to sign into answer the form. E-Mail addresses are **not collected**.

By the way, any type of event benefits from a feedback form. It is good practice to always have such a form URL at hand.



# Problem

![Picture description](/biz/consulting/images/LinkedInAndersJensenAskingSoundEngineer.png){:class="resize"}

## Step 1: Reading the incident report

Let us read this comment on LinkedIn as if we were an IT Supporter and this was an incident:

- The reporter mentions that the volume is being turned up
- The room has a certain qualitiy attributed to it ("is quiet")
- Off-the-shelf technology is mentioned (The RØDE wirelss Go microphone)
- The quality of the recording is described as having white noise

## verfifying the incident report



- Listening to the linked video the room is indeed quiet, but has a reverb like a kitchen or 
- The term "white noise" is not 100% correctly used, it is safe to assume that "noise floor" is meant
- The description of the audio signal chain is not complete

## ticket triage

- more information is needed,
- contact reporter! ;)

# Solution

Teaching a man to fish, and all this! A complex problem deserves some basic explanations and definitions first.

## Room Acoustics, Reverberation Time and Clap Test

The journey to improve the audio quality of a recorded narration for webinars or in videoconferences does not start with buying equipment. Because equipment is used inside a room and the room is where it starts.

The requirements to record for webinars are very similar to those of the voice actors, or voice over artists. And they are quite different from music producers or audio mixers. And quite different from high fidelity music listeners. So this kind of narrows down from whom to take advice from.
Another good source of advice are audio engineers in churches, by the way. And with a bit of training our own ears are another authoritative judge!

![Audio Signal Chain](/tec/log/audio/images/room-acoustics-materials.jpg){:class="resize"}

Within the room there will be direct sound and reflected sound from the walls and surfaces. The physical properties of these surfaces make or break a good room acoustic! Only so-called anechoc chambers have no reflected sound and they are not a good thing to strive for, by the way.

The reflected sound will hit our microphone again and decrease the quality of our recording. This reflected sound is THE most important aspect that needs to be controlled. Worst case is to sit between two hard walls which reflect our spoken word multiple times into the microphone until it dies down in volume.

And let's not forget that there is a reflective ceiling, too!

![Reflection Absorption Diffusion](/tec/log/audio/images/diffusion.png){:class="resize"}

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

![Play Store detail page for myRaumklang - Nachhall messen und optimieren](/tec/phy/myRaumklang/images/screenshot_play.google.com-store-apps-details-id-de.myraumklang.myraumklang.png){:class="resize"}

All this is another way of saying: Do a clap test, there is even an app for this!

Either the app or our own recording with our existing microphone into a software that displays a waveform will give us a measurement in seconds.

Then we do a few improvements, and measure again, and listen to our recording again.

![Clap Test Reveberation Time](/tec/log/images/clap-test_reverberation-time.png){:class="resize"}


In my room I have both hard and absorbant materials. But as the sound of my voice does not bounce back from the hard surfaces into the microphone I have not negative effect by the hard wooden cupboard doors. So a good room for audio recording does not need to be covered in foam all around!

![my room](/tec/log/audio/images/WOB38A8HO360_2022_1762-480.jpg){:class="resize"}

The biggest problem of my room is that the heating pipes transmit sound from the teenagers room underneath. Reverberation time does not fix THAT. Maybe I will give them a gamer's headset next christmas! ;)

Going by sich an (inofficial) RT60-like measurement means that it is easy to find out when to stop improving the room acoustic, and focus on other aspects of good audio in webinars!


{% include checklist.html checklistnames="Eliminate *noise,YouTube Pre-Upload Audiotrack,Windows 10 Audio Recording Inventory" heading="h2" %}

To reduce complexity a lot can be learned from the aviation industry: Their checklist culture is outstanding and based on a very easy to read tabular format: Arranged in a "Item" and "Condition" heading, the item to be checked is listed with the desired condition.

<!--
## Get in Contact

I love to connect with like-minded people and invite you to [Connect on LinkedIn](https://www.linkedin.com/in/cprima/). As I do not sell anything I won't pitch to you! ;)//-->
<!-- [![LinkedIn](/biz/marketing/images/ConnectOnLinkedIn.png)](https://www.linkedin.com/in/cprima/) -->
<!--
As this event is a hobby of mine I tend to frequent the site only outside Central European Working hours though.

In the past months I posted weekly snippets and short posts about automation, do-it-yourself, RPA and all things audio-video.
//-->

# Recording

The recording of the event is available at the livestream location on YouTube:

{% include youtubePlayer.html id="Frg5-22oChs" %}

☛ webpage of the event: https://www.cprima.net/biz/consulting/workshops/2022/02/25/2022-02-25-live-event-sound-good-in-webinars.html 

YouTuber Anders Jensen asked on LinkedIn if someone could help to improve the audio of his YouTube video and livestreams.

Well, I have repeated professional testimonials that I like to help other people fulfilling their potential.

Join Anders Jensen and me on a live session where
- we are going to wrap up first improvements for his video channel and his teaching business
- I share the condensed learning of my past 2 years
- and paint a roadmap for future improvements.

Participants will 
- be able to derive actionable ideas from this journey for their own improvements
- distinguish elements of good audio to apply to their own online presence
- rank these by difficulty and affordability
- recognize basic terms and concepts of audio engineering