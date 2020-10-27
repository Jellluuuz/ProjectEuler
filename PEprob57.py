import time

t0 = time.time()

key_val = [1]
denominator = [2]
numerator = [3]


for i in range(999):
    key_val.append(denominator[-1])
    denominator.append(2*denominator[-1] + key_val[-2])

    numerator.append(key_val[-1] + denominator[-1])

print key_val
print numerator
print denominator

count = 0

for i in range(len(numerator)):
    if len(str(numerator[i])) > len(str(denominator[i])):
        count += 1


print count
print time.time() - t0
