#                                       TUTORIAL 3


#QUESTION 2(B):Plot the correlation function of a Gaussian with itself.


#ANSWER:

from numpy import pi,exp,real,conj,linspace
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def corr(gaus):
    ft_gaus = fft(gaus)
    cj_gaus = conj(fft(gaus))
    return ifft(ft_gaus*cj_gaus)

y = linspace(-15,15,200)
sig = 0.5
gaus = exp(-0.5*y**2/sig**2)
h = corr(gaus)
m = real(h)
plt.plot(y,m)
plt.title('Correlation of Gaussian with itself')
plt.grid(True)
plt.show()


