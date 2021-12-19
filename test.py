import os, sys, numpy as np

def array_in_seq(array, seq):
    return any(np.all(array == each) for each in seq)

seq=[]
for i in range(10):
    array = np.random.randint(9,size=(10,10))

    seq.append(array)
print(seq)