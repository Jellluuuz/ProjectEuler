import time
from find_prime_factorization import prime_sieve


prime_list = prime_sieve(5,[])

print prime_list


def find_number(n):
    if n > 10 ** 8:
        return
    else:
        global count
        count += 1
        for p in prime_list:
            find_number(n * p)


count = 0
for i in prime_list:
    print i
    find_number(i)

print count