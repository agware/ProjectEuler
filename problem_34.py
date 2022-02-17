import math

# ToDo: Optimise further!

def digit_factorials(next_digit, stem, stem_sum):

    if len(stem) == 0:
        val = str(next_digit)
    else:
        val = str(next_digit) + stem

    # rough ceiling based on 7*9! = 2,540,160 < 9,999,999
    if len(val) > 7:
        return 0

    new_sum = math.factorial(next_digit) + stem_sum

    total = 0
    if val == str(new_sum) and val[0] != 0 and len(val) > 1:
        total += int(val)

    for i in range(10):
        total += digit_factorials(i, val, new_sum)
    
    return total


if __name__ == '__main__':
    total = 0
    for i in range(10):
        total += digit_factorials(i, '', 0)
    print(total)