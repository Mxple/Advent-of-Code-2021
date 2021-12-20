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
print(map)
def getPaths(node, visited,path=[]):
    paths = 0
    if node == "end":
        path.append('end')
        print(path)
        return 1
    if node in visited:
        return 0
    path.append(node)
    if node.islower():
        visited.append(node)
    for branch in map[node]:
        paths += getPaths(branch, visited,path)
    return paths


print(getPaths("start",[]))
