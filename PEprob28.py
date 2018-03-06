import time

numbers = range(1, 1001**2+2)

S = 0
i = 0
j = 0
while i < 1001**2-1:
    sub_count = 0
    j += 2
    while sub_count < 4:
        S += numbers[i]
        print numbers[i]
        i += j
        sub_count += 1

print S + numbers[i]
