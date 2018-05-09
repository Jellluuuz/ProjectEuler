import time
from find_prime_factorization import prime_sieve
from find_prime_factorization import get_prime_factors
import math

prime_list = prime_sieve(10**5, [])


def find_smallest_factorial(n):
    prime_factors = get_prime_factors(n, prime_list)
    max_factor = []
    for i in prime_factors:
        j = 1
        count = 0
        while True:
            counter = 1
            temp = j
            while temp % i[0] == 0:
                counter += 1
                temp /= i[0]
            count += counter
            if i[1] <= count:
                max_temp = i[0] * j
                break
            j += 1

        max_factor.append(max_temp)
    return max(max_factor)


N = 10**5

t = time.time()

S = 0
for i in range(2, N + 1):
    S += find_smallest_factorial(i)

print S

print time.time() - t
