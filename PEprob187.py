from find_prime_factorization import prime_sieve
import time


t = time.time()
prime_list = prime_sieve(5 * 10**7, [])
prime_list2 = prime_sieve(10**4, [])

count = 0

for idx, val in enumerate(prime_list2):
    if val == 101:
        prime_list = prime_sieve(10**6, [])
    if val == 1009:
        prime_list = prime_sieve(10**5, [])
    print val
    for val2 in prime_list[idx:]:
        if val * val2 < 10**8:
            count += 1
        else:
            break


print count

print time.time() - t

