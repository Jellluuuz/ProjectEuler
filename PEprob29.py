import time


t = time.time()
results = []
for i in range(2, 101):
    for j in range(2, 101):
        a = i ** j
        if a not in results:
            results.append(a)

print len(results)
print time.time() - t