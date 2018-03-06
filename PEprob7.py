def create_primes(n):
    primes = []
    i = 1
    while len(primes) < n:
        i += 1
        count = 0
        for k in range(1,i):
            if i % k == 0:
                count += 1
        if count == 1:
            primes.append(i)
        if len(primes) % 100 == 0:
            print len(primes)
    print primes    
    return primes

list1 = create_primes(10002)

            
            
