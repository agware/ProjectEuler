squares = [1, 4, 9]

target = 1000

i = len(squares) + 1
matched = False
while not matched:
    outcome = i ** 2
    
    min_index = 0
    max_index = len(squares)-1

    while min_index < max_index:
        tmp_result = outcome - squares[max_index]
        
        # discard all the impossible options
        while min_index < len(squares)-1 and squares[min_index] < tmp_result:
            min_index += 1
        
        # check if a possible match has been found
        if squares[min_index] == tmp_result:
            # check if it matches the target sum
            if min_index + max_index + 2 + i == target:
                print(str([min_index+1, max_index+1, i]))
                matched = True
                break
        
        max_index -= 1
    
    squares.append(outcome)
    i += 1