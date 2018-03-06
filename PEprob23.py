import numpy as np

p = np.arange(1,28123,1)


def find_abundant_numbers(n):
    abundant_numbers = []
    for i in range(1,n):
        divisors = []
        for j in range(1,i):
            if i % j == 0:
                divisors.append(j)
        if sum(divisors) > i:
            abundant_numbers.append(i)
        print i
    return abundant_numbers

abundant = find_abundant_numbers(30001)
no_good_numbers = []

for i in range(len(abundant)):
    print i
    for j in range(len(abundant)):
        no_good_numbers.append(abundant[i]+abundant[j])

no_good_numbers = list(set(no_good_numbers))

p = filter(lambda x: x not in no_good_numbers, p)

print sum(p)



