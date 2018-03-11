import numpy as np
import time
import itertools

t = time.time()

# create probability distribution for Peter
p = {}
for i in range(9,37):
    p[i] = 0
lst = list(itertools.product([1,2,3,4], repeat=9))
for i in lst:
    p[sum(i)] += 1

for i in p:
    p[i] /= float(4**9)

# create probability distribution for Colin
c = {}
for i in range(6,37):
    c[i] = 0
lst = list(itertools.product([1,2,3,4,5,6], repeat=6))
for i in lst:
    c[sum(i)] += 1

for i in c:
    c[i] /= float(6**6)

#calculate p > c
total_chance = 0
for i in range(9,37):
    for j in range(6,i):
        total_chance += p[i] * c[j]

print total_chance
print time.time() - t