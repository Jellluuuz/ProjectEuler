import time
from find_prime_factorization import get_factors


def number_contribution(M,n):
    return ((10 ** 15 / n) * (n**2)) % (10 ** 9)


t = time.time()
'''
M = 10**9
total = 0
for i in xrange(1, M):
    if i % 1000000 == 0:
        print i
    total += number_contribution(M, i)

print total
'''


N = 10**15
print N * (N * (N+1)/2) #% (10**9) # - (N mod i) * i
print time.time() - t

temp_list = []
for N in range(3,11):
    temp = 0
    for i in range(1,N):
        temp += (N % i) * i
    temp_list.append(temp)

print temp_list


