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

def get_abundant(factors):
    abundant = [False] * len(factors)

    for i in range(2, len(factors)):
        if i < sum(factors[i]):
            abundant[i] = True

    return abundant

def total_non_abundant_sum(target, abundant):
    total = 0
    for i in range(1, target):
        has_match = False
        for j in range(12, i//2 + 1):
            if abundant[j] and abundant[i-j]:
                has_match = True
                break
        
        if not has_match:
            total += i
    
    return total

if __name__ == '__main__':
    limit = 28123
    factors = get_factors(limit)
    abundant = get_abundant(factors)
    print(total_non_abundant_sum(limit, abundant))