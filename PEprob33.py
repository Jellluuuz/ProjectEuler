import time

t = time.time()

results = []

for i in range(10,99):
    for j in range(i+1,100):
        for char in str(i):
            if char in str(j):
                tempi = str(i).replace(char, "")
                tempj = str(j).replace(char, "")
                print str(i)[-1]
                try:
                    if float(int(tempi)/float(tempj)) == float(i/float(j)) and int(str(i)[-1]) != 0:
                        results.append((i,j))
                except ZeroDivisionError:
                    continue
                except ValueError:
                    continue

print results
num = 1
den = 1
for i in results:
    num *= i[0]
    den *= i[1]

num = float(num)
den = float(den)
i = 2
while num > 0:
    print i
    if num == 1:
        break
    if num % i == 0 and den % i == 0:
        num /= i
        den /= i
    else:
        i += 1

print num, den

print time.time() - t