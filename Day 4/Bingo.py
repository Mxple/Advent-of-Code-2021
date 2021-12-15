import os, sys
file = open(os.path.join(sys.path[0], "input.txt"), "r")
data = file.read()
file.close()

#list of order in which numbers are called
calls = data[:289].split(",")

rows = data[291:].split("\n")
tables = []
temp = []

#tables is a list of lists where each smaller list represents a table with its contents being rows ie
#[' 9 38  6 58 99', '89 69 96 33 73', '26 20 32 12 27', '67 29 79 81 59', '66 45 24 36 68'] -->
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
        temp.append(row)

#flips on diagonal:
# [' 9 38  6 58 99'       [' 9 89 26 67 66'
#  '89 69 96 33 73'        '38 69 20 29 45'
#  '26 20 32 12 27'   -->  ' 6 96 32 79 24'
#  '67 29 79 81 59'        '58 33 12 81 36'
#  '66 45 24 36 68']       '99 73 27 59 68']
def transpose(lst):
    temp = []
    for row in range(len(lst)):
        temp.append([int(s) for s in lst[row].split() if s.isdigit()])
    for row in temp:
        for i in range(len(temp[0])):
            

