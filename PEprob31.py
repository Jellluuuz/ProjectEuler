import math
import time

''' 
d = {}
for i in range(1,201):
    d[float(i)/100] = 0

d[0.01] = 1
d[0.02] = 1
for i in range(2,201):
    for j in range(1,int(float(i)/2 + 1)):
        for k in range(i- j, i):
            if j + k == i:
                print i, j, k
                d[float(i + 1)/100] = d[float(j)/100] + d[float(k)/100]
                if float(i)/100 in lst:
                    d[float(i + 1)/100] += 1

print d[2.00]
'''
setting = False
t = time.time()
count = 0
lst = [2., 1., 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
for i in range(2):
    current_val = i * 200
    if i * 200 == 200:
        count += 1
        break
    for j in range(3):
        current_val = i * 200 + j * 100
        if current_val == 2:
            count += 1
            break
        for k in range(5):
            current_val = i * 200 + j * 100 + k * 50
            if current_val == 2:
                count += 1
                break
            for l in range(11):
                current_val = i * 200 + j * 100 + k * 50 + l * 20
                if current_val == 2:
                    count += 1
                    break
                for m in range(21):
                    current_val = i * 200 + j * 100 + k * 50 + l * 20 + m * 10
                    if current_val == 2:
                        count += 1
                        break
                    for n in range(41):
                        current_val = i * 200 + j * 100 + k * 50 + l * 20 + m * 10 + n * 5
                        if current_val == 2:
                            count += 1
                            break
                        for o in range(101):
                            current_val = i * 200 + j * 100 + k * 50 + l * 20 + m * 10 + n * 5 + o * 2
                            p = 200 - current_val
                            if current_val + p == 200 and 0 <= p <= 200:
                                count += 1


print count

print time.time() - t