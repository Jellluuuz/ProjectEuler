import time
numbers = []
import math


t = time.time()
for i in range(3, 10000000):
    S = 0
    for char in str(i):
        S += math.factorial(int(char))
    if S == i:
        numbers.append(i)

print numbers
print sum(numbers)

print time.time() - t