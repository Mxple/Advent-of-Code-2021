import os, sys, numpy as np, matplotlib.pyplot as plt
from matplotlib import animation

with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    data = file.read().split("\n")

grid = []
for d in range(len(data)):
    grid.append([int(i) for i in data[d] if i.isdigit()])

grid = np.array(grid)

# grid = np.random.randint(9, size = (10,10))
# print(grid)

s=0
def step():
    result = 0
    global grid
    grid += 1
    flashed = []
    prev = -1
    while len(flashed) > prev:
        prev = len(flashed)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 10 and (i,j) not in flashed:
                    flashed.append( (i,j) )
                    #region
                    #corners
                    if (i,j) == (0,0):
                        grid[i+1][j] += 1
                        grid[i][j+1] += 1
                        grid[i+1][j+1] += 1
                    elif (i,j) == (0,len(grid[i])-1):
                        grid[i+1][j] += 1
                        grid[i][j-1] += 1
                        grid[i+1][j-1] += 1
                    elif (i,j) == (len(grid)-1,0):
                        grid[i-1][j] += 1
                        grid[i][j+1] += 1
                        grid[i-1][j+1] += 1
                    elif (i,j) == (len(grid)-1,len(grid[i])-1):
                        grid[i-1][j] += 1
                        grid[i][j-1] += 1
                        grid[i-1][j-1] += 1
                    #sides
                    elif i == 0:
                        grid[i][j+1] += 1
                        grid[i][j-1] += 1
                        grid[i+1][j-1] += 1
                        grid[i+1][j] += 1
                        grid[i+1][j+1] += 1
                    elif i == len(grid)-1:
                        grid[i][j+1] += 1
                        grid[i][j-1] += 1
                        grid[i-1][j-1] += 1
                        grid[i-1][j] += 1
                        grid[i-1][j+1] += 1
                    elif j == 0:
                        grid[i-1][j] += 1
                        grid[i+1][j] += 1
                        grid[i-1][j+1] += 1
                        grid[i][j+1] += 1
                        grid[i+1][j+1] += 1
                    elif j == len(grid[i])-1:
                        grid[i-1][j] += 1
                        grid[i+1][j] += 1
                        grid[i-1][j-1] += 1
                        grid[i][j-1] += 1
                        grid[i+1][j-1] += 1
                    #mid
                    else:
                        grid[i-1][j-1] += 1
                        grid[i-1][j] += 1
                        grid[i-1][j+1] += 1
                        grid[i][j-1] += 1
                        grid[i][j+1] += 1
                        grid[i+1][j-1] += 1
                        grid[i+1][j] += 1
                        grid[i+1][j+1] += 1
                    #endregion
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 10:
                grid[i][j] = 0
                result += 1
    return result


color = "inferno"
fig = plt.figure()
plt.imshow(grid, cmap=color, interpolation='nearest', origin="lower", aspect = "equal")

def init():
    plt.cla()
    plt.imshow(grid, cmap=color, interpolation='nearest', origin="lower", aspect = "equal")
    plt.colorbar()
    plt.title(0)


def animate(i):
    plt.cla()
    global s
    s+=1
    step()
    plt.imshow(grid, cmap=color, interpolation='nearest', origin="lower", aspect = "equal")
    plt.title(s)
anim = animation.FuncAnimation(fig, animate, init_func = init, repeat = False, interval = 1)
plt.show()