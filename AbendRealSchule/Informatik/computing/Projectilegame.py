##################################################
#                                                #
#   Template code for PHAS1240 final assignment  #
#   An "Angry Birds"-like game                   #
#   Louise Dash December 2013                    #
#                                                #
##################################################

# you will probably want to use all this commands from the visual module
from visual import sphere, display, curve, color, mag, random, box, label, vector, rate, cross
import numpy as np

#set up the scene
scene = display(width = 640, height = 480, center = (10,0,0))
ground = curve(pos=[(0,0,0),(20,0,0)],color = color.green)

print "Fire a projectile to try to topple the target"


### initial ball coordinates and other parameters

x0 = 0.0
y0 = 0.0
x = x0
y = y0
px = 0.0 # initial momentum vector coordinates
py = 0.0
pz = 0.0
g = 9.8 # gravitational accln, m.s^-2
m = 0.1 # mass of ball, kg
dt = 0.005 # time interval for loop, in seconds


### place the target at a random position 5-15 m away
x_targ =10 #random.uniform(5,15) # randomised target position
print "The target is ", round(x_targ,2), " metres away from you."
target_height = 2.0 # height of target, metres
target_width = 0.5 # width of target, metres (length = width)
target_mass = 100 # mass of target, kg
ball_rad = 0.2 # radius of ball (unitless, for animation only)
ball_mass = m # mass of ball in kg
contact_time = 0.01 # contact time for collision impulse calculation, in seconds


### set up visual objects
target = box(pos=(x_targ,target_height/2.0,0), length=target_width, height=target_height, width = target_width, color = color.red)
target_label = label(pos = target.pos, xoffset = -15, yoffset = -20, text = "Target at \n x = %1.2f m" % target.pos.x)
ball = sphere(pos = (x0,y0,0),radius = ball_rad, make_trail=True, color=color.blue)
coord_label = label(pos = (10,-10,0), text = " Projectile at \n x = %1.2f m, y = %1.2f m" % (ball.pos.x, ball.pos.y) )
momentum = vector(px,py,pz) # momentum vector

scene.autoscale = False

hit = False # A boolean variable to switch to True when player succeeds in hitting target
hit_tolerance = 0.5 # tolerance for defining a "hit" = centre-centre distance of ball and target
topple = False # A boolean variable to describe whether or not the taget falls  

while  topple== False and hit == False: # while ball has not hit target, loop code below. 
   
### ask for input
    dtheta = float(raw_input("Input the initial angle in degrees: ")) # user inputs angle of launch in deg
    theta = np.radians(dtheta) # convert launch angle to rad
    v0 = float(raw_input("Input the initial velocity in metres/second: ")) # user inputs launch velocity
    print "Ball fired!"
    y=y0
    x=x0
    t=0.0
### animate ball trajectory 
    while y >= y0 and hit== False: # loop code if the ball is higher than the ground and does not hit the target
            x= x0 + v0*np.cos(theta)*t # calculate new x position
            y= y0+ v0*np.sin(theta)*t- 0.5*g*t**2 # calculate new y position
            t=t+dt # increment time by dt
            ball.pos= (x,y,0) # update the position of the ball
            rate(50) # set the rate of animation
### determine if ball hits target
            if np.abs(x-x_targ) <= hit_tolerance and y <= target_height: # if distance between centre of ball and centre of target is less than the hit tolerance, the ball hits the target
                print "HIT"
                hit= True #ball hits target
### determine if ball topples target
                x_vel= v0 * np.cos(theta)# x velocity ( no acceleration in x direction) 
                y_vel= v0 * np.sin(theta) - g * t # y velocity ( acceleration due to gravity) 
                momentum= vector( ball_mass * x_vel, ball_mass * y_vel, 0) # final momentum of ball
                t_app= mag( momentum * y /contact_time) # calculate magnitude of torque applied to arget by ball 
                t_rest= np.abs( target_mass* g * 0.5 * target_width) # calculate magnitude of restoring torque on target
                if t_app > t_rest :
                    print "You toppled the target" 
                    print "WINNER"
                    
                    while n<=16:
                        target.rotate(angle=-np.pi/32, axis=[0,0,1], origin=[x_targ+ 0.5*target_width, 0,0])
                        n=n+1
                        rate (10)
                    topple = True
                if t_app < t_rest:
                    topple= False
                    hit= False 
                    print " The target did not fall, try again"

    if hit ==False :
        print " TRY AGAIN"


 
### Calculate if target topples



