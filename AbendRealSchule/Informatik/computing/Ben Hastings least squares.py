####################################################################
# A program to calculate the line of least squares for linear data #
# Ben Hastings, 15/11/2013                                         #
####################################################################                

import numpy as np # must import relevant packages 
import matplotlib.pyplot as plt

#load data from experiment and plot data 
x,y,yerror  = np.loadtxt('N:\computing\Hall_effect_data.csv', delimiter=',',unpack=True) # load data from  experiment 
plt.errorbar(x,y,fmt='ro', yerr=yerror, ecolor="black") # plot data with error bars that are coloured black 
plt.xlabel('current / mA', fontsize=14) # choose x axis label and fontsize. Greek letters generated using r' $\letter$ '
plt.ylabel('voltage / V ', fontsize=14) # choose y axis label and fontsize
plt.title('Hall Effect ', fontsize=20) # choose title of plot and fontize 
#plt.show() # show the plot 

# calculate m
meanx= np.mean(x) # calculate mean of x values
meany=np.mean(y) # calculate mean of y values
nx=len(x) # count number of x values
ny=len(y) # count number of y values 

nmtr=np.sum(x*(y- meany)) # calculate numerator of m
dmtr=np.sum(x*(x-meanx)) # calculate denominator 
m= nmtr/dmtr # calculate m by division of numerator by denominator 

# calcaulte c
c= meany-(m*meanx) # calculate c value 
print 'gradient:', m   
print 'y intercept:', c 

# create data for line of beat fit
maxx=np.max (x) # find maximum value of x
maxy=np.max (y) # find maximum value of y 
xmin= np.min(x) # find  minimum value of x
ymin=np.min(y)  # find minimum value of y 
regx=np.linspace (0,maxx,100) # create 100 x values ranging from 0 to maximum x value of experiment data, 
regy= m*regx- c # create y values according to y=mx +c 


#m error
D= np.sum((x-meanx)**2)
sumdi= np.sum((y-m*x-c)**2)
merror= np.sqrt((sumdi/D)/(nx-2))
print 'error in gradient:', merror 

#cerror
cerror=np.sqrt((nx**-1 + (meanx**2/D))* (sumdi/(nx-2)))
print 'error in y intercept:', cerror 


#plot best fit line 
plt.plot( regx,regy, "blue") # plot line of best fit with a blue line 
plt.xlim(0.1*xmin,1.1*maxx) # crop x axis
plt.ylim(0.1*ymin,1.1*maxy) # crop y axis 
plt.text(4,0.16, "y = {0:0.4f} x + {1:0.4f}".format(m,c)) # display equation of line on plot
plt.show() # shows the plot 







