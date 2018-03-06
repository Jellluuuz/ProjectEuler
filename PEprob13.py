import csv
import string

results = []
with open('prob_13.txt') as prob_13:
    for row in csv.reader(prob_13):
        results.append(row)

print results
S = 0
for i in results:
    print int(i[0])
    S += int(i[0])

print S