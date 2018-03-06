from find_prime_factorization import is_prime
from find_prime_factorization import prime_sieve


primes = prime_sieve(1000000, [])
truncatable_primes = []

def trunc_right(n):
    return int(str(n)[:len(str(n))-1])



def trunc_left(n):
    return int(str(n)[1:])



for i in primes[4:]:
    setting = True
    n = i
    while len(str(n)) > 1:
        if not is_prime(trunc_right(n)):
            setting = False
            break
        else:
            n = trunc_right(n)
    n = i
    while len(str(n)) > 1:
        if not is_prime(trunc_left(n)):
            setting = False
            break
        else:
            n = trunc_left(n)
    if setting is True:
        truncatable_primes.append(i)

print is_prime(1)
print sum(truncatable_primes)




