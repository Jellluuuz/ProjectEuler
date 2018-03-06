from find_prime_factorization import prime_sieve
from PEprob41 import is_prime
import math
import itertools
import time


def number_rotations(n):
    rotations = []
    for i in range(len(str(n))):
        temp_string = ''
        for j in range(len(str(n))):
            temp_string = temp_string + str(n)[(i + j) % len(str(n))]
        rotations.append(int(temp_string))
        i += 1
    return rotations




t = time.time()

circular_primes = []
check_primes = prime_sieve(int(math.sqrt(1000000)),[])
primes = prime_sieve(1000000, [])
for i in primes:
    state = True
    for j in number_rotations(i):
        if not is_prime(j, check_primes):
            state = False
    if state is True:
        circular_primes.append(i)

print circular_primes
print len(circular_primes)

print time.time() - t


