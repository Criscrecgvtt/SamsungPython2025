from timeit import *  # Import all classes and methods of timeit

dic = {0: 0, 1: 1}
def fibonacci_2(n):
    if n in dic:
        return dic[n]
    
    dic[n] = fibonacci_2(n - 1) + fibonacci_2(n - 2)
    return dic[n]

t2 = Timer("fibonacci_2(30)", "from __main__ import fibonacci_2")
print("fibonacci_2(30) * 20 times", t2.timeit(number=20), "seconds")

n = 45
for i in range(n):
    print(fibonacci_2(i),end=",")
