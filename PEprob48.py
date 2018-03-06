S = 0
for i in range(1, 1001):
    print i
    S += i**i
S = str(S)
S = int(S[-10:])

print S
