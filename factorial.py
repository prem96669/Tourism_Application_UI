import sys
from timeit import Timer
import csv
import matplotlib.pyplot as plt

sys.setrecursionlimit(150000)

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n*fact(n-1)
values = []
times = []
with open("C:/Users/premk/Desktop/values.txt", 'r') as f:
    for n in f:
        t = Timer(lambda: fact(int(n)))
        print(t.timeit(number=1))
        time = t.timeit(number=1)
        values.append(int(n))
        times.append(time)
    plt.plot(values, times)
    plt.show()

