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
for n in range(1, 10**6):

    count = 0
    nroot = math.sqrt(n)
    for i in xrange(1, int(nroot)+1):
            if n % i == 0:
                if (n/i + i) % 4 == 0:
                    if count > 0:
                        count += 1
                        break
                    if i <= nroot/math.sqrt(3):
                        count += 1
                    else:
                        if i == nroot:
                            count += 1
                        else:
                            count += 2
                            break

    if count == 1:
        som += 1
print som


print time.time() - t
