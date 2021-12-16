import sys, os, numpy as np, matplotlib.pyplot as plt

with open(os.path.join(sys.path[0], "input.txt")) as file:
    data = file.read().split("\n")
    notepad = {}
    for row in data:
        notepad[row.partition(" | ")[0]] = row.partition(" | ")[2]

print (notepad)
