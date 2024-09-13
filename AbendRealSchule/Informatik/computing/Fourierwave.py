import numpy as np
import matplotlib.pyplot as plt

#def fourierfn(x,n):
  #  """ Returns a term in the fourier series for a square wave"""

lim= 25 # set number of terms/2 ( because series consits of only odd n terms) 

L=1 # set period of square wave 
x= np.linspace(0, 10, 1000) 

def fourierfcn(x):
   
    n=1
    fourier=0 
    while n <= lim :
        if n/2 *2 != n:
            new_term= (4/np.pi) * 1/n * np.sin((n*np.pi* x)/L)
            fourier= fourier + new_term          
            n=n+1
        else: 
            n=n+1 
    return fourier 
    
plt. plot( x, fourierfcn(x) )
plt.show()
 