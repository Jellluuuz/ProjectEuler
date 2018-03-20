import time
from find_prime_factorization import prime_sieve


def largest_idempotent(n):
    maxi = 0
    for i in range(n):
        if (i ** 2) % n == i:
            maxi = i
    return maxi


t = time.time()

N = 10000
prime_list = prime_sieve(N, [])
to_check_list = [i for i in range(1, N+1) if i not in prime_list]
print to_check_list
S = 0
for i in to_check_list:
    S += largest_idempotent(i)
S += len(prime_list)
print S

print time.time() - t

#check out https://math.stackexchange.com/questions/175963/idempotents-in-mathbb-z-n