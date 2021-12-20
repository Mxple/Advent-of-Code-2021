import os, sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    data = file.read().replace("-"," ").splitlines()
print(data)
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
print(map)

def getPaths(startPos, visited = ["start"]):
    paths = 0
    if startPos == "end":
        return 1
    for next in map[startPos]:
        if next.islower():
            if next in visited:
                continue
            visited.append(next)
        else:
            paths += getPaths(next, visited)
    return paths

print(getPaths("start"))