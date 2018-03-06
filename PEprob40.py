p = ''

for i in range(1,200000):
    p = p + str(i)

#print p

print int(p[0])*int(p[9])*int(p[99])*int(p[999])*int(p[9999])*int(p[99999])*int(p[999999])
