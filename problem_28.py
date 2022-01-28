def sum_spiral(size):
    total = 1
    increment = 0
    step = 1
    for _ in range(size//2):
        increment += 2
        for _ in range(4):
            step += increment
            total += step
    
    return total

if __name__ == '__main__':
    print(sum_spiral(1001))