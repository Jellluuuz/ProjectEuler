import time
from find_prime_factorization import get_prime_factors
from find_prime_factorization import prime_sieve


def number_of_poss_sols(n):
    prime_factors = get_prime_factors(n, prime_list)
    p = 1
    for i in prime_factors:
        p *= i[1]*2 + 1
    if n % 2 == 0:
        number_of_sols = (p+1)/2
    else:
        number_of_sols = p / 2
    return number_of_sols

''' 
prime_list = prime_sieve(10**8, [])
t = time.time()
n = 1
while True:
    temp = number_of_poss_sols(n)
    if n == 123456:
        print temp
        print n
        break
    n += 1
'''
t = time.time()

prime_list = prime_sieve(1000,[])[:22]

p = 2**22

print number_of_poss_sols(p)

print time.time() - t
