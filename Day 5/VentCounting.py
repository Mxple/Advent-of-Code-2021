import os, sys
with open(os.path.join(sys.path[0], "input.txt")) as file:
    data = file.read()

data = data.split("\n")
newList = []
for line in range(len(data)):
    data[line] = data[line].replace("->", "").replace(",", " ").split()
    newList.append([(int(data[line][0]),int(data[line][1])),(int(data[line][2]),int(data[line][3]))])
cardinal = newList

for vector in range(len(cardinal)-1,-1,-1):
    if cardinal[vector][0][0] == cardinal[vector][1][0]:    #check x coords
        if cardinal[vector][0][1] < cardinal[vector][1][1]: #check for greater y value
            for i in range(cardinal[vector][0][1]+1, cardinal[vector][1][1]):
                cardinal[vector].insert(len(cardinal[vector])-1,(cardinal[vector][0][0],i))
        else:
            for i in range(cardinal[vector][0][1]-1, cardinal[vector][1][1],-1):
                cardinal[vector].insert(1,(cardinal[vector][0][0],i)) 
    elif cardinal[vector][0][1] == cardinal[vector][1][1]:  #check y coords
        if cardinal[vector][0][0] < cardinal[vector][1][0]: #check for greater x value
            for i in range(cardinal[vector][0][0]+1, cardinal[vector][1][0]):
                cardinal[vector].insert(len(cardinal[vector])-1,(i,cardinal[vector][0][1]))
        else:
            for i in range(cardinal[vector][0][0]-1, cardinal[vector][1][0],-1):
                cardinal[vector].insert(1,(i,cardinal[vector][0][1])) 
    else:                                                   #diagonal
        if cardinal[vector][0][0] < cardinal[vector][1][0]:         #if true, going right
            if cardinal[vector][0][1] < cardinal[vector][1][1]:     #up right 
                for i in range(1,cardinal[vector][1][0]-cardinal[vector][0][0]):
                    cardinal[vector].insert(len(cardinal[vector])-1,(cardinal[vector][0][0]+i,cardinal[vector][0][1]+i))
            else:                                           #down right 
                for i in range(1,cardinal[vector][1][0]-cardinal[vector][0][0]):
                    cardinal[vector].insert(len(cardinal[vector])-1,(cardinal[vector][0][0]+i,cardinal[vector][0][1]-i))
        else:                                               #if true, going left
            if cardinal[vector][0][1] < cardinal[vector][1][1]:     #up left 
                for i in range(1,cardinal[vector][0][0]-cardinal[vector][1][0]):
                    cardinal[vector].insert(len(cardinal[vector])-1,(cardinal[vector][0][0]-i,cardinal[vector][0][1]+i)) 
            else:                                           #down left
                for i in range(1,cardinal[vector][0][0]-cardinal[vector][1][0]):
                    cardinal[vector].insert(len(cardinal[vector])-1,(cardinal[vector][0][0]-i,cardinal[vector][0][1]-i)) 

grid = {}
for v in cardinal:
    for pt in v:
        if pt not in grid.keys():
            grid[pt]=1
        else:
            grid[pt]+=1

dangerSpots = 0
for i in grid.values():
    if i>1:
        dangerSpots+=1
        
with(open(os.path.join(sys.path[0], "results.txt"), "w")) as results:
    for v in cardinal:
        print(v ,file = results)
print(dangerSpots)