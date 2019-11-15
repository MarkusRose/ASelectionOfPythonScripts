import numpy
import pandas
import matplotlib.pyplot as plt
import random

N = 90000

sp = [[0., 50., 100.],[0., 50.,0.]]



coords = [[],[]]
x = random.random()*100
y = random.random()*50
coords[0].append(x)
coords[1].append(y)

for i in range(N):
    roll = random.randint(0,2);
    x += (sp[0][roll] - x)/2.
    y += (sp[1][roll] - y)/2.
    coords[0].append(x)
    coords[1].append(y)


plt.plot(coords[0],coords[1],'y-')
plt.plot(coords[0],coords[1],',')
plt.show()
