from find_prime_factorization import get_prime_factors
from find_prime_factorization import prime_sieve
import time


def direct_totient_function(k):
    p = 1
    for l in get_prime_factors(k, prime_list):
        p *= (1 - 1./l[0])
    return int(k * p)


def check_permutation(a, b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    for char in a:
        if a.count(char) != b.count(char):
            return False
    return True


def find_min(my_list):
    val = 0
    mini = 10
    for j in my_list:
        if float(j[0])/j[1] < mini:
            mini = float(j[0])/j[1]
            val = j[0]
    return val


t = time.time()
# not below 10**6
N = 10**5
prime_list = prime_sieve(N, [])
print time.time() - t
valid_permutes = []
for i in range(2, N):
    temp = direct_totient_function(i)
    if check_permutation(i, temp):
        print i
        print time.time() - t
        valid_permutes.append((i, temp))
print time.time() - t
min_val = find_min(valid_permutes)
print min_val
print time.time() - t
