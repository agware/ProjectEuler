import math

def get_factors(target):
    factors = [{1} for _ in range(target + 1)]

    for x in range(2, target+1):
        limit = math.floor(math.sqrt(x))
        for i in range(2, limit+1):
            if x % i == 0:
                factors[x].add(i)
                factors[x].add(x // i)
    
    return factors

def get_amicable_sum(factors):

    total = 0
    for i in range(2, len(factors)):
        val = sum(factors[i])
        if i < val < len(factors):
            if i == sum(factors[val]):
                total += i + val

    return total


if __name__ == '__main__':
    target = 10000
    factors = get_factors(target - 1)
    print(get_amicable_sum(factors))
