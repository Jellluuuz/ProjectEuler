import csv
import math
import operator

spamReader = csv.reader(open('p099_base_exp.txt'), delimiter=',', quotechar='|')

numbers = []
for row in spamReader:
    numbers.append(row)

for i in numbers:
    i[0] = int(i[0])
    i[1] = int(i[1])

exps = []
for i in numbers:
    i[1] = i[1] * math.log(i[0],2)
    exps.append(i[1])

print exps


index, value = max(enumerate(exps), key=operator.itemgetter(1))
print index + 1
print numbers[index][0]
