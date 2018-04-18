from find_prime_factorization import prime_sieve
import time



t = time.time()

prime_list = prime_sieve(100, [])

for p in prime_list:
    for n in range(1,100000):
        val = n ** 3 + n**2 * p
        if val ** (1./3) == int(val ** (1./3)):
            print p, n, val