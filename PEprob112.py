import time

def check_number(n):
    string = str(n)
    if string[1] > string[0]:
        for i in range(1,len(string)-1):
            if string[i+1] < string[i]:
                return True
        if string[-1] < string[-2]:
            return True
        return False
    elif string[1] < string[0]:
        for i in range(1,len(string)-1):
            if string[i+1] > string[i]:
                return True
        if string[-1] > string[-2]:
            return True
        return False
    else:
        try:
            return check_number(string[1:])
        except IndexError:
            print string
            return False





def check_ratio(k):
    count = 0
    for i in range(11,k):
        if check_number(i):
            count += 1
            print i
    return count/float(k)



#for i in range(100,21780):
#    if not check_number(i):
#        print i
#print check_ratio(21780)

t = time.time()
p = 0
i = 100
count = 0
while p <= .99:
    i += 1
    if check_number(i):
        count += 1
        p = count/float(i)
    print count
    print p

print 'answer is %d' % (i-1)


print 'time is %f' %(time.time()-t)