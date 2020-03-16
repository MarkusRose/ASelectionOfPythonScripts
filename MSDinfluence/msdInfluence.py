import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

D = 1e-6 #um^2/s
tau = 1 #s
precision = 0.03

fitrange = 30
Nsingle = 10000
Ndouble = 0


dx = np.random.normal(0,np.sqrt(2*D*tau),Nsingle)
dy = np.random.normal(0,np.sqrt(2*D*tau),Nsingle)

dx2 = np.random.normal(0,np.sqrt(2*D*2*tau),Ndouble)
dy2 = np.random.normal(0,np.sqrt(2*D*2*tau),Ndouble)


displacements = []

count = 0
for i in range(len(dx)):
    displacements.append([1,dx[i],dy[i]])
    if Ndouble != 0 and count < Ndouble and i >= (len(dx)/Ndouble * (count+1)):
        displacements.append([2,dx2[count],dy2[count]])
        count += 1
displacements = np.array(displacements)
track = np.cumsum(displacements,axis=0)
track[:,1] += np.random.normal(0,precision,len(track))
track[:,2] += np.random.normal(0,precision,len(track))


def msdCalc(track):
    lagtimes = np.arange(300) + 1
    msd = []
    for lag in lagtimes:
        disp = track[lag:] - track[:-lag]
        ssd = disp[:,1]**2 + disp[:,2]**2
        msd.append([lag,ssd.mean(),ssd.std()/np.sqrt(len(disp)),len(disp)])

    return np.array(msd)

msdtrack = msdCalc(track)

def linear(x,a,b):
    return a + b * x

popt,pcov = curve_fit(linear,msdtrack[:fitrange,0],msdtrack[:fitrange,1])

sigma = 0.5*np.sqrt(popt[0] + popt[1]*tau/3)
print(popt[0],popt[1])
print("Diffusion coefficient = {:0.02e}".format(popt[1]/4))
print("Dynamic precision = {:0.02e}".format(sigma))
print("Static precision = {:0.02e}".format(sigma/np.sqrt((647/2/1.45)**2 + popt[1]*tau/4)))

plt.figure()
plt.subplot(121)
plt.errorbar(msdtrack[:,0],msdtrack[:,1],yerr=msdtrack[:,2])
plt.plot(msdtrack[:,0],linear(msdtrack[:,0],popt[0],popt[1]))
plt.subplot(122)
plt.plot(track[:,1],track[:,2])
plt.show()
        

    

    



    
