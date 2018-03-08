import time


def check_numbers(a, b):
    if len(str(a)) == len(str(b)):
        for i in str(a):
            if str(a).count(i) != str(b).count(i):
                return False
        return True
    return False


t = time.time()

for i in range(1, 1000000):
    count = 0
    for j in range(2, 7):
        if check_numbers(i * j, i):
            count += 1
    if count == 5:
        print i
        break

print time.time() - t