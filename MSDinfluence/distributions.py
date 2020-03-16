
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

Nsteps = 10000
D = 1e-3
tau = 1

sig3 = np.sqrt(4*D*tau)*3

dx = np.random.normal(0,np.sqrt(2*D*tau),Nsteps)
dy = np.random.normal(0,np.sqrt(2*D*tau),Nsteps)
dr = np.sqrt(dx**2 + dy**2)

dx_hist = np.histogram(dr,bins=int(np.sqrt(Nsteps)),range=(0,sig3))
xvals = (dx_hist[1][1:] + dx_hist[1][:-1])/2
bwidth = (dx_hist[1][1:] - dx_hist[1][:-1]).mean()

print("*"*72)
print("Diff const: {:}".format(D))
print("bin width: {:}".format(bwidth))
print("# bins:    {:}".format(len(dx_hist[0])))
print("# steps:   {:}".format(dx_hist[0].sum()))

def gauss(x,D,N):
    tau = 1
    return N/np.sqrt(4*np.pi*D*tau)*np.exp(-x**2/(4*D*tau))

def radial(x,D,N):
    tau = 1
    return N*x/(2*D*tau)*np.exp(-x**2/(4*D*tau))

popt,pcov = curve_fit(radial,xvals,dx_hist[0])
print("-"*40)
print("D fit:   {:}".format(popt[0]))
print("N fit:   {:}".format(popt[1]/bwidth))
print("*"*72)

plt.bar(xvals,dx_hist[0],width=bwidth*0.7)
plt.plot(xvals,radial(xvals,popt[0],popt[1]))
plt.show()
