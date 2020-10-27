import time


def number_check(n):
    S = 0
    for char in str(n):
        S += int(char)
    if S == 1:
        return False
    i = 1
    temp = S
    while temp <= n:
        temp = S ** i
        if temp == n:
            return True
        i += 1
    return False


t = time.time()


count = 0
j = 10
sol_list = []
while count < 30:
    if number_check(j):
        sol_list.append(j)
        count += 1
        print j
    j += 1

print sol_list
print sol_list[30]

print time.time() - t

#i aflopen
#op hoeveel manieren kan je 28 schrijven ----<
#machten van die manieren checken
