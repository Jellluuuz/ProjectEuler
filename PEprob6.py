sum_squares = 0
sum_ints = 0
for i in range(101):
    sum_squares += i**2
for i in range(101):
    sum_ints += i
square_sums = sum_ints ** 2

print square_sums - sum_squares
