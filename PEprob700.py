import numpy as np
import math
from fractions import gcd



def lcm(a, b):
    return abs(a*b) // gcd(a, b)

print lcm(1504170715041707, 4503599627370517)

for i in range(100):
    print (1504170715041707*i) % 4503599627370517