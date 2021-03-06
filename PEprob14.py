import time


def create_chain(n):
    chain = [n]
    while n != 1:
        if n % 2 == 1:
            n = 3*n+1
        else:
            n = n/2
        chain.append(n)
    return len(chain)


def find_max_chain(n):
    starting_number, length = [1, 1]
    for i in range(1, n):
        temp_length = create_chain(i)
        if temp_length > length:
            starting_number, length = i, temp_length
#       print starting_number,length
    return starting_number, length


time1 = time.time()

print find_max_chain(1000000)

print time.time() - time1
