
import time



maxi = 0
val = 0
t = time.time()
for d in range(2,1001):
    for i in range(1,60):
        if float(10**i - 1) % d == 0:
            print '---'
            print float((10**i - 1))/ d
            print d
            if len(str((float(10 ** i - 1 / d)))) >= maxi and len(str((float(10 ** i - 1) / d))) < 1000:
                maxi = len(str((10 ** i - 1 / d)))
                val = d
            break

print val


for i in range(1,10):
    if float(10**i - 1) % 7 == 0:
        print float(10 **i - 1)/ 7

GECHEAT, FUCKING KUTVRAAG