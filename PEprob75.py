

def solutions(p):
    sols = []
    for i in range(1, p-2):
        for j in range(i, p-i-1):
            k = p - i - j
            a = [i, j, k]
            a.sort()
            if a[0]**2 + a[1] ** 2 == a[2] ** 2:
                    sols.append(a)
                    if len(sols) > 4:
                        return False
    return len(sols)/3


count = 0
for i in range(1500000):
    if i % 500 == 0:
        print i
    if solutions(i):
        count += 1


print count