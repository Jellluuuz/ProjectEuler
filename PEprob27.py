from find_prime_factorization import prime_sieve
from find_prime_factorization import is_prime
import time

t = time.time()



primes_list = prime_sieve(10**5, [])
b_primes = prime_sieve(10**3, [])

maxi = 0

for a in range(-1000, 1000):
    for b in b_primes:
        count = 0
        n = 0
        while True:
            val = n**2 + a * n + b
            if val > 1 and is_prime(val, primes_list):
                count += 1
                n += 1
            else:
                if count > maxi:
                    maxi = count
                    params = (a, b)
                break

#print list_of_n
print params,maxi
print params[0] * params[1]

print time.time() - t