import time


count = 0


def build_str(string):
    if len(string) == 30:
        global count
        count += 1
        return

    build_str(string + 'O')
    if 'L' not in string:
        build_str_2(string + 'L')
    try:
        if string[-1] is not 'A' or string[-2] is not 'A':
            build_str(string + 'A')
    except IndexError:
        build_str(string + 'A')


def build_str_2(string):
    if len(string) == 30:
        global count
        count += 1
        return
    build_str_2(string + 'O')
    try:
        if string[-1] is not 'A' or string[-2] is not 'A':
            build_str_2(string + 'A')
    except IndexError:
        build_str_2(string + 'A')


t = time.time()

build_str('')

print count

print time.time() - t
