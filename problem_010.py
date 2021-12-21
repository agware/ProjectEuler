from utils import prime_sieve

target = 2000000
primes = prime_sieve(target)

total = 0
for x in primes:
    total += x

print(total)