#{{ include.headingmodifier }} Loudness

Do you remember the times when TV commercials were so much louder than the actual TV content?
That was the time when the human perception of loudness was not taken into consideration.

The signal level on microphone or line level are measured with a technical reference, and the loudness innovation was to measure according to the human perception. This started at about 2010.

![perceived loudness, equal loudness contour, integrated LUFS](/tec/log/audio/images/perceived-loudness_equal-loudness-contour_integrated-LUFS.png){:class="resize"}

Nowadays streaming service like Spotify and -- you guessed it -- YouTube use the loudness across a while song or video to adjust loudness. YouTube actually only lowers the loudness, and protects users with headphones that way.

Based on what is called the Fletcher Munson Curve of human loudness perception a loudness measurement is a statistically determined value over time, either

- short-term or
- integrated, that means over for example a whole YouTube video.

Software like Youlean Loudness Meter analyze the audio and returns a graphical representation.


Why is this important?

Because when the production loudness did differ from the target platform's rules then it makes sense to adjust the distribution loudness, to not leave it up to the streaming service to mess about with the audio.

YouTube for example will

- turn down videos that are integrated -- which mean over the full duration -- louder than -14dB LUFS (which is the ludness unit).
- but YouTube will not turn the loudness up if it was too low to begin with!

The loudness measurement makes our -- hopefully many -- recordings comparable comparable between each other.

Methods to influnce the loudness of a recording are

- the compressor or
- the amplifier

The loudness measurement also helps us to adjust an interview partner to the same loudness as the host.

This knowledge could be applied to for example by making a conscious decision between a production loudness and a distribution loudness.
