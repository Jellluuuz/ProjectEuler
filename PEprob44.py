import math
import time

n = 10000


def create_pentagonal_list(k):
    return [i*(3*i-1)/2 for i in range(1, k)]


def check_pentagonal(k):
    if (float((1./2 + math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 + math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    elif (float((1./2 - math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 - math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    else:
        return False


def eligible_numbers(k, pentagonals):
    eligible_numbers = []
    for i in range(k-1):
        for j in range(i, k-1):
            if check_pentagonal(pentagonals[i] + pentagonals[j]):
                if check_pentagonal(pentagonals[j] - pentagonals[i]):
                    eligible_numbers.append((pentagonals[i], pentagonals[j]))
                    print i
    return eligible_numbers


#print create_pentagonal_list(n)
t = time.time()
eligible_numbers = eligible_numbers(n, create_pentagonal_list(n))
print eligible_numbers
print time.time()-t


