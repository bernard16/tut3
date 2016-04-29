#                                       TUTORIAL 3


#QUESTION 4: Write a routine to take the convolution of two arrays *without* any danger of wrapping around(by adding zeros).

#ANSWER:


import numpy as km
from numpy import linspace,arange,real,cos,exp,conj,pi,insert
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
x = km.linspace(-pi*2,pi*2,200)
f = km.cos(x)
g = km.exp(-x)
f = insert(f,len(f),0)
f = insert(f,len(f),0)
g = insert(g,len(g),0)
g = insert(g,len(g),0)
ft = fft(f)
gt = fft(g)
conv = ifft(ft*gt)
plt.plot(real(conv))
plt.title('Convolution without wrapped around')
plt.grid(True)
plt.show()
