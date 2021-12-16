import os, sys

from types import DynamicClassAttribute
file = open(os.path.join(sys.path[0], "input.txt"), "r")
data = file.read()
file.close()

#list of order in which numbers are called
calls = data.partition('\n')[0].split(",")
rows = data.partition('\n\n')[2].split("\n")
calls = [int(x) for x in calls]
tables = []
temp = []
#tables is a list of lists of list where each middle list represents a table with its contents being lists ie:
#[[9, 38, 6, 58, 99], [89, 69, 96, 33, 73], [26, 20, 32, 12, 27], [67, 29, 79, 81, 59], [66, 45, 24, 36, 68]] -->
#  9 38  6 58 99
# 89 69 96 33 73
# 26 20 32 12 27
# 67 29 79 81 59
# 66 45 24 36 68
for row in rows:
    if row == "":
        tables.append(temp)
        temp = []
    else:
        temp.append([int(s) for s in row.split() if s.isdigit()])
tables.append(temp)
#flips on diagonal:
#[[9, 38, 6, 58, 99],           [[9, 89, 26, 67, 66], 
# [89, 69, 96, 33, 73],         [38, 69, 20, 29, 45],
# [26, 20, 32, 12, 27],  -->    [6, 96, 32, 79, 24],
# [67, 29, 79, 81, 59],         [58, 33, 12, 81, 36],
# [66, 45, 24, 36, 68]]         [99, 73, 27, 59, 68]]
def transpose(lst):
    temp = []
    result = []
    for i in range(len(lst[0])):
        for row in lst:
            temp.append(row[i])
        result.append(temp)
        temp = []
    return result

class Bingo:
    def __init__(self, lst, lstT):
        self.rows = lst
        self.cols = lstT
    def turn(self, num):
        for r in range(len(self.rows)):
            self.rows[r]=[0 if x == num else x for x in self.rows[r]]
        for c in range(len(self.cols)):
            self.cols[c]=[0 if x == num else x for x in self.cols[c]]
    def checkWin(self):
        for r in self.rows:
            if       (r == [0,0,0,0,0]):
                return (True)
        for c in self.cols:
            return (c == [0,0,0,0,0])
    def getScore(self, prev):
        result = 0
        for row in self.rows:
            for item in row:
                if item > 0:
                    result += item
        result *= prev
        return result

bingoBoards = []
for table in tables:
    bingoBoards.append(Bingo(table, transpose(table)))

#main loop
#part 1
winners = {}
for i in calls:
    for board in range(len(bingoBoards)):
        bingoBoards[board].turn(i)
        if bingoBoards[board].checkWin() and bingoBoards[board] not in winners.keys():
             winners[bingoBoards[board]] = [board, (calls.index(i), i), bingoBoards[board].getScore(i)]

results = list(winners.values())


print("index"+"\t|"+"rounds, num"+"\t|"+"score")
print("__________________________")
for i in range(len(results)):
    print(str(results[i][0])+"\t|"+str(results[i][1])+"\t|"+str(results[i][2]))