def number_of_hexagons(n):
    count = 0
    for i in range(1,n/3+1):
        count += ((n-3*i + 1) * ((n-3*i + 1)+1))/ 2
    return count

print number_of_hexagons(20)
'''
sum = 0
for i in range(3,12346):
    if i % 1000 == 0:
        print i
    sum += number_of_hexagons(i)

print sum
'''


#ook nog hexagons die niet over de lattice lijnen lopen, lengte wortel(3)