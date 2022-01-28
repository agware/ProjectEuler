from utils import prime_sieve

# b must always be prime (for the n=0 case)

# max possible value is 
# n^2 + 1000n + 1000
# with an unknown n
# a can also be negative

# ballpark n at 200 for now and sieve primes up to 
# 241 000

limit = 1000

b_primes = prime_sieve(limit)
all_primes = set(prime_sieve(241000))

max_length = 0
answer = 0
for b in b_primes:
    for a in range(-1*limit + 1, limit):
        n = 1
        while True:
            if (n**2 + a*n + b) not in all_primes:
                break
            n += 1
        
        if n > max_length:
            max_length = n
            answer = a * b

print(max_length)
print(answer)

