import os, sys, numpy as np, matplotlib.pyplot as plt

with open(os.path.join(sys.path[0],"results.txt"),"r") as file:
    data = file.read().replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").split()

coords = np.zeros(shape=(1000,1000))
for i in range(0,len(data),2):
    coords[int(data[i])][int(data[i+1])]+=1

plt.imshow(coords, cmap='magma', interpolation='nearest', origin="lower")
plt.show()