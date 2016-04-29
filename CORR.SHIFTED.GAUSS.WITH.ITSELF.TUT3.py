#                                       TUTORIAL 3

#QUESTION 3:corrilation of shifted Gaussian function with its self using the results from 1 and 2.



from numpy import exp, real, pi, complex, linspace, arange,conj
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def conv(gaus,hln):
    gaus_ft = fft(gaus)
    return real(ifft(gaus_ft*hln))


x = linspace(-20,20,200)
sigma = 0.5; N = len(x); dx = 50; p = arange(N);c = complex(0,1)
gaus = exp(-0.5*x**2/sigma**2)
hln = exp(2*pi*c*p*dx/N)
l = conv(gaus,hln)
plt.plot(x,l,'b')
T = conv(gaus,hln)
def corr(l,T):
    ft = fft(l)
    conju = conj(fft(T))
    return ifft(ft*conju)


H = corr(l,T)
H1 = real(H)
plt.plot(x,H1,'r')
plt.grid(True)
plt.title('Correlation of shifted Gaussian function with itself')
plt.show()




#QUESTION: 3(B):

#ANSWER: The corrilation does not really depend on the shift because the corrilation of a shifted function is the same as the corrilation of a #        function which has not been shifted.
