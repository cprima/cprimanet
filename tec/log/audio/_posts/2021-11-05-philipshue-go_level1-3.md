---
layout: post
title: In the Homeoffice, show that you are On Air with a Philips Hue Go
component: TA_PTC_033
date:   2021-11-06 00:00:00 +0100
abstract: "In the Homeoffice, show that you are On Air with a Philips Hue Go."
---

A quick and easy way to signal family members, the partner or room mate that you are really, really busy is by color and with light.

Ever seen these "on air" signs that they use at radio stations or in recording studios? If the red light is on you better stay away from the door handle for sure!

![teaser](/tec/log/homeoffice-onair/images/home-sweet-office_onair_level1-3.png)

Combined with the colors of a traffic light such a signalling makes for a great solution in the homeoffice to tell kids that you really am in a conversation right now -- or that "the air is clear again" afterwards.

## Entry level

Buy a Philips Hue Go light and be done: There's an app for that and you can preset red, yellow and green as a widget on the smartphone screen to trigger predefined "scenes".

![Philips Hue Go](/tec/phy/PhilipsHue/images/screenshot_philips-hue.com_product-Go.png){:class="resize"}

## Next Level

If you have a home automation system in place you could synchronize a calendar and trigger light changes depending on your calendar entries.

## Pro Level

If you are into customized automation-at-your-fingertipps chances are that you have (heard of) a ElGato Streamdeck, the button-clad touchscreen macro-keyboard like box on your desk. Combined with developer access to the API of a Philips Hue bridge the press of a button signals "red" -- and even more important that you are available again to build up the trust in the solution.

![usecase](/tec/phy/PhilipsHue/OnAirLightAtHomeoffice%20-%20deployment.png){:class="resize"}

Here are my json payloads for a POST request to the Hue Bridge API:

```json
{"on":true, "sat":254, "bri":32,"xy":[0.675,0.322]} //red
{"on":true, "sat":254, "bri":32,"xy":[0.5,0.45]} //yellow
{"on":true, "sat":254, "bri":32,"xy":[0.2,0.7]} //green
{"on":false} //off
```

{% include youtubePlayer.html id="lkXlo8eg75E " %}  
