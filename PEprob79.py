import csv

keys = []
with open('p079_keylog.txt') as keylog:
    for row in keylog:
        keys.append(int(row))

indices = []
for i in range(10):
    temp_index = []
    for j in keys:
        string = []
        for k in str(j):
            string.append(int(k))
        try:
            temp_index.append(string.index(i))
        except ValueError:
            continue
    indices.append(temp_index)

print indices

MET PET EN PAPIER OPGELOST


