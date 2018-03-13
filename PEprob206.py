import time

t = time.time()

for i in range(10 ** 7, 10**8):
    number = str(int( '1' + str(i) + '0') ** 2)
    if int(number[0]) != 1 or int(number[2]) != 2 or int(number[4]) != 3 or int(number[6]) != 4 or int(number[8]) != 5 or int(number[10]) != 6 or int(number[12]) != 7 or int(number[14]) != 8 or int(number[16]) != 9 or int(number[18]) != 0:
        continue
    else:
        print 'DIT WORDT EM'
        print int( '1' + str(i) + '0')
        print time.time() - t
        exit()



for i in range(1000):
    if str(i**2)[-1] == 0:
        print i

