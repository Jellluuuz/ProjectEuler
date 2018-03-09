import numpy as np
import math
import time

numbers = {}
for i in range(10**6):
    numbers[i] = 0

def one_step(i):
    sum = 0
    for char in str(i):
        sum += math.factorial(int(char))
    return sum

t = time.time()

for i in range(10**6):
    setting = True
    temp = i
    count = 0
    chain = []
    while setting:

        temp = one_step(temp)
        if temp not in chain:
            chain.append(temp)
        else:
            setting = False
    numbers[i] += len(chain) + 1


for i in range(10**6):
    if numbers[i] == 60:
        count += 1
print count
print time.time() - t