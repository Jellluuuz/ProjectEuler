import time
from multiprocessing import Pool


def reverse(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num //= 10
  return rev


def check_reversible(n):
    string = str(n)
    if int(string[-1]) == 0:
        return False
    remainder = 0
    for i in range(len(str(n))):
        q = int(string[i]) + int(string[-(i+1)]) + remainder
        if q % 2 == 0:
            return False
        if q > 9:
            remainder = 1
        else:
            remainder = 0
    return True


def check_reversible_2(n):
    if int(str(n)[-1]) == 0:
        return False
    reverse = int(str(n)[::-1])
    sum_num = n + reverse
    for i in str(sum_num):
        if int(i) % 2 == 0:
            return False
    return True


t = time.time()
if __name__ == "__main__":
    p = Pool(7)
    L = p.map(check_reversible_2, range(1, 10**6))
    print sum(L)


print time.time() - t