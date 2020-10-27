from find_prime_factorization import prime_sieve
import time


def find_counter(a, b):
    factor = 0
    for i in range(len(str(a))):
        for k in range(10):
            if ((factor + 10**i * k) * b) % 10**(i+1) == a % 10**(i+1):
                factor = factor + 10**i * k
                break
    return factor


t = time.time()

prime_list = prime_sieve(10**6 + 10 ** 4, [])
prime_list = prime_list[2:]

sols2 = []

for o in range(len(prime_list)-1):
    if prime_list[o] > 10**6:
        break
    p1 = prime_list[o]
    p2 = prime_list[o+1]
    counter = find_counter(p1, p2)
    sols2.append(counter*p2)

print sum(sols2)
print time.time() - t
