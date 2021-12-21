# get a bunch of prime numbers

# for each triangle number, find all its factors

# have fun with combinatorics

from utils import prime_sieve

import math

target = 500

primes = prime_sieve(2000)

def get_factors(target, primes):
    factors = {}
    for i in range(len(primes)):
        prime = primes[i]
        while True:
            if target % prime != 0:
                break
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1
            target = target // prime
        
        if target == 1:
            return factors
    
    return factors

def get_combinations(n, length):
    if n == length:
        return 1
    
    if length == 1:
        return n
    
    numerator = math.factorial(n)
    denominator = math.factorial(length) * math.factorial(n-length)
    return numerator/denominator


i = 1
total = 0
while True:
    total += i

    factors = get_factors(total, primes)
    
    num_factors = 1

    for key, count in factors.items():
        num_factors *= (count + 1)

    if num_factors > target:
        print(total)
        break

    i += 1
    
    

    
    