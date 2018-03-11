import time
import math

def check_pandigital_end(n):
    a = str(n)[-9:]
    for i in range(1, 10):
        if a.count(str(i)) != 1:
            return False
    return True

def check_pandigital_start(n):
    a = str(n)[:9]
    for i in range(1, 10):
        if a.count(str(i)) != 1:
            return False
    return True


def check_pandigital(n):
    a = str(n)[:9]
    b = str(n)[-9:]
    for i in range(1, 10):
        if a.count(str(i)) != 1:
            return False
        if b.count(str(i)) != 1:
            return False
    return True

t = time.time()

F = [1,1]
temp1start = 1
temp1end = 1
temp2start = 1
temp2end = 1
count = 2
end_pandigitals = []

while count < 10**8:

    if count % 1000 == 0:
        print count
    temp3end = temp1end + temp2end % 10**12
    temp3start = int(str(temp1start)[:575]) + int(str(temp2start)[:575])
    count += 1
    if check_pandigital_start(temp3start): #and check_pandigital_end(temp3end):
        print count
        break
    else:
        temp1start = temp2start
        temp1end = temp2end
        temp2start = temp3start
        temp2end = temp3end


print '---'
print count




print time.time() - t
