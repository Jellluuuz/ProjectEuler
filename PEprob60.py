from find_prime_factorization import prime_sieve
from find_prime_factorization import is_prime
import time
import numpy as np


#def concat(a):
#    if not is_prime(int(str(a[0]) + str(a[1]))) or not is_prime(int(str(a[1]) + str(a[0]))):
#        return False
#    else:
#        return True
primes_check = prime_sieve(10**5,[])
def concat(a):
    for i in a:
        temp = list(a)
        temp.remove(i)
        for j in temp:
            if not is_prime(int(str(i) + str(j)), primes_check):
                return False
    return True


def append_check(a):
    for i in a[:-1]:
        if not is_prime(int(str(i) + str(a[-1]))):
            return False
        if not is_prime(int(str(a[-1]) + str(i))):
            return False
    return True

t = time.time()

primes = prime_sieve(10000, [])
#prime_list = prime_sieve(10**5,[])
Check_matrix = np.zeros((len(primes),len(primes)))

for i in primes:
    for j in primes[primes.index(i):]:
        if concat([i, j]):
            Check_matrix[primes.index(i)][primes.index(j)] = True

print Check_matrix

print time.time() - t

'''
gucci_primes = [[23, 311, 677, 827],[11,23,743,1871],[11,239,1049,1847],[11,239,1091,1847],[23,677,827,1871]]

for i in primes:
    for j in range(len(gucci_primes)):
        temp = list(gucci_primes[j])
        temp.append(i)
        if append_check(temp):
            print temp

print time.time()-t
'''

t = time.time()
gucci_primes = []
for i in primes:
    for j in [q for q, x in enumerate(Check_matrix[primes.index(i), ...]) if x]:
        for k in [q for q, x in enumerate(Check_matrix[primes.index(i), ...]) if x]:
            if Check_matrix[j, k]:
                for l in [q for q, x in enumerate(Check_matrix[primes.index(i), ...]) if x]:
                    if Check_matrix[j,l] and Check_matrix[k, l]:
                       for m in [q for q, x in enumerate(Check_matrix[primes.index(i), ...]) if x]:
                            if Check_matrix[j,m] and Check_matrix[k,m] and Check_matrix[l,m]:
                                gucci_primes.append([i, primes[j], primes[k], primes[l],primes[m]])
                                print time.time() -t

print gucci_primes
print sum(gucci_primes[0])
print 'time is %f' % (time.time()-t)
