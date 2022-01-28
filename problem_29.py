# each number is made up of a combination of primes
# each unique "base" will add 100 unique elements
# each non-unique "base" could still add new elements if it extends beyond the original's reach
# e.g. 2^100 == 4^50, so 4 will add 50 elements
#      4^100 == 16^50
# but 8 and 16 overlap so need to apply logic carefully

# 2, 4 & 8 with 5
# 2, 2^2, 2^3, 2^4, 2^5
# 2^2, 2^4, 2^6, 2^8, 2^10
# 2^3, 2^6, 2^9, 2^12, 2^15

def get_steps(checked, i):
    seen = {i}

    x = i
    step = 1
    while x < len(checked):
        checked[x] = True
        limit = len(checked) - 1
        possible_steps = range(2*step, (step*limit)+1, step)
        seen.update(possible_steps)
        x *= i
        step += 1

    return len(seen)

def solve(target):

    checked = [False] * (target+1)
    answer = 0
    for i in range(2, len(checked)):
        if not checked[i]:
            answer += get_steps(checked, i)

    print(answer)

if __name__ == '__main__':
    solve(5)
    solve(100)