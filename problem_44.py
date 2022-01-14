# P(n) = n * (3n - 1)/2

# P(n+1) - P(n) = 3n + 1

queue = {0: [(1, 2)]}

count = 0
next_add = (1, 3)
next_index = 2
count_added = 1

def calc_pentagonal(n):
    return n * (3*n - 1)/2

while count < 30:
    print('\nCount:', count)

    if count == next_index:
        queue[count].append(next_add)
        next_index += next_add[1]
        next_add = (next_add[0], next_add[1]+1)

        count_added += 1
        if count_added % 3 == 0:
            next_index += 1

    check = queue.pop(count)
    for node in check:
        x1 = calc_pentagonal(node[0])
        x2 = calc_pentagonal(node[1])

        difference = x2 - x1
        print(node, '-', difference)
        
        next_node = (node[0]+1, node[1]+1)
        increment = node[1] - node[0]

        key = count + increment
        if count + increment in queue:
            queue[key].append(next_node)
        else:
            queue[key] = [next_node]
    
    count += 1