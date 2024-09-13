############################################################
# An Animation of a projectile under gravity               #
#   Ben Hastings, 06/12/2013                               #
#                                                          #
############################################################

from visual import sphere, curve, color, display, rate
import numpy as np

# set up the scene
scene = display(x = 50, y = 50, width = 640, height = 480, center = (20,0,0))
ground = curve(pos=[(-5,0,0),(50,0,0)],color = color.green)

# initial ball coordinates
x0 = 0.0
y0 = 0.0
y = y0
g = 9.8 # m/s2
dt = 0.01 # time interval for loop, in seconds

# input initial angle and velocity
dtheta = float(raw_input("Input the initial angle in degrees: "))
theta = np.radians(dtheta)
v0 = float(raw_input("Input the initial velocity in metres/second: "))


# start the animation
ball = sphere(pos = (x0,y0,0),radius = 1,make_trail=True)
t=0.0
while y >= y0:
    x= x0 + v0*np.cos(theta)*t # calculate new x position
    y= y0+ v0*np.sin(theta)*t- 0.5*g*t**2 # calculate new y position
    t=t+dt # increment time by dt
    ball.pos= (x,y,0) # update the position of the ball
    rate(15) # set the rate of animation 

# print results of projectile
rng= (v0**2*np.sin(2*theta))/g # calculate the range as predicted by suvat eqns 
print " " # create a blank line 
print "the projectile was in the air for", t, "s" # print the final t value
print "the projectile travelled",round(x,5) , "m" # print the final x value, rounded to 5dp
print "the predicted range is", round(rng,5), "m" # print the predicted range, rounded to 5dp
print "difference between predicted and actual ranges :",round(np.abs(x-rng),5), "m" # show difference between final x value and range. np.abs() produces the modulus



