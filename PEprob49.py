import time
from find_prime_factorization import prime_sieve
import itertools

primes = prime_sieve(10000, [])
primes = [x for x in primes if len(str(x)) == 4]

triples = []
for i1, val1 in enumerate(primes):
    for i2, val2 in enumerate(primes[i1+1:]):
        if val2 + val2 - val1 in primes:
            triples.append((val1, val2, val2 + val2-val1))


correct_triples = []
for i in triples:
    temp = True
    for char in str(i[0]):
        if char not in str(i[1]) or char not in str(i[2]):
            temp = False
    for char in str(i[1]):
        if char not in str(i[0]) or char not in str(i[2]):
            temp = False
    for char in str(i[2]):
        if char not in str(i[0]) or char not in str(i[1]):
            temp = False
    if temp:
        correct_triples.append(i)
296962999629

print correct_triples
