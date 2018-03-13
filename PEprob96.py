import numpy as np

#Sudoku = np.zeros((9,9))
Sudoku = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


poss_mat = np.zeros((9,9,9))


def create_poss_mat(sudoku):
    for i in range(9):
        for j in range(9):
            poss_mat[i, j, :] = range(1, 10)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                poss_mat[i][:][sudoku[i][j]-1] = 0
                poss_mat[:][j][sudoku[i][j]-1] = 0

print poss_mat[0]
create_poss_mat(Sudoku)
#print poss_mat
