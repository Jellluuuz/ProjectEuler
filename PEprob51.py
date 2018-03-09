import time
from multiprocessing import Pool
from find_prime_factorization import prime_sieve
from find_prime_factorization import is_prime
import itertools
import copy

def check_number(n):
    number_list = []
    for i in str(n):
        number_list.append(int(i))
    for k in range(1, len(str(n)), 1):
        for j in itertools.combinations(range(len(str(n))), k):
            count = 0
            for i in range(10):
                temp = copy.copy(number_list)
                if i == 0 and 0 in j:
                    continue
                for p in j:
                    temp[p] = i
                number = 0
                for o, val in enumerate(temp):
                    number += val *10 ** (len(temp)-(o+1))
                if number in primes:
#                if is_prime(number, primes):
                    count += 1
            if count > 7:
                print j
                print number
                return True

    return False

t = time.time()
primes = set(prime_sieve(1000000, []))



if __name__ == "__main__":
    p = Pool(7)
    L = p.map(check_number, range(1, 1000000))
    print L.index(1) + 1


#results = []
#for i in range(100000):
#    if check_number(i):
#        results.append(i)


#print 'RESULTS'
#print results
print time.time() - t


