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
for n in range(10**3, 10**6):
    divisors = list(divisorgenerator(n))
    count = 0
    for i in divisors:
        if (n/i + i) % 4 == 0:
            if i - (n/i + i)/4 > 0:
                count += 1
    if count == 10:
        som += 1
print som


print time.time() - t
