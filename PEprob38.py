import time

def pan_prod(n,k):
    string = ''
    for char in (k):
        string = string + str(n * char)
    return int(string)


def check_pandigital(n):
    if len(str(n)) != 9:
        return False
    for q in range(1,10):
        if str(n).count(str(q)) != 1:
            return False
    return True


t = time.time()
my_list = []
for i in range(2,10):
    a = tuple(range(1, i+1))
    print a
    for j in range(1, 100000):
        number = pan_prod(j, a)
        if len(str(number)) > 9:
            break
        if check_pandigital(number):
            my_list.append(number)
            if number == 935218704:
                print a,j

print my_list
print max(my_list)




print 'time is %f' %(time.time() -t)