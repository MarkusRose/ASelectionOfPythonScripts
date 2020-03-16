import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit



xbins = (np.arange(101)-51)/50 * 3
xvals = (xbins[1:] + xbins[:-1])/2
wx = (xbins[1:] - xbins[:-1]).mean()

randsteps = np.random.normal(loc=0,scale=1,size=10000)
hist = np.histogram(randsteps,bins=xbins)

randsteps = np.random.normal(loc=1,scale=1,size=10000)
hist2 = np.histogram(randsteps,bins=xbins)

randsteps = np.random.normal(loc=2,scale=1,size=10000)
hist3 = np.histogram(randsteps,bins=xbins)

def gaussfunc(x,mu=0,A=1,sig=1):
    return A*np.exp(-(x-mu)**2/(2*sig**2))

popt1,pcov1 = curve_fit(gaussfunc,xvals,hist[0])
popt2,pcov2 = curve_fit(gaussfunc,xvals+1,hist2[0])
popt3,pcov3 = curve_fit(gaussfunc,xvals+2,hist3[0])
print(popt1)
print(popt2)
print(popt3)


f,ax = plt.subplots(1,2)
ax[0].bar(xvals,hist[0],width=wx,color='xkcd:orange')
ax[0].bar(xvals,hist2[0],width=wx,color='xkcd:dark blue')
ax[0].bar(xvals,hist3[0],width=wx,color='xkcd:red')
ax[1].plot(xvals,gaussfunc(xvals,popt1[0],popt1[1],popt1[2]),color='xkcd:orange')
ax[1].plot(xvals,gaussfunc(xvals,popt2[0],popt2[1],popt2[2]),color='xkcd:dark blue')
ax[1].plot(xvals,gaussfunc(xvals,popt3[0],popt3[1],popt3[2]),color='xkcd:red')
plt.show()
