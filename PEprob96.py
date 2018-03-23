import numpy as np
import copy
import time


def import_sudoku():
    sudoku_list = []
    with open('p096_sudoku.txt', 'r') as sudokus:
        for row in sudokus:
            row.replace("'", '')
            sudoku_list.append(row)
    sudoku_list = map(lambda s: s.strip(), sudoku_list)
    sudoku_list_in_form = []
    temp = []
    for ind, string in enumerate(sudoku_list):
        temp.append(string)

        if ind % 10 == 0:
            to_add = copy.deepcopy(temp)
            if ind > 0:
                sudoku_list_in_form.append(to_add[:-1])
            temp = []
        if str is sudoku_list[-1]:
            to_add = copy.deepcopy(temp)
            sudoku_list_in_form.append(to_add)

    d = {}
    counter = 0
    for j in sudoku_list_in_form:
        sudoku1 = []
        for k in j:
            temp = [int(x) for x in k]
#        temp.append([int(x) for x in j])
#        for char in j:
#            temp.append(char)
            sudoku1.append(temp)

        d[counter] = sudoku1
        counter += 1
    return d


sudoku_dict = import_sudoku()


def create_poss_mat(input_sudoku):
    possibility_mat = np.zeros((9, 9, 9))
    for i in range(9):
        for j in range(9):
            possibility_mat[i, j, :] = range(1, 10)
    for i in range(9):
        for j in range(9):
            if input_sudoku[i][j] != 0:
                possibility_mat[i][j][:] = 0
                for l in range(9):
                    # remove value on i,j from possibilities horizontally
                    possibility_mat[i][l][input_sudoku[i][j] - 1] = 0
                    # remove value on i,j from possibilities vertically
                    possibility_mat[l][j][input_sudoku[i][j] - 1] = 0
                if i < 3 and j < 3:
                    for temp1 in range(3):
                        for temp2 in range(3):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif i < 3 and j < 6:
                    for temp1 in range(3):
                        for temp2 in range(3, 6):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif i < 3:
                    for temp1 in range(3):
                        for temp2 in range(6, 9):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif i < 6 and j < 3:
                    for temp1 in range(3, 6):
                        for temp2 in range(3):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif i < 6 and j < 6:
                    for temp1 in range(3, 6):
                        for temp2 in range(3, 6):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif i < 6:
                    for temp1 in range(3, 6):
                        for temp2 in range(6, 9):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif j < 3:
                    for temp1 in range(6, 9):
                        for temp2 in range(3):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                elif j < 6:
                    for temp1 in range(6, 9):
                        for temp2 in range(3, 6):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
                else:
                    for temp1 in range(6, 9):
                        for temp2 in range(6, 9):
                            possibility_mat[temp1][temp2][input_sudoku[i][j] - 1] = 0
    return possibility_mat


def clean_poss_mat(possibility_mat, i, j, val):
    for l in range(9):
        # remove value on i,j from possibilities horizontally
        possibility_mat[i][l][val - 1] = 0
        # remove value on i,j from possibilities vertically
        possibility_mat[l][j][val - 1] = 0
    if i < 3 and j < 3:
        for temp1 in range(3):
            for temp2 in range(3):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif i < 3 and j < 6:
        for temp1 in range(3):
            for temp2 in range(3, 6):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif i < 3:
        for temp1 in range(3):
            for temp2 in range(6, 9):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif i < 6 and j < 3:
        for temp1 in range(3, 6):
            for temp2 in range(3):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif i < 6 and j < 6:
        for temp1 in range(3, 6):
            for temp2 in range(3, 6):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif i < 6:
        for temp1 in range(3, 6):
            for temp2 in range(6, 9):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif j < 3:
        for temp1 in range(6, 9):
            for temp2 in range(3):
                possibility_mat[temp1][temp2][val - 1] = 0
    elif j < 6:
        for temp1 in range(6, 9):
            for temp2 in range(3, 6):
                possibility_mat[temp1][temp2][val - 1] = 0
    else:
        for temp1 in range(6, 9):
            for temp2 in range(6, 9):
                possibility_mat[temp1][temp2][val - 1] = 0
    return possibility_mat


