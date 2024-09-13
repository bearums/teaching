################################################################
# A visualisation of the caesium chloride crystalline structure#
# Ben Hastings, 29/11/2013                                     #
################################################################
from visual import sphere, color, curve
import numpy as np

num = 3
size = 0.3 # size of the "atoms"
for i in range(-num, num+1): # loop over each spatial dimension
    for j in range(-num, num+1):
        for k in range (-num, num+1):
            sphere(pos=[i,j,k],radius=size,color=color.green) # generates a sphere 
            sphere(pos=[i+0.5, j+0.5, k+0.5], radius= 0.8*size, color=color.blue) #generates a sphere slightly displaced (by 0.5 of a unit) in each direction

