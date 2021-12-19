import os, sys, numpy as np, matplotlib.pyplot as plt, mpl_toolkits.mplot3d  

with open(os.path.join(sys.path[0], "input.txt"),"r") as file:
    data = file.read().split()
for d in range(len(data)):
    data[d] = [int(s) for s in data[d] if s.isdigit]

grid = np.array(data)

#region check low points
lowpts = []
lowptsIndicies = []
#corners:
if grid[0][0] < grid[1][0] and grid[0][0] < grid[0][1]:
    lowpts.append(grid[0][0])
    lowptsIndicies.append((0,0))
if grid[0][len(grid[0])-1] < grid[1][len(grid[0])-1] and grid[len(grid[0])-1][0] < grid[0][len(grid[0])-2]:
    lowpts.append(grid[0][len(grid[0])-1])
    lowptsIndicies.append((0,len(grid[0])-1))
if grid[len(grid[0])-1][0] < grid[len(grid[0])-2][0] and grid[len(grid[0])-1][0] < grid[len(grid[0])-1][1]:
    lowpts.append(grid[len(grid[0])-1][0])
    lowptsIndicies.append((len(grid[0])-1,0))
if grid[len(grid[0])-1][len(grid[0])-1] < grid[len(grid[0])-2][len(grid[0])-1] and grid[len(grid[0])-1][len(grid[0])-1] < grid[len(grid[0])-1][len(grid[0])-2]:
    lowpts.append(grid[len(grid[0])-1][len(grid[0])-1])
    lowptsIndicies.append((len(grid[0])-1,len(grid[0])-1))

#edges
for i in range(1,len(grid[0])-1):   #horiz
    if grid[0][i]<grid[0][i-1] and grid[0][i]<grid[0][i+1] and grid[0][i]<grid[1][i]:
        lowpts.append(grid[0][i])
        lowptsIndicies.append((0,i))
    if grid[len(grid)-1][i]<grid[len(grid)-1][i-1] and grid[len(grid)-1][i]<grid[len(grid)-1][i+1] and grid[len(grid)-1][i]<grid[len(grid)-2][i]:
        lowpts.append(grid[len(grid)-1][i])
        lowptsIndicies.append((len(grid)-1,i))
     #vert
    if grid[i][0]<grid[i-1][0] and grid[i][0]<grid[i+1][0] and grid[i][0]<grid[i][1]:
        lowpts.append(grid[i][0])
        lowptsIndicies.append((i,0))
    if grid[i][len(grid)-1]<grid[i-1][len(grid)-1] and grid[i][len(grid)-1]<grid[i+1][len(grid)-1] and grid[i][len(grid)-1]<grid[i][len(grid)-2]:
        lowpts.append(grid[i][len(grid)-1])
        lowptsIndicies.append((i,len(grid-1)))

for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i+1][j] and grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i][j+1]:
            lowpts.append(grid[i][j])
            lowptsIndicies.append((i,j))
#endregion
result = 0
for i in lowpts:
    result += 1+i
print(result)
print(lowptsIndicies)

#takes a low point, returns the basin size
def getBasinSize(coordinate, grid):
    for g in range(len(grid)):
        grid[g][grid[g] < 9] = 0
    h,w = len(grid), len(grid[0])
    visited = set()
     
    def flood(x, y, old = 0, new = -1):
        if x < 0 or y < 0 or x >= h or y >= w or (x,y) in visited or grid[x][y] != old:
            return
        grid[x][y] = new
        visited.add( (x,y) )

        flood(x+1,y)
        flood(x-1,y)
        flood(x,y+1)
        flood(x,y-1)
    #end of flood function
    flood(coordinate[0],coordinate[1])
    return (len(visited))

basinsizes = []
for i in lowptsIndicies:
    basinsizes.append(getBasinSize(i,grid))
basinsizes.sort(reverse=True)
print(basinsizes[0]*basinsizes[1]*basinsizes[2])