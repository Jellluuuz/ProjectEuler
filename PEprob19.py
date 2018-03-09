''' list of month lengths '''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
''' A little bit of research revealed the day of the week
 on Jan. 1, 1901 (Tuesday)'''
day = 2
acc = 0 #accumulator
for year in range(1901, 2001):
    for month in range(12):
        m = months[month] # get month length
        if day == 0:
            acc += 1
        #if month is Feb and its a leap year, add one to its length
        if m == 28 and year % 4 == 0:
            m += 1
        for d in range(m):
            #just keep track of the day

            if day == 6:
                day = 0
            else:
                day += 1
print(acc)