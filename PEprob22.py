import csv
import functools
import locale
import time


def word_to_value(string):
    val = 0
    for char in string:
        val += ord(char) - 96
    return val


t = time.time()

with open('p022_names.txt', 'r') as names:
    names_string = names.read().lower()
names_string = sorted(names_string.replace('"', '').split(","), key=functools.cmp_to_key(locale.strcoll))

print names_string[0]

total_val = 0
for i in names_string:
    total_val += word_to_value(i) * (names_string.index(i)+1)

print total_val

print time.time() - t