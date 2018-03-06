abundants = set(i for i in range(1,28124) if d(i) > i)

def abundantsum(i):
    return any(i-a in abundants for a in abundants)

print sum(i for i in range(1,28124) if not abundantsum(i))
