import math
from find_prime_factorization import get_prime_factors
import time
import numpy as np

def relative_prime(n,k):
    prime = True
    for i in get_prime_factors(n, None):
        if k % i[0] == 0:
            prime = False
    return prime


def totient_function(k):
    totient_list = [x for x in range(1, k)]
    dummy = [x for x in range(1, k)]
    primes = get_prime_factors(k, None)
    for i in totient_list:
        for j in primes:
            if i % j[0] == 0:
                dummy.remove(i)
                break
    return len(dummy)

def direct_totient_function(k):
    p = 1
    for i in get_prime_factors(k, None):
        p *= (1 - 1./i[0])
    return k * p


def find_largest_quotient(n):
    max = 0
    max_value = 0
    for i in range(2, n):
        temp = direct_totient_function(i)
        if float(i)/temp > max:
            max = float(i)/temp
            max_value = i
    return max_value


t = time.time()
print find_largest_quotient(25000)
#print totient_function(113)
#print direct_totient_function(113)
print time.time() - t


