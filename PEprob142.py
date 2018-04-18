import gmpy
import time


t = time.time()

n = 1000


for i in range(1, n):
    a = i**2
    for j in range(1, i):
        c = j**2
        if gmpy.is_square(a-c):
            f = a-c
            for k in range(j % 2, j, 2):
                d = k**2
                if gmpy.is_square(a-d):
                    e = a - d
                    if c-e > 0 and gmpy.is_square(c-e):
                        b = c - e
                        x = (a + b)/2
                        y = (e + f)/2
                        z = (c - d)/2
                        if x > y > z > 0:
                            print x, y, z
                            print x + y + z

                            print time.time() - t
                            exit()
