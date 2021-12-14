import os, sys

#part 1
def countIncrements(depthList):
    result = 0

    for i in range(1,len(depthList)):
        if int(depthList[i-1]) < int(depthList[i]):
            result += 1

    return result

#part 2
def threeMeasurementSlidingWindow(depthList):
    threeMeasureList = []
    
    for i in range(2,len(depthList)):
        threeMeasureList.append(int(depthList[i-2])+int(depthList[i-1])+int(depthList[i]))

    return threeMeasureList

file1 = open(os.path.join(sys.path[0], "input.txt"), "r")
list1 = file1.read().split()
list2 = threeMeasurementSlidingWindow(list1)
file1.close()

print(countIncrements(list1))
print(countIncrements(list2))