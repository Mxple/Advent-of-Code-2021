import os, sys
def findModeCol(lst):
    gamma = ""
    elipson = ""
    for i in range(len(lst[0])):
        temp = 0
        for binary in lst:
            temp += int(binary[i])
        if temp > len(lst)//2:
            gamma += ("1")
            elipson += ("0")
        else:
            gamma += ("0")
            elipson += ("1")
    return (int(gamma), int(elipson))

def toDecimal(binary):
    binary = str(binary)[::-1]
    result = 0
    for i in range(0,len(binary)):
        result += (2**(i))*int(binary[i])
    return result

file = open(os.path.join(sys.path[0], "input.txt"), "r")
data = file.read().split()
file.close()

diagnostic = findModeCol(data)
print(toDecimal(diagnostic[0])*toDecimal(diagnostic[1]))
