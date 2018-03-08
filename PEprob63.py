import time
from multiprocessing import Pool
import math

def is_perfect(num, power):
    float_candidate = num ** (1/power)
    int_candidate = int(math.floor(float_candidate))
    while True:
        powered = int_candidate ** power
        if powered == num: return True
        elif powered > num: return False
        int_candidate += 1

def num_check(n):
    if is_perfect(n, len(str(n))):
        return True
    else:
        return False


numbers = []
for i in range(0,100):
    for j in range(1,100):
        if len(str(j ** i)) == i and j ** i not in numbers:
            numbers.append(j**i)
print len(numbers)



'''
if __name__ == "__main__":
    t = time.time()
    p = Pool(7)
    L = p.map(num_check, range(0, 10**7))
    print sum(L)
    print time.time() - t
'''