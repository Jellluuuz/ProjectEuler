import time
import math


def divisorgenerator(m):
    large_divisors = []
    for j in xrange(1, int(math.sqrt(m) + 1)):
        if m % j == 0:
            yield j
            if j*j != m:
                large_divisors.append(m / j)
    for divisor in reversed(large_divisors):
        yield divisor


t = time.time()

som = 0
for n in range(10**1, 10**6):
    divisors = list(divisorgenerator(n))
    count = 0
    temp = []
    for i in divisors:
        if (n/i + i) % 4 == 0:
            if i - (n/i + i)/4 > 0:
                if n == 100:
                    temp.append(i)
                    count += 1
    if count == 10:
        som += 1
    if n == 100:
        print n, temp

print som


print time.time() - t
