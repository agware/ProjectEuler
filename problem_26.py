def get_length_recurring(divisor):
    numerator = 1

    remainders = set()
    while numerator > 0:
        remainders.add(numerator)

        numerator *= 10
        numerator %= divisor

        if numerator in remainders:
            break

    return len(remainders)

def solve(limit):

    max_length = 0
    answer = None
    for i in range(2, limit):
        length = get_length_recurring(i)
        if length > max_length:
            max_length = length
            answer = i

    print(answer)

if __name__ == '__main__':
    solve(10)
    solve(1000)
