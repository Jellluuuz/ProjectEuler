i = 999
j = 999
palindromes = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        number = i*j
        string = str(number)    
        l = len(string)
        check = True
        for k in range(l):
            if string[k] != string[l-k-1]:
                check = False
        if check == True:
            palindromes.append(number)
print palindromes
print max(palindromes)    

