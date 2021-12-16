import sys, os, numpy as np, matplotlib.pyplot as plt

with open(os.path.join(sys.path[0], "input.txt")) as file:
    data = file.read().split("\n")
    notepad = {}
    for row in data:
        notepad[row.partition(" | ")[0]] = row.partition(" | ")[2]

#returns true if string a is inside string b regardless of order. returns char otherwise
def inside(a, b):
    for i in a:
        if i not in b:
            return i
    return True

#returns true if all elements of a string are in another and vise versa. length doesn't matter.
def same(a, b):
    for i in a:
        if i not in b:
            return False
    for j in b:
        if j not in a:
            return False
    return True

def toDigits(key, puzzle):
    keys = key.split()
    puzzles = puzzle.split()
    a=b=c=d=e=f=g=zero=one=two=three=four=five=six=seven=eight=nine = ""

    for k in keys:
        if len(k) == 2:
            one = k
        if len(k) == 3:
            seven = k
        if len(k) == 4:
            four == k
        if len(k) == 7:
            eight = k

    a = inside(seven,one)

    for k in keys:
        if len(k) == 5:
            if inside(one, k):
                three = k
    for k in keys:
        if same(k,three+four):
            nine = k

    e = inside(eight,nine)
    g = inside(nine,four+seven)

    b = inside(eight, three+e+g)
    for k in keys:
        if same(e+g+b+seven,k):
            zero = k

    d = inside(eight,zero)
    for k in keys:
        if len(k)==6 and same(k,zero) and same(k,nine):
            six = k
    c = inside(eight,six)
    f = inside(one, c)

    enigma = {
        a:"a",
        b:"b",
        c:"c",
        d:"d",
        e:"e",
        f:"f",
        g:"g"
    }

    decoded = []
    for p in puzzles:
        temp = ""
        for char in p:
           temp += enigma[char]
        decoded.append(temp)


    map = ["abcefg","cf","acdfg","bcdf","abdfg","abdfg","abdefg","acf","abcdefg","abcdfg"]
    result = []
    for d in range(len(decoded)):
        for i in range(len(map)):
            if same(puzzles[d],map[i]):
                result.append(i)
    return result


display = []
for item in notepad.items():
    display.append(toDigits(item[0],item[1]))
print(display)