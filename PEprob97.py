'Little Fermat"s theorem: a^p = a mod p'

from find_prime_factorization import is_prime

n = 1
for i in range(7830457):
    n = 2 * n % 10**10
print str(n * 28433 + 1)[-10:]