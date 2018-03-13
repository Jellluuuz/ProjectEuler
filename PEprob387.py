from find_prime_factorization import is_prime
from find_prime_factorization import prime_sieve
import math
import time


def check_harshad(n):
    S = 0
    for i in str(n):
        S += int(i)
    if n % S == 0:
        return True
    return False


def add_one(n,k):
    return int(str(n) + str(k))

t = time.time()
starting_harshad = range(1,10)
total_harshad = [starting_harshad]
while True:
    temp_harshad = []
    for i in total_harshad[-1]:
        for k in range(10):
            temp = add_one(i,k)
            if check_harshad(temp):
                temp_harshad = temp_harshad + [temp]
    total_harshad.append(temp_harshad)
    if len(str(total_harshad[-1][0])) >= 13:
        break


total_strong_harshad = []
for i in total_harshad:
    prime_list = prime_sieve(10 ** (int(math.ceil(len(str(i[0]))/2))), [])
    for j in i:
        S = 0
        for k in str(j):
            S += int(k)
        if is_prime(j/S, prime_list):
            total_strong_harshad.append(j)


total_strong_harshad_primes = []
S = 0
j = 0
for i in total_strong_harshad:
    print i
    if len(str(i)) != j:
        prime_list = prime_sieve(10 ** (int(math.ceil((len(str(i)) + 2) / 2))), [])
        j = len(str(i))
    #prime_list = prime_sieve(10 ** (int(math.ceil(len(str(i))+1 / 2))), [])
    for j in [1,3,7,9]:
        a = int(str(i) + str(j))
        if is_prime(a, prime_list):
            total_strong_harshad_primes.append(a)
            S += a

print S
print time.time() - t