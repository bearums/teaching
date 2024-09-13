#######################################################
# A plot of data from an x-ray diffraction experiment #
# Ben Hastings, 01/11/2013                            #
#######################################################                

import numpy as np # must import relevant packages 
import matplotlib.pyplot as plt

#xlif,ylif = np.loadtxt('N:\computing\LiF-30kV.csv', delimiter=',',unpack=True) # load data from LiF experiment 
#xnacl, ynacl= np.loadtxt('N:\computing\NaCl-30kV.csv', delimiter=',', unpack=True) # load data from NaCl experiment
x= np.arange(2,16,1)
y=x**2 
y2= y/np.log(x)

plt.plot (x, y, 'k') # plot Lif data with a black line
plt.plot (x,y2, 'r')# plot NaCl data with a red line 

plt.xlabel('n', fontsize=14) # choose x axis label and fontsize. Greek letters generated using r' $\letter$ '
plt.ylabel('G(n) ', fontsize=14) # choose y axis label and fontsize
#plt.title('Xray Diffraction', fontsize=20) # choose title of plot and fontize 
plt.legend( [ 'n^2','NaCl-30kV']) # display a legend and choose legend text 


plt.show() # show the plot 