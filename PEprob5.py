check = True
i = 1
while check == True:
    for k in range(1,21):
        if i % k != 0:
            break
        if k == 20:
            print i
            check = False            
            break
    i += 1

