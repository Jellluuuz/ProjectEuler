import time
import itertools


def conv_to_string(perm_tuple):
    temp = ''
    for char in perm_tuple:
        temp = temp + str(char)
    return int(temp)


t = time.time()

valid_sols = []
for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    counter = 0
    if i[9] + i[0] == i[2] + i[3] and \
        i[2] + i[1] == i[4] + i[5] and \
        i[4] + i[3] == i[6] + i[7] and \
        i[6] + i[5] == i[8] + i[0]:
        valid_sols.append(i)

print len(valid_sols)
real_valid_sols = []
for i in valid_sols:
    if i[9] < i[2] and i[9] < i[4] and i[9] < i[6] and i[9] < i[8]:
        if i[0] != 10 and i[1] != 10 and i[3] != 10 and i[5] != 10 and i[7] != 10:
            real_valid_sols.append((i[9], i[0], i[1], i[2], i[1], i[3], i[4], i[3], i[5],
                                      i[6], i[5], i[7], i[8], i[7], i[0]))


int_real_valid_sols = []
for i in real_valid_sols:
    int_real_valid_sols.append(conv_to_string(i))

print max(int_real_valid_sols)

print time.time() - t
