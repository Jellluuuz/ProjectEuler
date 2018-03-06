import math
import time


def choose_function(n,r):
    return math.factorial(n)/(math.factorial(r)* math.factorial(n-r))

c = 0
for i in range(23,101):
    for j in range(i):
        if choose_function(i, j) > 1000000:
            c += 1

print c

