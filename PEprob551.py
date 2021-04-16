import time

sequence = [1]
current_sum = [1]

def sum_over_digits(number):
    total = 0
    for char in str(number):
        total += int(char)
    return total

dummy = 20

t0 = time.time()

for i in range(dummy):
    sequence.append(current_sum[-1])
    current_sum.append(current_sum[-1] + sum_over_digits(sequence[-1]))

print time.time() - t0

print sequence
print current_sum
