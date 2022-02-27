#{{ include.headingmodifier }} Types of Audio Editing

7 types https://audioaural.com/what-are-the-7-types-of-audio-editing-techniques/

- amplification: increase the volume
- compression: change the dynamics
- limiting: limit sound above a certain level
- panning: move the sound in and between left and right stereo channel
- equalization: changes to the frequency spectrum; low-cut, high-cut, bell boost, notch
- normalization: When the level of a track is increased so that it reaches a norm.
- stereo imaging:  the manipulation of an audio signal within the 180° stereo field

In the context of audio, Dynamic Range is the difference in Decibel between the quietest and loudest part.
It can refer to both the dynamic range of the audio track(s) in a video,
or the capabilities of a signal chain consisting of hardware and software.

The quietest part of a signal chain is called noise floor and each piece of equipment has one -- even a cable.


![dBFS Decibel Full Scale](/tec/log/audio/images/dynamic-range_headroom.png){:class="resize"}

##{{ include.headingmodifier }} Compressor

The dynamic range can be altered by compression and expansion:
Compressors (and in its extreme form Limiters) reduce Dynamic Range, while Expander (and in its extreme form Gates) increase it.

![dBFS Decibel Full Scale](/tec/log/audio/images/compressor.png){:class="resize"}


##{{ include.headingmodifier }} Expander and Gate

A Gate, or noise gate, is like an inverted compressor: Instead of limiting signals above a given threshold, the gate lowers a signal below a given threshold.
