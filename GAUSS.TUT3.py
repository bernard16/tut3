#                                        TUTORIAL 3

#QUESTION 1(B):Plot a gaussian that started in the centre of the array shifted by half the array length.

#ANSWER:




import numpy as km
from matplotlib import pyplot as plt
def convl(f,hln):
    ft = km.fft.fft(f)
    return km.real(km.fft.ifft(ft*hln))

x = km.linspace(-20,20,500)
cgm = 0.5
f= km.exp(-0.5*x**2/cgm**2)
N = len(x)
L = km.arange(N)
J = km.complex(0,1)
dx = len(x)/2
hln = km.exp(-2*km.pi*J*L*dx/N)
h = convl(f,hln)

plt.plot(x,f,'b')
plt.plot(x,h,'r')
plt.grid(True)
plt.title('Gaussian half shifted')
plt.show()
