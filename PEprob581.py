from find_prime_factorization import get_prime_factors
import time

N = 4380
triangle_numbers = [(x * (x + 1))/2 for x in range(2, N)]

for i, val in enumerate(triangle_numbers):
    prime_factors = get_prime_factors(val, None)
    if prime_factors[-1][0] <= 47:
        print prime_factors
        print i + 1, val


