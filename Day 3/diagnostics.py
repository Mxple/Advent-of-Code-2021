import os, sys
file = open(os.path.join(sys.path[0], "input.txt"), "r")
data = file.read().split()
file.close()

#input a list of binary digits (list, leastcommon = False)
def findCommonBinary(lst,leastCommon=False):
    total = 0
    for digit in lst:
        total += int(digit)
    if (total >= len(lst)/2):
        if leastCommon:
            return (0)
        return (1)
    else:
        if leastCommon:
            return (1)
        return (0)

#returns a column of a list (list, colIndex)
def extractColumn(lst, colIndex):
    column = []
    for row in lst:
        column.append(row[colIndex])
    return column

#destroys every entry of a list which the coords are not equal to the condition (lst, column, value)
def parseList(lst, column, value):
    newList = []
    for i in range(len(lst)):
        if lst[i][column] == value:
            newList.append(lst[i])
    return newList

#takes a binary number in the form of a string and decimalizes it
def toDecimal(binary):
    binary = binary[::-1]
    result = 0
    for i in range(0,len(binary)):
        result += (2**(i))*int(binary[i])
    return result

#part 1
gamma = ""
elipson = ""

for i in range(len(data[0])):
    col = extractColumn(data, i)
    mode1 = findCommonBinary(col)
    mode2 = findCommonBinary(col, True)
    gamma += str(mode1)
    elipson += str(mode2)

print(toDecimal(gamma)*toDecimal(elipson))

#part 2
o2rating = data
for i in range(len(o2rating[0])):
    col = extractColumn(o2rating, i)
    mode = findCommonBinary(col)
    o2rating = parseList(o2rating, i, str(mode))
    if len(o2rating) == 1:
        break

co2rating = data
for i in range(len(co2rating[0])):
    col = extractColumn(co2rating, i)
    mode = findCommonBinary(col, True)
    co2rating = parseList(co2rating, i, str(mode))
    if len(co2rating) == 1:
        break
    
print(toDecimal(co2rating[0])*toDecimal(o2rating[0]))