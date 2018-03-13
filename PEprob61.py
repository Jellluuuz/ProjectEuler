import time

t = time.time()

triangle = [i*(i+1)/2 for i in range(40, 150)]
real_triangle = [x for x in triangle if len(str(x)) == 4]

square = [i**2 for i in range(30, 101)]
real_square = [x for x in square if len(str(x)) == 4]

pentagonal = [i*(3*i-1)/2 for i in range(20, 101)]
real_pentagonal = [x for x in pentagonal if len(str(x)) == 4]

hexagonal = [i*(2*i-1) for i in range(20, 101)]
real_hexagonal = [x for x in hexagonal if len(str(x)) == 4]

heptagonal =[i*(5*i - 3)/2 for i in range(20, 101)]
real_heptagonal = [x for x in heptagonal if len(str(x)) == 4]

octagonal =[i*(3*i - 2) for i in range(15, 70)]
real_octagonal = [x for x in octagonal if len(str(x)) == 4]


total_numbers = []
total_numbers.append(real_triangle)
total_numbers.append(real_square)
total_numbers.append(real_pentagonal)
total_numbers.append(real_hexagonal)
total_numbers.append(real_heptagonal)
total_numbers.append(real_octagonal)


print total_numbers

for i in total_numbers[0]:
    for q1 in range(1,6):
        for j in total_numbers[q1]:
            if str(i)[-2:] == str(j)[:2]:
                for q2 in range(1, 6):
                    if q1 == q2:
                        continue
                    for k in total_numbers[q2]:
                        if str(j)[-2:] == str(k)[:2]:
                            for q3 in range(1,6):
                                if q3 == q1 or q3 == q2:
                                    continue
                                for l in total_numbers[q3]:
                                    if str(k)[-2:] == str(l)[:2]:
                                        for q4 in range(1, 6):
                                            if q4 == q1 or q4 == q2 or q4 == q3:
                                                continue
                                            for m in total_numbers[q4]:
                                                if str(l)[-2:] == str(m)[:2]:
                                                    for q5 in range(1,6):
                                                        if q5 == q1 or q5 == q2 or q5 == q3 or q5 == q4:
                                                            continue
                                                        for n in total_numbers[q5]:
                                                            if str(m)[-2:] == str(n)[:2] and str(n)[-2:] == str(i)[:2]:
                                                                print i
                                                                print j
                                                                print k
                                                                print l
                                                                print m
                                                                print n
                                                                print i + j + k + l + m + n


print time.time() - t