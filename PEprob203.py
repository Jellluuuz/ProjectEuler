import time
import math
from find_prime_factorization import prime_sieve


def choose(n,k):
    return (math.factorial(n))/(math.factorial(k) * math.factorial(n-k))

def get_prime_factors(n, primelist):
    own_num = n
    half_n = int(float(n)/2) + 1
    if primelist is None:
        primelist = prime_sieve(n, output=[])

    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 1:
            return False
        if n == 1:
            return True
        if p > half_n:
            fs.append((own_num, 1))
            return True


t = time.time()

numbers = []
for i in range(51):
    for j in range(i/2 + 1):
        temp = choose(i,j)
        if temp not in numbers:
            numbers.append(choose(i,j))

prime_list = prime_sieve(10**8)
S = 0
for i in numbers:
    if get_prime_factors(i, prime_list):
        S += i

print S

print time.time() - t
