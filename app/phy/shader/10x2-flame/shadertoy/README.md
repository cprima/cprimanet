---
checklists: []
---

```
/**
 * Draws quadratic function graph 10x² upside down,
 * uses for each x it's y value to blend the red and green channel
 * and flickers by a sinuoid fraction of the elapsed time.
 *
 * @author: Christian Prior-Mamulyan <cprior@gmail.com>
 * @licence: public domain
 * @see: https://www.shadertoy.com/view/3sX3RX by catafest
 *
 */

#define time iTime // elapsed time
float flame_width = 10.; //sane values between 6. and 12.
float y, fx;
float resolution_multiplier = 1.4; // to move the tip of the flame a bit downwards
float position_x_offset = 0.;
float position_y_offset = 0.1;
vec3 black = vec3(0.0, 0.0, 0.0);
vec3 green = vec3(.0, 1., .0);
vec3 yellow = vec3(1., 1., .0);
vec3 blue = vec3(.0, 0., 1.);
float initialdebugduration = 4.;


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{

    if (time < initialdebugduration){
        position_y_offset = 0.;
    }

    // Normalized pixel coordinates (from 0 to 1)
    // 0 is top left
    vec2 uv = (fragCoord/iResolution.xy) * resolution_multiplier;

    // re-set coordinates to center the flame
    // x and y will be between -0.5 and 0.5
    vec2 position = uv - vec2( (resolution_multiplier / 2.) + position_x_offset , 0.5 + position_y_offset);

    //position.y *= -1.; // flips the output and makes the quadratic graph easier to recognize

    vec3 color = black;

    // y0 is above and y1 is below, so 10x squared 2 will be flipped downwards
    // x values
    float fx = pow(position.x * flame_width, 2.);

    // flickering generated by moving the coordinate system by a small amount with time as factor
    if (time >= initialdebugduration){
        position.y += fract(sin(time * 24.)) * 0.1;
    }

    // length returns the length of the vector, i.e. $\sqrt { { x[0] }^2 + { x[1] }^2 + \dots }$.
    float y = length(position + vec2(position.x, fx));
    // smoothstep performs interpolation (lower, upper, source)
    color.r += smoothstep(0.0, 0.3, (resolution_multiplier/2.) - y) * 0.71; //solarized yellow 181,137,0
    color.g += smoothstep(0.0, 0.3, (resolution_multiplier/2.) - y) * 0.54; //solarized yellow 181,137,0
    color.b = color.b; // :-) //solarized yellow 181,137,0
    //color.rg += 1. - y; // alternative to the smoothstep(s) above

    //some colors to "debug" visually
    if (time < initialdebugduration) {
        if (position.x > (resolution_multiplier/2.*.5)*+1.) {
            color = green;
        }

        if (position.x < (resolution_multiplier/2.*.5)*-1.) {
            color = green;
        }

        if (position.y > (resolution_multiplier/2.*.5)*+1. + position_y_offset) {
            color = blue;
        }
        if (position.x < .5 - y) {
            color = yellow;
        }
    }

    // as per shadertoy convention, fragColor hands over the RGB color to the engine
    fragColor = vec4(color,1.0);
}


/*
MadMapper material
vec4 materialColorForPixel( vec2 texCoord )
{
    // Normalized pixel coordinates (from 0 to 1)
    // 0 is top left
    vec2 uv = (texCoord)*1.4;
    // re-set coordinates to center the flame
    // x and y will be between -0.5 and 0.5
    vec2 position = uv - vec2(0.7, 0.6);
    position.y *= -1.;


    // black as background
    // vec3(1.0, 1.0, 0.0) is yellow
    vec3 color = vec3(0.0, 0.0, 0.0);

    // y0 is top and y1 is bottom, so 10x squared 2 will be flipped downwards
    // x values
    float fx = pow(position.x * 6., 2.);

    // flickering generated by moving the coordinate system by a small amount with time as factor
    position.y += fract(sin(TIME * 24.)) * 0.1;

    // 
    float y = length(position + vec2(position.x, fx));

    color.r += smoothstep(0.0, 0.3, 0.71 - y) * 0.71;
    color.g += smoothstep(0.0, 0.3, 0.71 - y) * 0.54;
    //color.rg += 1. - y;

    // Output to screen
    return vec4(color,1.0);
}
*/

/*
+───────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+────────+────────+────────+────────+────────+────────+────────+────────+─────────+
| xy    | -0.500  | -0.400  | -0.300  | -0.200  | -0.100  | -0.075  | -0.050  | -0.025  | 0.000  | 0.025  | 0.050  | 0.075  | 0.100  | 0.200  | 0.300  | 0.400  | 0.500   |
+───────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+────────+────────+────────+────────+────────+────────+────────+────────+─────────+
| 10x²  | 25.000  | 16.000  | 9.000   | 4.000   | 1.000   | 0.563   | 0.250   | 0.063   | 0.000  | 0.063  | 0.250  | 0.563  | 1.000  | 4.000  | 9.000  | 16.000 | 25.000  |
| -0.5  | 25.500  | 16.500  | 9.500   | 4.500   | 1.500   | 1.063   | 0.750   | 0.563   | 0.500  | 0.563  | 0.750  | 1.063  | 1.500  | 4.500  | 9.500  | 16.500 | 25.500  |
| -0.4  | 25.400  | 16.400  | 9.400   | 4.400   | 1.400   | 0.963   | 0.650   | 0.463   | 0.400  | 0.463  | 0.650  | 0.963  | 1.400  | 4.400  | 9.400  | 16.400 | 25.400  |
| -0.3  | 25.300  | 16.300  | 9.300   | 4.300   | 1.300   | 0.862   | 0.550   | 0.362   | 0.300  | 0.362  | 0.550  | 0.862  | 1.300  | 4.300  | 9.300  | 16.300 | 25.300  |
| -0.2  | 25.200  | 16.200  | 9.200   | 4.200   | 1.200   | 0.763   | 0.450   | 0.263   | 0.200  | 0.263  | 0.450  | 0.763  | 1.200  | 4.200  | 9.200  | 16.200 | 25.200  |
| -0.1  | 25.100  | 16.100  | 9.100   | 4.100   | 1.100   | 0.662   | 0.350   | 0.162   | 0.100  | 0.162  | 0.350  | 0.662  | 1.100  | 4.100  | 9.100  | 16.100 | 25.100  |
| 0     | 25.000  | 16.000  | 9.000   | 4.000   | 1.000   | 0.563   | 0.250   | 0.063   | 0.000  | 0.063  | 0.250  | 0.563  | 1.000  | 4.000  | 9.000  | 16.000 | 25.000  |
| 0.1   | 24.900  | 15.900  | 8.900   | 3.900   | 0.900   | 0.463   | 0.150   | 0.037   | 0.100  | 0.037  | 0.150  | 0.463  | 0.900  | 3.900  | 8.900  | 15.900 | 24.900  |
| 0.2   | 24.800  | 15.800  | 8.800   | 3.800   | 0.800   | 0.362   | 0.050   | 0.138   | 0.200  | 0.138  | 0.050  | 0.362  | 0.800  | 3.800  | 8.800  | 15.800 | 24.800  |
| 0.3   | 24.700  | 15.700  | 8.700   | 3.700   | 0.700   | 0.263   | 0.050   | 0.237   | 0.300  | 0.237  | 0.050  | 0.263  | 0.700  | 3.700  | 8.700  | 15.700 | 24.700  |
| 0.4   | 24.600  | 15.600  | 8.600   | 3.600   | 0.600   | 0.162   | 0.150   | 0.338   | 0.400  | 0.338  | 0.150  | 0.162  | 0.600  | 3.600  | 8.600  | 15.600 | 24.600  |
| 0.5   | 24.500  | 15.500  | 8.500   | 3.500   | 0.500   | 0.063   | 0.250   | 0.438   | 0.500  | 0.438  | 0.250  | 0.063  | 0.500  | 3.500  | 8.500  | 15.500 | 24.500  |
+───────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+─────────+────────+────────+────────+────────+────────+────────+────────+────────+─────────+

+───────+───+───+───+───+───+───+───+───+───+
|       |   |-0.|-0.|-0.|   | 0.| 0.| 0.|   |
|       | < |075|050|025| 0 |025|050|075| > |
+───────+───+───+───+───+───+───+───+───+───+
| -0.5  | ░ | ░ | ░ | ░ | ▓ | ░ | ░ | ░ | ░ |
| -0.4  | ░ | ░ | ░ | ▓ | ▓ | ▓ | ░ | ░ | ░ |
| -0.3  | ░ | ░ | ░ | ▓ | ▓ | ▓ | ░ | ░ | ░ |
| -0.2  | ░ | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ | ░ |
| -0.1  | ░ | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ | ░ |
| 0     | ░ | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ | ░ |
| 0.1   | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ |
| 0.2   | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ |
| 0.3   | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ |
| 0.4   | ░ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ | ░ |
| 0.5   | ░ | ▓ | ▓ | ▓ | ░ | ▓ | ▓ | ▓ | ░ |
+───────+───+───+───+───+───+───+───+───+───+


*/
```