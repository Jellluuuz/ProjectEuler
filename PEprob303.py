import time


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def foo2(n):
    i = 1
    while True:
        tern = int(ternary(i))
        if tern %  n == 0:
            return tern / n
        i += 1


t = time.time()

som = 0

for idx in range(1, 901):
    som += foo2(idx)

print som

print time.time() - t


