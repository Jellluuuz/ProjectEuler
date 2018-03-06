from math import *
primes = []


def largest_prime_number(n):
    global primes
    i = 2
    while n > 1:

        if n % i == 0:
            n = n/i
            print 'n = %d' %n
            print 'i = %d' %i
        i += 1


largest_prime_number(600851475143)
