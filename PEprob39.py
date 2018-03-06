import time




def solutions(p):
    sols = []
    for i in range(1, p-2):
        for j in range(i, p-i-1):
            k = p - i - j
            a = [i, j, k]
            a.sort()
            if a[0]**2 + a[1] ** 2 == a[2] ** 2:
                    sols.append(a)
    return len(sols)/3

t = time.time()

per = 0
maxi = 0
for p in range(3, 1001):
    current_sol = solutions(p)
    if current_sol > maxi:
        maxi = current_sol
        per = p

print maxi
print per

print 'time is %f' %(time.time()-t)
