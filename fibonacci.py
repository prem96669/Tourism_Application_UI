import csv
from timeit import Timer
import matplotlib.pyplot as plt

def fibonacci_series(n): 
    a = 0
    b = 1
    while n >= 0:
        if n == 0: 
            return a 
        elif n == 1: 
            return b 
        else: 
            for i in range(2,n): 
                c = a + b 
                a = b 
                b = c 
            return b 

values = []
times = []
with open("C:/Users/premk/Desktop/values.txt", 'r') as f:
    plt.figure(1)
    for n in f:
        t = Timer(lambda: fibonacci_series(int(n)))
        time = t.timeit(number=1)
        values.append(int(n))
        times.append(time)
    plt.plot(values, times)
    print(values)
    print(times)
    plt.show()