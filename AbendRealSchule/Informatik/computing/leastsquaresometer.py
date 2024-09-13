###############################################################################
#                    ~*~ leastsquaresometer.py ~*~                            #
#                                                                             #
#  Least squares fit visualisation. Calculates squares of deviations and      #
#  shows how they change when user varies slope and intercept.                #
#                                                                             #
#               (c) Louise Dash June-November 2013                            #
###############################################################################


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Slider

### Read in data
# normally data should be in a text file with x and y values
#x,y = np.loadtxt("mydata.dat",unpack=True, usecols=[0,1])
# For this visualization, best if slope ~ 1, so use this data instead
# feel free to vary the values!
x = np.array([10,20,30,40,50])
y = np.array([14.3,20.68,33.1,42,47.7])

# basic information from the data
x_min = np.min(x)
x_max = np.max(x)
y_min = np.min(y)
y_max = np.max(y)

print " The minimum value of x is", x_min
print " The maximum value of x is", x_max
print " The minimum value of y is", y_min
print " The maximum value of y is", y_max

### Fit the data

mean_x = np.mean(x)
mean_y = np.mean(y)
slope = np.sum((x - mean_x)*y) / np.sum((x - mean_x)*x)
intercept = mean_y - slope*mean_x
sum_of_squares = np.sum((y - slope*x - intercept)**2)
print " Fitted line: slope is", slope
print "   ... and intercept is", intercept
print " Sum of squares is", sum_of_squares
# generate a list of x-points for the fitted line
# straight line only needs 2 points, but we'll do more.
x_points = np.linspace(x_min/2.,x_max*2.,100)
y_points = slope*x_points + intercept


### Set up the initial plot

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, aspect='equal') # need this to use add_artist
plt.subplots_adjust(left=0.01, bottom=0.25) # make some more room at bottom and left
plt.plot(x, y, 'ro')
plt.line, = plt.plot(x_points, y_points, 'g-') #nb use of comma
plt.xlim(0.8*x_min,1.1*x_max)
plt.ylim(0.8*y_min,1.1*y_max)
plt.xlabel('x')
plt.ylabel('y')

sq_text = ax.text(15,-1,'Sum of the area of the squares is %1.2f' %sum_of_squares)
### define the sliders
axcolor = 'lightgoldenrodyellow' # any color will do

# add an axes (subplot) in the space we made using subplots_adjust
ax_slope = plt.axes([0.15, 0.1, 0.5, 0.03], axisbg=axcolor)
ax_intercept  = plt.axes([0.15, 0.15, 0.5, 0.03], axisbg=axcolor)
# ...and put a slider in it
slider_slope = Slider(ax_slope, 'Slope', slope*0.5, slope*1.5, valfmt='%4f',valinit=slope)
slider_intercept = Slider(ax_intercept, 'Intercept', intercept*0.5,intercept*1.5,
    valfmt='%4f', valinit=intercept)


###  set up the squares for the initial plot
sqcol = '#99b267'
patches = []
for xx,yy in zip(x,y):
    # calculate vertical distance from datapoint to line
    dist = yy - (slope*xx + intercept)
    if slope > 0:
        if dist > 0:
            # datapoint is TOP RIGHT of the square
            posx = xx-dist
            posy = yy-dist
            wid = dist
            hei = dist
        else: # dist is negative
            # datapoint is BOTTOM LEFT of the square
            posx = xx
            posy = yy
            wid = -dist
            hei = -dist
    else: #slope is negative
        if dist > 0:
            # datapoint is TOP LEFT of the square
            posx = xx
            posy = yy - dist
            wid = dist
            hei = dist
        else: # dist is negative
            # datapoint is BOTTOM RIGHT of the square
            posx = xx+dist
            posy = yy
            wid = -dist
            hei = -dist

    square = Rectangle(xy=(posx,posy), width=wid, height=hei)
    patches.append(square)
    
sq_collection = PatchCollection(patches, alpha=0.4)
#sq_collection.set_array(np.array(colors))
ax.add_collection(sq_collection)

def update_squares(val):
    """Function to update the plot based on current slider positions.
    Recalculates the squares and updates the straight line.
    """
    slope = slider_slope.val
    intercept = slider_intercept.val
    sum_of_squares = np.sum((y - slope*x - intercept)**2)
    y_points = slope*x_points + intercept 
    sq_text.set_text('Sum of squares is %1.2f' %sum_of_squares)
    del ax.collections[:] # delete the old squares
    patches = []
    for xx,yy in zip(x,y):
        # calculate vertical distance from datapoint to line
        dist = yy - (slope*xx + intercept)
        if slope > 0:
            if dist > 0:
                # datapoint is TOP RIGHT of the square
                posx = xx-dist
                posy = yy-dist
                wid = dist
                hei = dist
            else: # dist is negative
                # datapoint is BOTTOM LEFT of the square
                posx = xx
                posy = yy
                wid = -dist
                hei = -dist
        else: #slope is negative
            if dist > 0:
                # datapoint is TOP LEFT of the square
                posx = xx
                posy = yy - dist
                wid = dist
                hei = dist
            else: # dist is negative
                # datapoint is BOTTOM RIGHT of the square
                posx = xx+dist
                posy = yy
                wid = -dist
                hei = -dist
        square = Rectangle(xy=(posx,posy), width=wid, height=hei)
        patches.append(square)
        
    sq_collection = PatchCollection(patches, alpha=0.4)
    ax.add_collection(sq_collection)
    
    plt.line.set_ydata(y_points) # put the new ydata in "line"
    plt.draw() # draw it.


# if the slider posn changed, update and recalculate
slider_slope.on_changed(update_squares)
slider_intercept.on_changed(update_squares)

# output the plot to the screen
plt.show()
