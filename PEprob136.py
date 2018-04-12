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
'''
som = 0
for n in xrange(1, 10**2):
    count = 0
    if n % 10000 == 0:
        print n
    for i in divisorgenerator(n):
        if count > 1:
            break
        if (n/i + i) % 4 == 0:
            if i - (n/i + i)/4 > 0:
                count += 1
    if count == 1:
        som += 1
        print n
print som

print '---'

som = 0
for n in range(4, 10**2):
    count = 0
    for i in range(1, int(math.sqrt(n)/3) + 2):
        if count > 1:
            break
        if n % i == 0:
            if (n/i + i) % 4 == 0:
                count += 1
    if count < 2:
        if (n+1) % 4 == 0:
            count += 1
        if (2 + n/2) % 4 == 0:
            count += 1
    else:
        continue
    if count == 1:
        for j in range(int(math.sqrt(n)/3) + 1, int(math.sqrt(n))):
            if n % i == 0:
                if (n/i + i) % 4 == 0:
                    count += 2
                    break
    if count == 1:
        print n
        som += 1

print som


'''
som = 0
for n in range(3, 10**6):
    count = 0
    nroot = math.sqrt(n)
    for i in range(1, int(nroot)+1):
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
