import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x,m,sig,A=1):
    return np.exp(-(x-m)**2/(2*sig**2))*A

def airydisc(x,m,den):
    return (np.sin(np.pi*(x-m)/den)/(np.pi/den*(x-m)))**2

mean = 0
sig = 0.211
den = 0.61
xr = (np.arange(400)/400*2-1)*3+0.001

yairy = airydisc(xr,mean,den)
print(yairy)

popt,pcov = curve_fit(gaussian,xr,yairy)
print(popt)

plt.plot(xr,gaussian(xr,mean,sig),label=r"exp(-(x-m)^2/(2*sig^2))")
plt.plot(xr,airydisc(xr,mean,den),label=r"(sin(pi*(x-m)/den)/(pi/den*(x-m))^2")
plt.vlines([den,sig],0,1,'k')
plt.legend()
plt.show()
