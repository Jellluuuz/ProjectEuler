from find_prime_factorization import prime_sieve
from PEprob41 import is_prime
from find_prime_factorization import is_prime
import math
import time


t = time.time()

n = 10000
primes = prime_sieve(n, [])


def gen_composite_numbers(n):
    primes = prime_sieve(n,[])
    for i in range(4,n):
        if i not in primes and i % 2 != 0:
            yield i


def squares(n):
    square_list = []
    for i in range(1, int(math.sqrt(n))):
        square_list.append(i**2)
    return square_list


square_list = squares(n)
for i in gen_composite_numbers(n):
    setting = False
    for j in primes:
        for k in square_list:
            if i == j + 2 * k:
                setting = True
    if setting is False:
        print i
        print time.time()-t
        exit()


print time.time() - t




