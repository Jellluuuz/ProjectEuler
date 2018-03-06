'Little Fermat"s theorem: a^p = a mod p'

from find_prime_factorization import is_prime

poss_ans = []
for i in range(1,100):
    a = i*7830457*28433+3
    if a % 2 != 0 and a % 5 != 0:
        poss_ans.append(str(a)[-10:])

print poss_ans

misschien toch niet