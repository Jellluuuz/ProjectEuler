import numpy as np
import time

t1 = time.time()
p = np.arange(2,2000000,1).tolist()
i = 0

while i < 1415:
    '''
    check = True
    for j in range(i):
        if p[i] % p[j] == 0:
            del p[i]
            check = False
    if check:
        i += 1
    print i
    '''
        
     
        
        
    j = 1
    while j < len(p)-i:
        current_prime = p[i]
        if p[j+i] % current_prime == 0:
            del p[j+i]
#            p.pop(i+j)
        else:
            j += 1
#            print j
    i += 1      
    print i
print p
    
s = sum(p)
print s
print time.time()-t1

