import time

N = 100000

def create_triangle_list(k):
    return [i*(i+1)/2 for i in range(1, k)]


def create_pentagonal_list(k):
    return [i*(3*i-1)/2 for i in range(1, k)]


def create_hexagonal_list(k):
    return [i*(2*i-1) for i in range(1, k)]

def check_pentagonal(k):
    if (float((1./2 + math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 + math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    elif (float((1./2 - math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 - math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    else:
        return False


def check_hexagonal(k):
    if (float((1./2 + math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 + math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    elif (float((1./2 - math.sqrt(1./4 + 6*k)))/3).is_integer() and float((1./2 - math.sqrt(1./4 + 6*k)))/3 > 0:
        return True
    else:
        return False

t = time.time()

triangle_list = create_triangle_list(N)
pentagonal_list = create_pentagonal_list(N)
hexagonal_list = create_hexagonal_list(N)
'''
if len(triangle_list) < len(pentagonal_list) and len(triangle_list) < len(hexagonal_list):
    starting_list = triangle_list
elif len(pentagonal_list) < len(triangle_list) and len(pentagonal_list) < len(hexagonal_list):
    starting_list = pentagonal_list
else:
    starting_list = hexagonal_list
'''
correct_number = []
for i in pentagonal_list:
    if i in triangle_list and i in hexagonal_list:
        correct_number.append(i)

print correct_number

print t-time.time()