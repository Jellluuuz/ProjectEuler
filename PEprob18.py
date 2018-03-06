import time
 
# read file
rows = []
FILE = open("p018_triangle.txt", "r")
for blob in FILE: rows.append([int(i) for i in blob.split(" ")])
 
start = time.time()

for i,j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:
    rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])
t1 = time.time() - start


def traverse(i,j):
    if i == len(rows)-2:
        return max(rows[i+1][j],rows[i+1][j+1]) + rows[i][j]
    return max(traverse(i+1,j),traverse(i+1,j+1)) + rows[i][j]


start = time.time()
waarde = traverse(0,0) 
t2 = time.time()-start   
elapsed = time.time() - start
 
print "Brute force: %s seconds" % (t1)
print "Dynamic Programming: %s seconds" % (t2)
print "Differs factor %d for n = 15" %(t2/t1)
