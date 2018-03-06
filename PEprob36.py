import time

def check_palindrome(n):
    setting = True
    for i in range(len(str(n))/2+1):
        if str(n)[i] != str(n)[-(i+1)]:
            return False
    return setting




palindromes = []
for i in range(1,1000000):
    if check_palindrome(i):
        palindromes.append(i)



valid = []
for i in palindromes:
    if check_palindrome(bin(i)[2:]):
        valid.append(i)

print sum(valid)



t = time.time()
#print palindromes
print time.time() - t
