
def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]
1406357289
S = 0
for p in permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    #if p[0] == 1 and p[1] == 4 and p[2] == 0 and p[3] == 6 and p[4] == 3 and p[5] == 5 and p[6] == 7 and p[7] == 2 and p[8] == 8 and p[9] == 9:
    if (p[1]*100+p[2]*10+p[3]) % 2 == 0:
        if (p[2] * 100 + p[3] * 10 + p[4]) % 3 == 0:
            if (p[3] * 100 + p[4] * 10 + p[5]) % 5 == 0:
                if (p[4] * 100 + p[5] * 10 + p[6]) % 7 == 0:
                    if (p[5] * 100 + p[6] * 10 + p[7]) % 11 == 0:
                        if (p[6] * 100 + p[7] * 10 + p[8]) % 13 == 0:
                            if (p[7] * 100 + p[8] * 10 + p[9]) % 17 == 0:
                                S += p[0]*10**9 + p[1]*10**8 + p[2]*10**7 + p[3]*10**6 + p[4]*10**5 + p[5]*10**4 + p[6]*10**3 + p[7]*10**2+ p[8]*10**1+ p[9]


print S
