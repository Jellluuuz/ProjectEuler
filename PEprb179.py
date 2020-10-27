import time
from find_prime_factorization import prime_sieve


def get_number_divisors(n, primelist):
    half_n = int(float(n)/2) + 1
    if primelist is None:
        primelist = prime_sieve(n, output=[])

    prod = 1
    for p in primelist:
        counter = 0
        while n % p == 0:
            n /= p
            counter += 1
        if counter > 0:
            prod *= (counter+1)
        if n == 1:
            return prod
        if p > half_n:
            return prod+1


t = time.time()
N = 10**7
count = 0
prime_list = prime_sieve(N/2+1, [])
temp2 = 2
for i in range(2, N):
    if i % 1000 == 0:
        print i
    temp1 = temp2
    temp2 = get_number_divisors(i+1, prime_list)
    if temp1 == temp2:
        count += 1

print count
print time.time() - t
