import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

print("Hello World!")



img = np.zeros((256,256))
lines = np.zeros((256,256))

ranges = np.arange(256)

for i in range(len(img)):
    img[i] += np.mod((ranges - i),256)


lines[np.mod(range(len(lines)),10)==0] = np.zeros((256)) + 255

centre = 256/2
radius = 20

circle = np.zeros(lines.shape)
for i in range(len(circle)):
    for j in range(len(circle[i])):
        if (i-centre)**2 + (j-centre) **2 < radius**2:
            circle[i,j] = 1

plt.imshow(np.clip(circle+lines,0,255))
plt.show()


