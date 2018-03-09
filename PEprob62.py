import time
from multiprocessing import Pool


def check_numbers(a,b):
    if len(str(a)) == len(str(b)):
        for i in str(a):
            if str(a).count(i) != str(b).count(i):
                return False
        return True
    return False


def check_number(n):
    count = 0
    for i in cubes_set:
        if check_numbers(n,i):
            count += 1
    if count == 5:
        return True


t = time.time()
cubes = [x**3 for x in range(10000)]
cubes_set = set([x**3 for x in range(10000)])
if __name__ == '__main__':
    p = Pool(7)
    L = p.map(check_number, cubes)
    print time.time() - t
    print L.index(1)**3
