import csv


numerals = []
with open('p089_roman.txt') as p089_roman:
    for row in csv.reader(p089_roman):
        numerals.append(row)


print numerals

