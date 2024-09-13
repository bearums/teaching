################################################################################
# Fourier Series Square Wave with Slider to Adjust Number of Terms in Series   #
# Ben Hastings, 24/11/2013                                                     #
################################################################################


import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


def fourierfcn(x,t): # x is data to be plotted. t is number of terms 
    """ Returns one term in the fourier series for a square wave """
    L=1 # set the period of the wave ( L is half the period) 
    n=1 # set the term number to 1 initially 
    fourier=0 # set the initial result of the summation to 0 
    while n <= t*2  : # start a while loop until twice the term limit is reached. Note twice term limit because only every other term is actually summed
        if n/2 *2 != n:  # ensure only odd n terms of the series are summed. Use of integer division
            new_term= (4/np.pi) * 1/n * np.sin((n*np.pi* x)/L) # generate new term in the series 
            fourier= fourier + new_term  # adds the new term to the series         
            n=n+1 # increment the number of terms 
        else: 
            n=n+1 # increment the number of terms. Note nothing is added to the series, as n is even in this case 
    return fourier # return the value of the summation 

#Generate the initial data:
terms = 1 # this variable will be controlled by slider
x = np.linspace(0,5,1000) # grid of x data
y =fourierfcn(x, terms)  # the function to plot

# Generate up the initial plot:
ax = plt.subplot(111) # create new axes for 1 row, 1 column, plotnumber 1
                      # This is the default axis
plt.title( ' Fourier Series Square Wave', fontsize= 18) # Add a title to the plot and choose fontsize 
plt.subplots_adjust(left=0.15, bottom=0.25) # make room for the slider 
plt.line, = plt.plot(x,y , linewidth=1, color='r') # plot data, choosing line width and colour of line 
plt.xlim( 0, 5.1) # crop the x axis 
plt.xlabel("x") # choose an x axis label
plt.ylabel("y") # choose a y axis label 

#define the sliders:
axcolor = 'lightgreen' # choose a colour for the slider axis, any colour works 
ax_terms = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)# add axes (a subplot) in the space we made using subplots_adjust
slider_terms = Slider(ax_terms, 'number of terms ', 0,30, valfmt='%0.00f',valinit=(1)) # choose title for slider, range, format of values displayed ( %0.00f is integers) and initial slider value 

def update_terms(val):
    """function to update the plot based on current slider_phase position"""
    terms = slider_terms.val # use slider position to set the number of terms 
    y = fourierfcn(x, terms) 
    plt.line.set_ydata(y) # make a line of the new y data
    plt.draw() # redraw the plot.

slider_terms.on_changed(update_terms)# if the slider position is changed, update number of terms  and recalculate

plt.show() # shows the plot 
