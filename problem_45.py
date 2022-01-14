import math

def is_triangular(n):
    determinant = 1 + 8*n
    root = math.isqrt(determinant)
    if root**2 != determinant:
        return False
    return (root - 1) % 2 == 0

def is_pentagonal(n):
    determinant = 1 + 24*n
    root = math.isqrt(determinant)
    if root**2 != determinant:
        return False
    return (1 + root) % 6 == 0

def calc_hexagonal(n):
    return n*(2*n - 1)

count = 144     # starting from immediately after the provided solution
while True:
    value = calc_hexagonal(count)

    if is_triangular(value):
        if is_pentagonal(value):
            print(value)
            break
    
    count += 1