import csv
import numpy as np
import copy
import time

t = time.time()

matrix = []
with open('p081_matrix.txt') as p081_matrix:
    for row in csv.reader(p081_matrix):
        matrix.append(row)

sum_matrix = np.zeros((80, 80))
for i in range(80):
    sum_matrix[i][0] = int(matrix[0][i])


def check_equal(a, b):
    for i in range(80):
        for j in range(80):
            if a[i][j] != b[i][j]:
                return False
    return True


def one_step_right(sum_matrix, j):
    for i in range(80):
        sum_matrix[i][j] = sum_matrix[i][j-1] + int(matrix[i][j])
    return sum_matrix


def check_better(sum_matrix, j):
    for i in range(80):
        try:
            if sum_matrix[i][j] > sum_matrix[i - 1][j] + int(matrix[i][j]):
                sum_matrix[i][j] = sum_matrix[i - 1][j] + int(matrix[i][j])
        except IndexError:
            pass
        try:
            if sum_matrix[i][j] > sum_matrix[i + 1][j] + int(matrix[i][j]):
                sum_matrix[i][j] = sum_matrix[i + 1][j] + int(matrix[i][j])
        except IndexError:
            pass
    return sum_matrix


for j in range(1, 80):
    sum_matrix = one_step_right(sum_matrix, j)
    while True:
        temp = copy.deepcopy(sum_matrix)
        sum_matrix = check_better(sum_matrix, j)
        if check_equal(sum_matrix, temp):
            break

min_val = 10**6
for i in range(80):
    if sum_matrix[i][-1] < min_val:
        min_val = sum_matrix[i][-1]
print min_val
print time.time() - t