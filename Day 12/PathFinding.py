import os, sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    data = file.read().replace("-"," ").splitlines()

map = {}
for d in data:
    if d.split()[0] not in map:
        map[ d.split()[0] ] =  [ d.split()[1] ]
    else:
        map[d.split()[0]].append(d.split()[1])
    if d.split()[1] not in map:
        map[ d.split()[1] ] =  [ d.split()[0] ]
    else:
        map[d.split()[1]].append(d.split()[0])
map.pop("end")
for key, value in map.items():
    if "start" in value:
        value.remove("start")

def getPaths(node="start", visited=set()):
    paths = 0
    if node == "end":
        return 1
    if node in visited and node.islower():
        return 0
    for branch in map[node]:
        paths += getPaths(branch, visited | {node})
    return paths

def getPaths2(node="start", visited=set(), visitedTwice=set()):
    paths = 0
    if node == "end":
        return 1
    if node in visitedTwice and node.islower():
        return 0
    other = visitedTwice.copy()
    if node in visited:
        other.add(node)
    for branch in map[node]:
        paths += getPaths2(branch, visited | {node}, other)
    return paths

print(getPaths2())
