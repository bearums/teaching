###################################################
# A Simulation of two planets orbiting a star     #
# Ben Hastings 13/12/2013 (FRIDAY THE THIRTEENTH!)#
###################################################

from visual import sphere, vector, color, rate, mag
import numpy as np

dt = 0.01 # timestep
step = 1 # loop counter
maxstep = 2000 # maximum number of steps

#  Define the star, planets and constants
M = 1000 # mass of star (in units where G = 1)
mass = 1 # mass of planet
initpos = vector(0.0,1.0,0.0) # initial position vector of Planet
Planet = sphere(pos=initpos,radius=0.05*mass,color=color.blue,make_trail=True)
Planet.trail_object.color=color.white # make the trail white
Star = sphere(pos=(0,0,0),radius=0.1,color=color.yellow)
vel = vector(-25.0, 0.0, 0.0) # initial velocity of planet 1
pos= initpos # set position of planet to initial position 

#define second planet 
massb= 1.05
posb= vector( 0.0, 1.0, 1.0) # set initial position
velb= vector( -21.0, 0.0, -8.0) # set initial velocity 
Planetb=sphere(pos=posb,radius=0.05*massb,color=color.red,make_trail=True)
Planetb.trail_object.color=color.green # make trial green 
while step <= maxstep:
   # compute position of first planet 
    magpos= mag(pos) # calculate the magnitude of the position vector
    vel= vel- M*pos*dt/(magpos**3) # work out velocity
    pos= pos+ vel*dt # work out position 
    Planet.pos= pos #update the planet's position

    # compute position of second planet 
    magposb= mag(posb)
    velb= velb- M*posb*dt/ (magposb**3)
    posb= posb +velb*dt 
    Planetb.pos=posb

    step= step+1 # increment the loop counter 
    rate( 50) # set speed of animation
    
    

print("end of program")
