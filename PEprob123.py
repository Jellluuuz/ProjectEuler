from find_prime_factorization import prime_sieve
import time

prime_list = prime_sieve(10**6, [])

print prime_list.index(21059)


def calc_rem(n):
    p = prime_list[n-1]
    return ((p+1)**n + (p-1)**n) % (p**2)


t = time.time()

for j in range(22000):
    if j % 10**3 == 0:
        print j
    if calc_rem(j) > 10**10:
        print j
        print time.time() - t
        exit()

print time.time() - t