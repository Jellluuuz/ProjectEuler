from find_prime_factorization import prime_sieve
import time


#Wilson's Theorem is key!

def test_final(p):
    pthree = (p-1)/2 % p
    tempthree = (p-1)/2

    while True:
        if tempthree % 3 == 0:
            pfour = (-tempthree/3) % p
            tempfour = pfour % p
            break
        else:
            tempthree += p
    while True:
        if tempfour % 4 == 0:
            pfive = (-tempfour/4) % p
            break
        else:
            tempfour += p

    return (pthree +pfour + pfive) % p


t_start = time.time()
prime_list = prime_sieve(10**8, [])[2:]

t1 = time.time()

final = 0
for p in prime_list:
    final += test_final(p)
print final

print time.time() - t1, time.time() - t_start
