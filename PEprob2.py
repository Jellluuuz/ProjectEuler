total_count = 0
count1 = 0 
count2 = 1
while count1 < 4000001:
    count1 = count1 + count2
    count2 = count1 + count2
    if count1 % 2 == 0:
        total_count += count1
    if count2 % 2 == 0:
        total_count += count2
print total_count
