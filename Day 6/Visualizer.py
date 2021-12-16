import os, sys, numpy as np, matplotlib.pyplot as plt

with open(os.path.join(sys.path[0],"results.txt"),"r") as file:
    data = file.read().replace("[","").replace("]","").split("\n")
    
chart = []
for row in data:
    chart.append([int(s) for s in row if s.isdigit()])
chart.pop()

for c in range(len(chart)):
    while len(chart[c]) != len(chart[-1]):
        chart[c].append(-1)

a = np.array(chart)
a=a.transpose()
plt.imshow(a, cmap='bone_r', interpolation='nearest',aspect = "auto")
plt.gca().invert_yaxis()
plt.show()
