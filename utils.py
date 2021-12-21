def prime_sieve(target):
    flags = [0] * target
    flags[0] = 1

    primes = []
    for i in range(target):
        if flags[i] ==  0:
            prime = i + 1
            primes.append(prime)

            for j in range(i + prime, target, prime):
                flags[j] = 1
    
    return primes