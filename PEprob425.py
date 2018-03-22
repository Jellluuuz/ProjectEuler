from find_prime_factorization import prime_sieve
from find_prime_factorization import is_prime
import copy
import time

#prime_list = prime_sieve(10**3, [])

twosrelatives = []

def same_length(my_list):
    same_length_list = []
    length = len(str(my_list[0]))
    for i in my_list:
        for idx in range(length):
            for j in range(10):
                if str(i)[idx] != j:
                    temp = str(copy.deepcopy(i))
                    temp[idx] = j
                    if is_prime(temp):
                        same_length_list.append(temp)
    return same_length_list

print same_length([2])

