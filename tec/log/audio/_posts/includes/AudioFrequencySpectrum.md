#{{ include.headingmodifier }} The Audio Frequency Spectrum

This audio frequency spectrum shows the range of frequencies that the human ear can interpret. As a rule of thumb we hear at maximum from 20 Hz to 20.000 Hertz -- or 20 kilo Hertz.

As it is a logarithmic scale the higher numbers are better visualized with the octaves of a piano keyboard.

> Our speaking voice has three frequency ranges that need to be understood;
> 1. Fundamentals.  The fundamental frequencies of speech occur roughly between 85Hz and 250Hz.
> 1. Vowels.  Vowels sounds contain the maximum energy and power of the voice, occurring between 350Hz and 2KHz.
> 1. Consonants.  Consonants occur between 1.5KHz and 4KHz.  They contain little energy but are essential to intelligibility.

![frequency spectrum human hearing human voice](/tec/log/audio/images/frequency-spectrum.png){:class="resize"}

Although we might hear in that frequency range the human voice is located in a smaller range.
Male voices typically from 200 to 6000 Hertz,
and female voices from 400 to 8000 Hertz.


A problematic range is between 5000 and about 8000 Hertz, where the so-called sibilance occurs.
Sibilance is that harsh sound that can happen during consonant syllables (like S, T, and Z).
Techniques like a De-Esser try to cut very narrowly within this frequency band.

By the way, the reason why we record in 44.100 Hz or for videos 48.000 Hz is that this is 2 times 20.000 Hz plus a bit of extra for the sampling filter to work. This is based on the Nyquist Sampling Theorem.