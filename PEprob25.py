lst = [1, 1]


def calc_fib(lst):
    c = 0
    while len(str(lst[-1])) < 1000:
        c += 1
        lst.append(sum(lst[-2:]))
    return lst


print len(calc_fib(lst))
