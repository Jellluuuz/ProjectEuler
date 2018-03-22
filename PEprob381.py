from find_prime_factorization import prime_sieve
import math
import time


def mod_fact(n, p):
    mod_fact = 1
    while n > 1:
        mod_fact *= n
        mod_fact = mod_fact % p
        n -= 1
    return mod_fact


def prime_k_fact(p):
    s = 0
    temp = mod_fact(p-5, p)
    for k in range(5)[::-1]:
        s += temp
        temp *= (p-k) % p
    return s % p

t = time.time()


# hogere priemgetallen duurt lang
prime_list = prime_sieve(10**4, [])[2:]

total_sum = 0
for p in prime_list:
    total_sum += prime_k_fact(p)

print total_sum

print time.time() - t

