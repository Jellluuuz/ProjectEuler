def check_number(k):
    S = 0
    for char in str(k):
        S += int(char) ** 5
    return S == k

numbers = []
for i in range(1000000):
    if check_number(i):
        numbers.append(i)

print numbers
print sum(numbers)-1