

https://www.youtube.com/watch?v=8Iuvj9hQczQ

Shift A Mesh plane, groundplane
S
Ctrl A Scale
Properties Panel Physics Colission

Shift A Empty Plane Axis
G z

Shift A Mesh UVSphere
G z
s

Click Sphere, SHift click empty Ctrl p Parent?object

Click Sphere
Properties Panel Particle Proerties add ParticleSystem

Shift A Mesh UV-Sphere
g
"ember"

new Material Emission Stngth =50
color red-orange

click emitteig object, rename
Particle Properties  Render Render as object, instance object Scale 0.0x

select empty
Transform
Rotation Y = #frame/3 //purple
Location Z #sin(frame/5)/3+4.5

Properties Panel Scene Render Engine Eevee, Bloom 

ParticleProperties Velocity NormalVelocity 0.8 Object Velocity 0.2 Tangent Velocity 0.4 

select groundplane Physics Proeprties Dampening 0.6 Friction 0.2


Shift A Camera Transform Rotation X90 Y0 Z0, Location to set frame X,Y


Scene Proerties Motion Blur Shutter 50 Steps 250 Max Blur 512 bg sep 10

Particle EMission Number 2000 Frame Staert 1 Ed e.g.125 Lifetime 75 Lifetime Randomness .2 System Bake

select groundplane Material Properties Add BaseColor dark grey
edit mode	e	
select edge		
	z	
click		
bevel	Ctrl B	Segments = 32
exit edit mode	Tab	
modifiers		
subdivicion surface	simpoe, viewport subdivisions = 2	
render propertires	screenspace refflections = On	

select groundplane


Scene Proeprties Position EndOnFrame


Still ender: Shutter 50, steps 250
Animatin Render Shutter 20 steps 150


https://www.youtube.com/watch?v=eKMPXwl-Sac

shader tab
colorramp -> emission
value node
keyframes




https://www.graphicsandprogramming.net/eng/tutorial/blender/particles/create-comet-with-particles-in-blender
follow a curve



Creating Vertex Groups
Vertex groups are maintained within the Object Data tab (1) in the Properties


https://artisticrender.com/how-to-use-a-particle-system-in-blender-to-scatter-objects/

