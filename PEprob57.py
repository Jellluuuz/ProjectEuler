import time
from fractions import Fraction

t = time.time()

deci_fracs = []

a = Fraction(1./2)
for i in range(1000):
    deci_fracs.append(str(1 + a))
    a = Fraction(str(1./(2+a))).limit_denominator()
    print a

count = 0
for i in deci_fracs:
    num = i.split('/')
    #print num
    if len(num[0]) > len(num[1]):
        count += 1
    print num[0], num[1]

print count

print time.time() - t

