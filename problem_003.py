from utils import prime_sieve

import math

target = 600851475143

factor_limit = int(math.floor(math.sqrt(target)))
primes = prime_sieve(factor_limit)

for i in range(len(primes)):
    prime = primes[-i-1]
    if target % prime == 0:
        print(prime)
        break
