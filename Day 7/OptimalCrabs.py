#why are crab submarines limited to horizontal movement!!? and i guess they all share fuel... unless pt2 !!
import sys, os, numpy as np, matplotlib.pyplot as plt

with open(os.path.join(sys.path[0], "input.txt")) as file:
    data = [int(i) for i in file.read().split(",") if i.isdigit]

part2=True

diffs = []
for i in range(min(data),max(data)):
    temp = 0
    for d in data:
        if not part2:
            temp += (abs(i-d)) #part 1
        else:
            temp += sum(range((abs(i-d))+1)) #part 2
    diffs.append(temp)
print((min(diffs),diffs))


scatter = {}
for i in data:
    if i not in scatter.keys():
        scatter[i]=1
    else:
        scatter[i]+=1

plt.plot(range(0,1840),diffs)
plt.scatter(scatter.keys(),scatter.values())
plt.show()
