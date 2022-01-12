from utils import prime_sieve

target = 10001

# this solution doesn't feel particularly in 
# the spirit of the problem

primes = prime_sieve(200000)
print(primes[target-1])