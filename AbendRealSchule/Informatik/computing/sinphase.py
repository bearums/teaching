import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


### Set up the initial data:
phase = np.pi/2. # this variable will be controlled by slider
x = np.linspace(0,25,1000) # grid of x data
y = np.sin(x + phase) # the function to plot

### Set up the initial plot:
ax = plt.subplot(111) # create new axes for 1 row, 1 column, plotnumber 1
                      # This is the default axis
plt.subplots_adjust(left=0.15, bottom=0.25) # make some more room at bottom and left
plt.line, = plt.plot(x, y, linewidth=1, color='r') # nb use of comma
plt.xlabel("x")
plt.ylabel("sin(x + $\phi$)")

### define the sliders:
axcolor = 'lightgoldenrodyellow' # any colour works
# add axes (a subplot) in the space we made using subplots_adjust
ax_phase = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
# ...and put a slider in it
slider_phase = Slider(ax_phase, 'phase $\phi$', 0, np.pi, valfmt='%7.4g',valinit=(np.pi/2.))

def update_phase(val):
    """function to update the plot based on current slider_phase position"""
    phase = slider_phase.val # use slider position to set the phase
    y = np.sin(x + phase)
    plt.line.set_ydata(y) # make a line of the new y data
    plt.draw() # redraw the plot.

# if the slider posn is changed, update phase and recalculate
slider_phase.on_changed(update_phase)

plt.show()
