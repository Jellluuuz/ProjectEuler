from find_prime_factorization import prime_sieve
from find_prime_factorization import is_prime
import time
import math

t = time.time()
prime_list = prime_sieve(10**5, [])
number_count = 1
prime_count = 0
i = 1
j = 2
spiral_length = 1
while True:
    for dummy in range(4):
        i += j
        if is_prime(i, prime_list):
            prime_count += 1
        number_count += 1
    spiral_length += 2

    if float(prime_count)/number_count < 0.1:
        print spiral_length
        break
    j += 2

print time.time() - t