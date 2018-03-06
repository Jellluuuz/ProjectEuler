
from collections import Counter
import time
def prime_factor(n):
    i = 2
    primes = []
    while i <= n:
        if n % i == 0:
            primes.append(i)
            n = n / i 
        else:
            i += 1
    return Counter(primes)


def amount_divisors(n):
    divisors = 1
    a = prime_factor(n)
    for x in a:
        divisors = divisors * (a[x] + 1)
    return divisors
i = 1
time1 = time.time()
while True:
    n = (i * (i+ 1))/2
 #   print n
   # a = amount_divisors(n)
  #  print a
    if amount_divisors(n) > 500:
        break
    i += 1
print n
print amount_divisors(n)
print time.time()-time1

