import math
import time

# return a dict or a list of primes up to N
# create full prime sieve for N=10^6 in 1 sec
def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_factors(n, primelist=None):
    if primelist is None:
        primelist = prime_sieve(n,output=[])

    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0

        while n % p == 0:
            n /= p
            fcount[p] += 1

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors


# get a list of prime factors
# ex: get_prime_factors(140) -> ((2,2), (5,1), (7,1))
#     140 = 2^2 * 5^1 * 7^1
def get_prime_factors(n, primelist):
    own_num = n
    half_n = int(float(n)/2) + 1
    if primelist is None:
        primelist = prime_sieve(n, output=[])

    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))
        if n == 1:
            return fs
        if p > half_n:
            fs.append((own_num, 1))
            return fs



    #return fs


def is_prime(n,primes_list):
    if primes_list is None:
        primes_list = prime_sieve(int(math.sqrt(n)), [])
    if n == 1:
        return False
    for p in primes_list:
        if p <= math.sqrt(n):
            if n % p == 0:
                return False
        else:
            return True

    return True

