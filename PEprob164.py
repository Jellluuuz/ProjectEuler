import time

count = 0


def create_number(strng, n, som):
    if len(strng) == n:
        global count
        count += 1
        return
    else:
        for j in range(10-som):
            temp2 = int(strng[-1])
            create_number(strng + str(j), n, temp2 + int(j))


t = time.time()
for i in range(1, 10):
    create_number(str(i), 9, 0)
print count

print time.time() - t