def valid_solution(sudoku_to_check):
    # check occurance of every value horizontally and vertically
    for val in range(1, 10):
        horizontal_counter = 0
        vertical_counter = 0
        for i in range(9):
            for j in range(9):
                if sudoku_to_check[i][j] == val:
                    horizontal_counter += 1
                if sudoku_to_check[j][i] == val:
                    vertical_counter += 1
        if horizontal_counter != 9 or vertical_counter != 9:
                return False

        block_counter = 0
        for i in range(3):
            for j in range(3):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(3):
            for j in range(3, 6):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(3):
            for j in range(6, 9):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(3, 6):
            for j in range(3):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(3, 6):
            for j in range(3, 6):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(3, 6):
            for j in range(6, 9):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(6, 9):
            for j in range(3):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(6, 9):
            for j in range(3, 6):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False
        block_counter = 0
        for i in range(6, 9):
            for j in range(6, 9):
                if sudoku_to_check[i][j] == val:
                    block_counter += 1
        if block_counter != 1:
            return False

    return True


def check_attempt_possible(poss_mat_to_check, i ,j, val):
    poss_mat_copy = copy.deepcopy(poss_mat_to_check)
    poss_mat_copy = clean_poss_mat(poss_mat_copy, i, j, val)
    for row in range(9):
        for column in range(9):
            number_of_poss = 0
            for k in range(9):
                if poss_mat_copy != 0:
                    number_of_poss += 1
                    break
            if number_of_poss == 0:
                return False
    return True




def solve(sudoku_to_solve, possibility_mat):
    loc = 0
    sudoku_to_solve = copy.deepcopy(sudoku_to_solve)
    setting = True
    while setting:
        setting = False
        for i in range(9):
            for j in range(9):
                count = 0
                if sudoku_to_solve[i][j] == 0:
                    for k in range(9):
                        if possibility_mat[i][j][k] != 0:
                            count += 1
                            loc = k
                    if count == 1:
                        setting = True
                        sudoku_to_solve[i][j] = int(possibility_mat[i][j][loc])
                        possibility_mat = clean_poss_mat(possibility_mat, i, j, int(sudoku_to_solve[i][j]))

    # check if sudoku is fully solved
    solve_counter = 0
    for i in range(9):
        for j in range(9):
            if sudoku_to_solve[i][j] == 0:
                solve_counter += 1
    if solve_counter != 0:
        print 'Beware, this SuDoku is not fully solved'
    return sudoku_to_solve, possibility_mat


def test_recursion(sudoku_to_recurse, poss_mat):
    solve_counter = 0
    for i in range(9):
        for j in range(9):
            if sudoku_to_recurse[i][j] == 0:
                solve_counter += 1
    if solve_counter == 0:
        if valid_solution(sudoku_to_recurse):
            return sudoku_to_recurse
        else:
            return None
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if poss_mat[i][j][k] != 0:
                    if check_attempt_possible(poss_mat, i, j, poss_mat[i][j][k]):
                        temp_sudoku = copy.deepcopy(sudoku_to_recurse)
                        temp_sudoku[i, j] = poss_mat[i][j][k]
                        temp_poss_mat = clean_poss_mat(poss_mat, i, j, poss_mat[i][j][k])
                        return test_recursion(temp_sudoku, temp_poss_mat)
                else:
                    return

    # DOE DE RECURSIE HIER TOEVOEGEN DOEN!!!!


t = time.time()

print sudoku_dict[48]
for i in range(49):
    sudoku = sudoku_dict[i]
    poss_mat = create_poss_mat(sudoku)
    print '---'
    print i
    sudoku, poss_mat = solve(sudoku, poss_mat)
'''
sudoku = sudoku_dict[0]
print sudoku
poss_mat = create_poss_mat(sudoku)
solution = solve(sudoku, poss_mat)
print test_recursion(sudoku, poss_mat)
'''

# sum(solution[0][0:3])   <-- het op te tellen deel per sudoku
