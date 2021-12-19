import os, sys, numpy as np
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    data = file.read().split("\n")

grid = []
for d in range(len(data)):
    grid.append([int(i) for i in data[d] if i.isdigit()])

grid = np.array(grid)

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

def array_in_seq(array, seq):
    return any(np.all(array == each) for each in seq)
    
#Part 1
# result = 0
# for i in range(100):
#     result += step()
# print (result)
memory = []
syncro = 1

grids = open(os.path.join(sys.path[0],"grids.txt"), "w") 
memoryresults = open(os.path.join(sys.path[0],"memoryresults.txt"), "w") 

while step() != len(grid) * len(grid[0]):
    syncro += 1
    print(grid, file = grids)
    memory.append(grid)
print(memory, file = memoryresults)
print(syncro)

grids.close()
memoryresults.close()