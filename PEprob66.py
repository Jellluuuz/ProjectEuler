import time
import math
import gmpy

##iets met continued fractioned van D

def find_minimal_sol(n):
    j = 1
    while True:
        i_2 = 1 + n * j ** 2
        if gmpy.is_square(i_2):
            i = math.sqrt(i_2)
            print i, j, n
            return i
        j += 1


t = time.time()

results = []
squares = [x**2 for x in range(1, 32)]

Ds = [x for x in range(1, 1001) if x not in squares]


for D in Ds:
    print D
    results.append(find_minimal_sol(D))

print results

print Ds[results.index(max(results))]
print time.time() - t
