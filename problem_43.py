def has_duplicates(digits):
    return len(digits) != len(set(digits))

def add_possibility(digits, additional, possible):
    front = (digits[0], digits[1])
    additional = str(digits[2]) + additional

    if front in possible:
        possible[front].append(additional)
    else:
        possible[front] = [additional]

def check_additional(digits, possible, next_possible):
    stem = (digits[1], digits[2])
    if stem not in possible:
        return None
    
    for additional in possible[stem]:
        if str(digits[0]) not in additional:
            add_possibility(digits, additional, next_possible)


def get_possible(divisor, possible=None):
    next_possible = {}

    for num in range(divisor, 1000, divisor):
        digits = [num//100, (num//10) % 10, num % 10]
        if not has_duplicates(digits):
            if possible is None:
                add_possibility(digits, '', next_possible)
            else:
                check_additional(digits, possible, next_possible)
    
    return next_possible

possible = None
for x in [17, 13, 11, 7, 5, 3, 2]:
    possible = get_possible(x, possible)

total = 0
for key, val in possible.items():
    for stem in val:
        final = str(key[0]) + str(key[1]) + stem
        remainder = set('0123456789').difference(set(final))
        total += int(remainder.pop() + final)

print(total)