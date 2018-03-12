import time


def find_minimal_sol(D):
    for i in range(1,3000):
        for j in range(1,10000):
            if i**2 - D * j**2 == 1:
                return i
    print 'NIKS GEVONDEN YO'
t = time.time()
results = []
squares = [x**2 for x in range(1,32)]

Ds = [x for x in range(1,1001) if x not in squares]

for D in Ds:
    print D
    results.append(find_minimal_sol(D))

print results

print Ds[results.index(max(results))]
print time.time() - t