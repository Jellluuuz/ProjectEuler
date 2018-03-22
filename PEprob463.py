import time


def function1(n):
    try:
        return d[n]
    except KeyError:
        if n == 1 or n == 0:
            return 1
        if n == 3:
            return 3
        if n % 2 == 0:
            d[n] = function1(n / 2)
            return d[n]
        if (n-1) % 4 == 0:
            d[n] = 2 * function1(2*((n-1)/4) + 1) - function1((n-1) / 4)
            return d[n]
        if (n-3) % 4 == 0:
            d[n] = 3 * function1(2*(n - 3)/4 + 1) - 2 * function1((n-3)/4)
            return d[n]


def sum_function(n):
    try:
        return s[n]
    except KeyError:
        if n < 1:
            return 0
        if n == 3:
            return 5
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n % 4 == 3:
            s[n] = 6 * sum_function((n-1)/2) - 8 * sum_function((n-3)/4) - 1
            return s[n]
        elif n % 4 == 2:
            s[n] = sum_function(n-1) + function1(n/2)
            return s[n]
        elif n % 4 == 1:
            s[n] = function1(n) + function1((n-1)/2) + sum_function(n-2)
            return s[n]
        else:
            s[n] = sum_function(n-1) + function1(n/4)
            return s[n]


s = {}
s[1] = 1
s[2] = 2
s[3] = 5
s[4] = 6
s[5] = 11


d = {}
d[1] = 1
d[2] = 1
d[3] = 3
d[4] = 1
d[5] = 5

t = time.time()
print str(sum_function(3**37))[-9:]
print time.time() - t
