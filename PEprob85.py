import time


def check_rectangles(L,W):
    count = 0
    for i in range(1,L+1):
        for j in range(1,W+1):
            count += (L-i + 1) * (W - j + 1)
    return count


t = time.time()

best = 0
area = 0
for i in range(100):
    for j in range(100):
        sol = check_rectangles(i,j)
        if abs(sol - 2000000) < abs(best - 2000000):
            best = sol
            area = i * j

print area
print 'time is %f' % (time.time() - t)
