import os, sys, numpy as np

with open(os.path.join(sys.path[0], "input.txt")) as file:
    data = file.read()
data = [int(i) for i in data.split(",") if i.isdigit]
#data is a list of integers, each representing the internal timer of a lanternfish
class Fish:
    def __init__(self, timer=8):
        self.timer = timer
    def elapseDay(self):
        if self.timer > 0:
            self.timer -= 1
            return False
        else:
            self.timer = 6
            return True

#starting batch
fishies=np.zeros(shape=(9,1))
for i in data:
    fishies[i]+=1

dayMatrix = np.zeros(shape=(9,9))
for i in range(8):
    dayMatrix[i][i+1] = 1
dayMatrix[6][0]=1
dayMatrix[8][0]=1

result = np.linalg.matrix_power(dayMatrix, 256).dot(fishies)
print(sum(result))

'''
for timer in data:
    fishies.append(Fish(timer))

f = open(os.path.join(sys.path[0], "results.txt"), "w")
temp = 0
for day in range(100):
    for fish in range(len(fishies)):
        if (fishies[fish].elapseDay()):
            fishies.append(Fish())
    print([int(i.timer) for i in fishies],file = f)
'''