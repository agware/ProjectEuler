from utils import prime_sieve

import math

target = 20

primes = prime_sieve(target)

total = 1
for x in primes:
    power = int(math.floor(math.log(target,x)))
    total *= x ** power

print(total)