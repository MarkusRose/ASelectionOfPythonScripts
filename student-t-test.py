import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def modelfun(x,alpha,beta):
    return alpha + beta * x + np.random.normal(loc=0,scale=10,size=len(x))

def linfun(x,alpha,beta):
    return alpha + beta * x

a = 1
b = 2
x = np.arange(10)
y = modelfun(x,a,b)

popt,pcov = curve_fit(linfun,x,y)
yfit = linfun(x,popt[0],popt[1])

e_res = (y-yfit)

ss_res = (e_res**2).sum()
print("Sum Squared Residuals: {:}".format(ss_res))

beta0 = 0

t_score = (popt[1]-beta0)*np.sqrt(len(x)-2)/np.sqrt(ss_res/((x-x.mean())**2).sum())
chi_squared = (e_res**2/yfit).sum()
r_squared = 1 - (e_res**2).sum()/((y-y.mean())**2).sum()
print("t-test score: {:}".format(t_score))
print("chi squared: {:}".format(chi_squared))
print("R squared: {:}".format(r_squared))

fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(111)
ax.plot(x,y,'o')
ax.plot(x,yfit,'-')
plt.show()


