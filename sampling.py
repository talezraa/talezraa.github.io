
import numpy as np
import matplotlib.pyplot as plt
########

def find_nearest(array, value): # finds index of element in array closest to a specific value
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return abs(idx-1)

def sampling(f,a,b,size=1): # returns random nb between a and b following f pdf ( normalized)
    x = np.linspace(a,b,1000)  
    CDF=np.zeros(x.shape)
    for k in range(1,x.shape[0]):  # computes CDF by Riemann integration
        dx=x[k]-x[k-1]
        CDF[k]=CDF[k-1]+f(x[k]-dx/2)*dx
    def inv_CDF(y): # returns x(CDF)
        return x[find_nearest(CDF,y)]
    uniform = np.random.random(size=size) #(b-a)*np.random.random(size=size)+a
    return np.array([inv_CDF(k) for k in uniform])
#######

f = lambda x :np.exp(-x**2/2)/np.sqrt(2*np.pi)
a=-3
b=3
size =1000
x=np.linspace(a,b,size)
plt.hist(sampling(f,a,b,size =size),density = True,bins=20)
plt.plot(x,f(x),label='pdf')
plt.legend()
plt.show()