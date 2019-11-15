from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Function Definition
def funct(x,a,b):
    return b - a*x**2

#Parameters and X and Y calculation
a = 3
b = 40
x = (np.arange(101)/101*2 - 1)*5
x += np.random.normal(0,0.3,len(x))
x = np.sort(x)
y = funct(x,a,b)
y += np.random.normal(0,4,len(y))

#Fitting of the function
popt,pcov = curve_fit(funct,x,y)
print(pcov)
print()

#R^2 = 1 - SS_res/SS_tot
ssres = np.sum((y-funct(x,popt[0],popt[1]))**2)
sstot = np.sum((y - y.mean())**2)
rsquared = 1 - ssres/sstot

#pearson correlation coefficient
#X = "y data"; Y = "fitted y data"
#pcc = (E[XY] - E[X] E[Y])/(std(X) std(Y))
#R^2 = pcc^2
expectXY = np.mean(y*(funct(x,popt[0],popt[1])))
expectX = np.mean(y)
expectY = np.mean(funct(x,popt[0],popt[1]))
stdX = np.std(y)
stdY = np.std(funct(x,popt[0],popt[1]))
pcc = (expectXY - expectX*expectY)/(stdX*stdY)

#t-test/ or maybe z-test with std~~poptulation std??
ymean = np.mean(y) - np.mean(funct(x,popt[0],popt[1]))
ystd = np.std(y)

tval = ymean/ystd/np.sqrt(len(x))

#Output comparison
print("===============")
print("Starting Values: a = {:} b = {:}".format(a,b))
print("Fit Values: a = {:0.04f} b = {:0.02f}".format(popt[0],popt[1]))
print("===============")
print()
print("===============")
print("Fit Errors (1STD): da = {:0.06f} db = {:0.04f}".format(*np.sqrt(np.diag(pcov))))
print("R-squared Value: R^2 = {:0.03f}".format(rsquared))
print("Pearson Correlation Coefficient:  pcc = {:0.04f}".format(pcc))
print("Data R-squared value:  pcc^2 = {:0.04f}".format(pcc**2))
print("===============")
print("One sample t-test: t = {:}".format(tval))
print("===============")


#Plot data and fit
plt.plot(x,y,'mo')
plt.plot(x,funct(x,popt[0],popt[1]))
plt.show()

