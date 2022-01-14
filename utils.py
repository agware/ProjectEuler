def prime_sieve(target):
    limit = target + 1
    flags = [True] * limit
    flags[0] = False
    flags[1] = False

    primes = []
    for i in range(limit):
        if flags[i]:
            prime = i
            primes.append(prime)

            for j in range(i + prime, limit, prime):
                flags[j] = False
    
    return primes


if __name__ == '__main__':
    print(prime_sieve(20))