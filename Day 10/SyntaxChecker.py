import os, sys, numpy as np

syntax = []
incomplete = []

with open(os.path.join(sys.path[0], "input.txt"),"r") as file:
    data = file.read().split()

#separates input file into a nested list with inner elements being an individual character
for line in data:
    syntax.append([char for char in line])

#map characters to numbers
map = {
    "(":3, ")":-3,
    "[":57, "]":-57,
    "{":1197, "}":-1197,
    "<":25137, ">":-25137
    }

#replaces charactesr with numbers (scores) as sepcified by the map
for r in range(len(syntax)):
    for c in range(len(syntax[r])):
        syntax[r][c] = map[syntax[r][c]]
        
#checks for corruption by adding openers( [ { <  and subtracting from the last opener depending on closer >}])
def isCorrupt(line: list):
    temp = []
    for l in line:
        if l > 0:
            temp.append(l)
        elif -1*l == temp[-1]:
            temp.pop(-1)
        else:
            return l
    return temp

#complestes the line by taking incomplete openers (temp) and closing them in order
def complete(line: list):
    temp = isCorrupt(line)
    temp.reverse()
    temp = [i*-1 for i in temp]
    return temp

#Part 1
result = 0
for line in syntax:
    if (type(isCorrupt(line)) == int):
        result -= isCorrupt(line)
    else:
        incomplete.append(line)
print(result)

#Part 2
result2 = []
for incomp in incomplete:
    score = 0
    for i in complete(incomp):
        score *= 5
        if i == -3:
            score += 1
        elif i == -57:
            score += 2
        elif i == -1197:
            score += 3
        else:
            score += 4
    result2.append(score)
result2.sort()
print(result2[len(result2)//2])