i = 0
for c in range(1000):
    for b in range(c):
        for a in range(b):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print 'a = %d, b = %d, c = %d' %(a,b,c)
                print a*b*c
print i
