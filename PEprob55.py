import time


def check_palindrome(n):
    setting = True
    for i in range(len(str(n))/2+1):
        if str(n)[i] != str(n)[-(i+1)]:
            return False
    return setting


def reverse(n):
    string = ''
    for char in reversed(str(n)):
        string = string + char
    return int(string)


def evolve(n):
    return n + reverse(n)


def check_lychrel(n):
    state = True
    count = 0
    while count < 50:
        count += 1
        n = evolve(n)
        if check_palindrome(n):
            state = False
            break
            print count
    return state

print check_lychrel(196)
S = 0
for i in range(1,10000):
    if check_lychrel(i):
        S += 1

print S


