#                                                   TUTORIAL 3

#QUESTION 1(A).Write a function that will shift an array by an arbitrary amount using a convolution.


#ANSWER:



import numpy as km
from matplotlib import pyplot as plt
def convl(f,ab):
    ft = km.fft.fft(f)
    return km.real(km.fft.ifft(ft*ab))

x = km.linspace(-2*km.pi,2*km.pi,200)
f= km.cos(x)
N = len(x)
L = km.arange(N)
J = km.complex(0,1)
# now lets choose the arbitrary number/amount 
dx = 15.0
ab = km.exp(-2*km.pi*J*L*dx/N)
h = convl(f,ab)

plt.plot(x,f,'r')
plt.plot(x,h,'b')
plt.grid(True)
plt.title('cos function shift by pi/4')
plt.show()
