from find_prime_factorization import prime_sieve
import time
import itertools
import math

#t = time.time()


def is_prime(n, primes_list):
    for p in primes_list:
        if p ** 2 > n:
            return True
        elif n % p == 0:
            return False
    return True

if __name__ == '__main__':
    cap = math.sqrt(1000000000)
    primes = prime_sieve(int(cap),[])
    pandigitals = []
    for j in range(1,10):
        for i in itertools.permutations(range(1, j+1)):
            string = ''
            for char in i:
                string = string + str(char)
            pandigital = int(string)
            if is_prime(pandigital, primes):
                pandigitals.append(pandigital)
    print pandigitals
    print max(pandigitals)



#print time.time() - t