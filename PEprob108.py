import time
from find_prime_factorization import get_prime_factors
from find_prime_factorization import prime_sieve


def get_number_divisors(list_of_tuples, prod, val):
    if prod > val:
        return
    if len(list_of_tuples) == 0:
        if prod <= val:
            global count
            count += 1
            return
        return
    for i in range((list_of_tuples[0][1])*2+1):
        get_number_divisors(list_of_tuples[1:], prod * (list_of_tuples[0][0] ** i), val)
    return


t = time.time()

prime_list = prime_sieve(10**6, [])

n = 1
while True:
    count = 0
    get_number_divisors(get_prime_factors(n, prime_list), 1, n)
    if count > 400:
        print count
        print n
        break
    n += 1
print time.time() - t
