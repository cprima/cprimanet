#{{ include.headingmodifier }} Electric Signals, Noise, Discretization

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
