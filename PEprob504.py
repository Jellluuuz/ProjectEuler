import time

def check_contained_lattice_points(a,b,c,d):
    ab = float(b)/-a
    bc = float(b)/-c
    cd = float(-d)/c
    da = float(-d)/a

    for i in range(-c + 1, a):
        for j in range(-d + 1, b):
            if i >= 0:
                if j >= 0:
                    if j * ab > ab + b:
                        return False