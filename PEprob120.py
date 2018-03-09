import time

t = time.time()
sum1 = 0
for a in range(3, 1001):
    maxi = 2
    for n in range(1, a):
        r = (2 * n * a) % (a**2)
        if r > maxi:
            maxi = r
    r = maxi
    if a == 7:
        print r
    sum1 += r
print sum1

print time.time() - t
#for n in range(2, 1000, 2):
#    print ((a + 1) ** n + (a - 1) ** n) % (a ** 2)

