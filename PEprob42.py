import csv
import string

results = []
with open('p042_words.txt') as p042_words:
    for row in csv.reader(p042_words):
        results.append(row)

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 1

triangle_values = [(n*(n+1))/2 for n in range(1, 20)]


def assign_value(word,value):
    word_value = 0
    for k in word:
        word_value += value[k]
    return word_value

count = 0
for i in results:
    for j in i:
        if assign_value(j, values) in triangle_values:
            count += 1

print count
