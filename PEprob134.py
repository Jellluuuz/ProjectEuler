from find_prime_factorization import prime_sieve
import time


def counter_gen(a, b):
    a = a % 10
    b = b % 10
    count = 0
    if a == 1:
        if b == 1:
            while True:
                yield count * 10 + 1
                count += 1
        if b == 3:
            while True:
                yield count * 10 + 7
                count += 1
        if b == 7:
            while True:
                yield count * 10 + 3
                count += 1
        if b == 9:
            while True:
                yield count * 10 + 9
                count += 1

    elif a == 3:
        if b == 1:
            while True:
                yield count * 10 + 3
                count += 1
        if b == 3:
            while True:
                yield count * 10 + 1
                count += 1
        if b == 7:
            while True:
                yield count * 10 + 9
                count += 1
        if b == 9:
            while True:
                yield count * 10 + 7
                count += 1

    elif a == 7:
        if b == 1:
            while True:
                yield count * 10 + 7
                count += 1
        if b == 3:
            while True:
                yield count * 10 + 9
                count += 1
        if b == 7:
            while True:
                yield count * 10 + 1
                count += 1
        if b == 9:
            while True:
                yield count * 10 + 3
                count += 1

    elif a == 9:
        if b == 1:
            while True:
                yield count * 10 + 9
                count += 1
        if b == 3:
            while True:
                yield count * 10 + 3
                count += 1
        if b == 7:
            while True:
                yield count * 10 + 7
                count += 1
        if b == 9:
            while True:
                yield count * 10 + 1
                count += 1
    else:
        while True:
            yield count
            count += 1


def find_counter(a,b):
    factor = 0
    for i in range(len(str(a))):
        for k in range(10):
            if ((factor + 10**i * k) * b) % 10**(i+1) == a % 10**(i+1):
                factor = factor + 10**i * k
                break
    return factor


t = time.time()

prime_list = prime_sieve(10**6 + 10 ** 4, [])   #MOET ER NOG EENTJE BIJ, P1 < 10**7, NIET P2
prime_list = prime_list[2:]



'''
sols = []

for i in range(len(prime_list)-1):
    p1 = prime_list[i]
    p2 = prime_list[i+1]
    for counter in counter_gen(p1, p2):
        if (counter * p2) % 10**len(str(p1)) == p1:
            #print p1, p2, counter, counter * p2
            sols.append(counter * p2)
            break

#print sols
print sum(sols)
'''

sols2 = []


for o in range(len(prime_list)-1):
    if prime_list[o] > 10**6:
        break
    p1 = prime_list[o]
    p2 = prime_list[o+1]
    counter = find_counter(p1, p2)
    sols2.append(counter*p2)

print sols2[:10]
print sum(sols2)

print find_counter(19,23) * 23

print time.time() - t
