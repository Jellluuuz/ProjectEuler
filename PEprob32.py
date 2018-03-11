import itertools
import time


def check_number(n):
    for i in range(1,9):
        for j in range(i+1,9):
            if int(str(n)[:i]) * int(str(n)[i:j]) == int(str(n)[j:]):
                print int(str(n)[:i]), int(str(n)[i:j]), int(str(n)[j:]), n
                return int(str(n)[j:])
#for i in itertools.permutations([1,2,3,4,5,6,7,8,9]):

t = time.time()
numbers = []
for i in itertools.permutations([1,2,3,4,5,6,7,8,9]):
    string = ''
    for j in i:
        string = string + str(j)
    a = check_number(int(string))
    if a and a not in numbers:
        numbers.append(a)
print numbers
print sum(numbers)

print time.time() - t