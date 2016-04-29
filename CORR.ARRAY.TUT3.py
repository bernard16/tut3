#                                        TUTORIAL 3

#QUESTION 2(A): write a routine to take the correlation function of two arrays.

#ANSWER:

import numpy as km
from numpy import linspace,arange,real,cos,exp,conj,pi
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
x = km.linspace(-pi*2,pi*2,200)
f = km.cos(x)
g = km.exp(-x)
corr =km.fft.ifft(km.fft.fft(f)*km.conj(km.fft.fft(g)))
corr_real = km.real(corr)
plt.plot(x,corr_real,'r')
plt.title('Correlation of cos & exponential')
plt.grid(True)
plt.show()
