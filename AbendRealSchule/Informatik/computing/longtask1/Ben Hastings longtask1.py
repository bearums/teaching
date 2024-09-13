#############################################################################
# A program to calculate the weighted line of least squares for linear data #
# Ben Hastings, 18/11/2013                                                  #
#############################################################################                

import numpy as np # must import relevant packages 
import matplotlib.pyplot as plt


#load data from experiment and plot data 
v,y,yerror  = np.loadtxt('N:\computing\longtask1\eovermdata.csv', delimiter=',',unpack=True) # load data from  experiment 
x= np.sqrt(v)
plt.errorbar(x,y,fmt='ro', yerr=yerror, ecolor="black", label='_nolegend_') # plot data with error bars that are coloured black and remove from legend
plt.xlabel( r'$\sqrt{V}$ / $\rm{V} ^ { \frac{1}{2}}$' , fontsize=14) # choose x axis label and fontsize. maths text generated using r' $\letter$ '. roman numeral V must be used to avoid V overlapping with 1/2 
plt.ylabel('r / m ', fontsize=14) # choose y axis label and fontsize
plt.title('Specific Charge of The Electron ', fontsize=20) # choose title of plot and fontize 
maxx=np.max (x) # find maximum value of x
maxy=np.max (y) # find maximum value of y 
xmin= np.min(x) # find  minimum value of x
ymin=np.min(y)  # find minimum value of y 
plt.xlim(0.8*np.min(x),1.1*np.max(x)) # crop x axis to values between fractions of minimum and maximum x values
plt.ylim(0.8*np.min(y),1.1*np.max(y)) # crop y axis to values between fractions of miniuum and maximum x values


###########################unweighted best fit line
 #calculate m
meanx= np.mean(x) # calculate mean of x values
meany=np.mean(y) # calculate mean of y values
nx=len(x) # count number of x values
ny=len(y) # count number of y values 
nmtr=np.sum(x*(y- meany)) # calculate numerator of m
dmtr=np.sum(x*(x-meanx)) # calculate denominator 
m= nmtr/dmtr # calculate m by division of numerator by denominator 

# calcaulte c
c= meany-(m*meanx) # calculate c value 

# create data for line of beat fit
regx=np.linspace (0,1.5*maxx,100) # create 100 x values ranging from 0 to 1.5 times the maximum x value of experiment data, 
regy= m*regx + c # create y values according to y=mx +c 

#m error
D= np.sum((x-meanx)**2)
sumdi= np.sum((y-m*x-c)**2)
merror= np.sqrt((sumdi/D)/(nx-2)) 

#cerror
cerror=np.sqrt((nx**-1 + (meanx**2/D))* (sumdi/(nx-2)))

################################## weighted best fit line 
# calculate w_m
w= 1/(yerror**2) # calculate weight for each error 
sumw=np.sum(w)
delta=(sumw* np.sum(w*x*x))- ((np.sum(w*x))*np.sum(w*x)) # denominator in expression for weighted m ( abbreviated to delta)
w_nmtr=(sumw *np.sum(w*x*y))- (np.sum(w*x)*np.sum(w*y)) # numerator in expression for weighted m 
w_m= w_nmtr/delta # perform division to compute w_m 

#calculate w_c
w_c= ((np.sum(w*x*x)*np.sum(w*y))- (np.sum(w*x)*np.sum(w*x*y)))/delta 

# create data weighted best fit line. Note x values have been generated in code at line 34
w_regy= w_m* regx + w_c 

# calculate w_m error
w_merror= np.sqrt( sumw/delta)

#calculate c_m error
c_merror= np.sqrt( np.sum(w*x*x)/delta)

# plot best fit lines 
plt.plot( regx,regy, "blue", label='unweighted line') # plot unweighted line  with a blue line and set name for legend 
plt.plot(regx, w_regy, "green", label='weighted line') # plot weighted line with a green line and set name for legend 
plt.legend ( loc='lower right') # show legend in lower right of plot  
plt.show() # displays the plot 

# calculating e/m values

B= 1.28e-3 # set value for magnetic field strength. Units- Tesla
r2=np.sqrt(2) #create label for root 2 

# unweighted line result
em= ((r2/B)/m)**2  

#weighted line result
wem= ((r2/B)/w_m)**2 


# output to console results 
print 'unweighted line :- '
print 'y=', m, 'x +', c
print 'gradient error=', merror
print 'y intercept error=', cerror
print' ' #make a blank line to space out text 
print 'weighted line :- '
print 'y=',w_m, 'x +',c
print 'gradient error=',w_merror
print 'y intercept error=', c_merror 
print '' # make blank line
print 'e/m as calculated from unweighted line=', em, 'C/kg'
print '' # make blank line
print 'e/m as calculated from weighted line=', wem, 'C/kg'

