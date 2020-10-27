import time
import math
import operator as op


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

d = {}

d[1] = 0
d[2] = float(1)/ncr(70,20)

total_poss = ncr(70,20)
poss_for_3 = 0
for i in range(1, 11):
    for j in range(1, 11):
        k = 20 - i - j
        if 0 < k < 11:
            poss_for_3 += ncr(10, i) * ncr(10, j) * ncr(10, k)

d[3] = float(poss_for_3)/total_poss

poss_for_4 = 0
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1,11):
            l = 20 - i - j - k
            if 0 < l < 11:
                poss_for_4 += ncr(10, i) * ncr(10, j) * ncr(10, k) * ncr(10,l)

d[4] = float(poss_for_4)/total_poss

poss_for_5 = 0
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1,11):
                m = 20 - i - j - k - l
                if 0 < m < 11:
                    poss_for_5 += ncr(10, i) * ncr(10, j) * ncr(10, k) * ncr(10, l) * ncr(10, m)

d[5] = float(poss_for_5) / total_poss


poss_for_6 = 0
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1,11):
                for m in range(1,11):
                    n = 20 - i - j - k - l - m
                if 0 < n < 11:
                    poss_for_6 += ncr(10, i) * ncr(10, j) * ncr(10, k) * ncr(10, l) * ncr(10, m) * ncr(10, n)

d[6] = float(poss_for_6) / total_poss


poss_for_7 = 0
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1,11):
                for m in range(1,11):
                    for n in range(1, 11):
                        o = 20 - i - j - k - l - m - n
                if 0 < o < 11:
                    poss_for_7 += ncr(10, i) * ncr(10, j) * ncr(10, k) * ncr(10, l) * ncr(10, m) * ncr(10, n) * ncr(10,o)

d[7] = float(poss_for_7) / total_poss

E = 0
for i in range(1,8):
    E += i * d[i]

print E
