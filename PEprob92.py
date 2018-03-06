import time

def calc_next(n):
    next = 0
    for char in str(n):
        next += int(char) ** 2
    return next

def run_sequence(n):
    while n != 89 and n != 1:
        n = calc_next(n)
    return n


def create_table():
    valid = []
    for i in range(1, 568):
        temp = run_sequence(i)
        if temp == 89:
            valid.append(i)
    return valid


valid = create_table()

t = time.time()
count = 0
for i in range(568, 10000000):
    if calc_next(i) in valid:
        count += 1
print count + len(valid)

print time.time() - t
