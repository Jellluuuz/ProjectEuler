from find_prime_factorization import get_prime_factors
import time

CHEATED, BRUTE-FORCE TOOK TOO LONG

def check_factors(n):
    if len(get_prime_factors(n, None)) == 4:
        return True


t = time.time()

for i in range(134000, 135000):
    if check_factors(i):
        print i
        setting = True
        for j in range(1, 4):
            if not check_factors(i+j):
                setting = False
                break
        if setting is True:
            print i
            print time.time() - t
            exit()

print time.time() - t


