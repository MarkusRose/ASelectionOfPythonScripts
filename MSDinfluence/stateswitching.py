import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


states = []

p12 = 0.2
p21 = 0.3

p = np.array([[1-p12,p12],[p21,1-p21]])

statprob1 = p21/(p12+p21)
statprob2 = p12/(p12+p21)

for i in range(10000):

    if len(states) == 0:

        u = np.random.random()

        if u < statprob2:
            states.append(1)
        else:
            states.append(0)
    else:

        s0 = states[-1]
        s1 = (s0+1) % 2

        u = np.random.random()

        if u < p[s0,s1]:
            states.append(s1)
        else:
            states.append(s0)

print(np.array(states).sum()/len(states))

