import csv
import numpy as np

matrix = []
with open('p081_matrix.txt') as p081_matrix:
    for row in csv.reader(p081_matrix):
        matrix.append(row)

sum_matrix = np.zeros((80, 80))
sum_matrix[0][0] = matrix[0][0]


def expand(i, j):
    if i < 79:
        temp_right = int(sum_matrix[i][j]) + int(matrix[i+1][j])
        if temp_right < sum_matrix[i+1][j] or sum_matrix[i+1][j] == 0:
            sum_matrix[i+1][j] = temp_right
    if j < 79:
        temp_bottom = int(sum_matrix[i][j]) + int(matrix[i][j+1])
        if temp_bottom < sum_matrix[i][j+1] or sum_matrix[i][j+1] == 0:
            sum_matrix[i][j+1] = temp_bottom
    return sum_matrix

for i in range(80):
    for j in range(80):
        expand(i,j)



print sum_matrix
