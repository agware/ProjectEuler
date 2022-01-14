# P(n) = n * (3n - 1)/2

# P(n+1) - P(n) = 3n + 1

import math

def calc_pentagonal(n):
    return n * (3*n - 1)//2


def is_pentagonal(n):
    determinant = 1 + 24*n
    root = math.isqrt(determinant)
    if root**2 != determinant:
        return False
    
    return (1 + root) % 6 == 0


def check_options(queue, count):
    nodes = queue.pop(count)
    for node in nodes:
        x1 = calc_pentagonal(node[0])
        x2 = calc_pentagonal(node[1])

        difference = x2 - x1
        if is_pentagonal(difference):
            total = x2 + x1
            if is_pentagonal(total):
                print(node)
                print(difference)
                return True
        
        next_node = (node[0]+1, node[1]+1)
        increment = node[1] - node[0]

        key = count + increment
        if count + increment in queue:
            queue[key].append(next_node)
        else:
            queue[key] = [next_node]
    
    return False

queue = {0: [(1, 2)]}

count = 0
next_add = (1, 3)
next_index = 2
count_added = 1

found_solution = False
while not found_solution:

    if count == next_index:
        queue[count].append(next_add)
        next_index += next_add[1]
        next_add = (next_add[0], next_add[1]+1)

        count_added += 1
        if count_added % 3 == 0:
            next_index += 1

    found_solution = check_options(queue, count)
    
    count += 1