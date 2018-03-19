import time


t = time.time()

maxi_a = 0
maxi_b = 0
maxi_sum = 0

for a in range(100):
    for b in range(100):
        temp_sum = 0
        temp = a ** b
        for i in str(temp):
            temp_sum += int(i)
            if temp_sum > maxi_sum:
                maxi_a = a
                maxi_b = b
                maxi_sum = temp_sum

print maxi_sum, maxi_a, maxi_b
print time.time() - t