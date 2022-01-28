import math

def get_lexicographic_permutation(n, target):
    # this is required for indexing from 1 not 0
    target -= 1

    digits = list(range(n))
    out = ''
    for _ in range(n):
        num_perms = math.factorial(len(digits)-1)
        index = target // num_perms
        target %= num_perms
        x = digits.pop(index)
        out += str(x)
    
    return out


if __name__ == '__main__':
    print(get_lexicographic_permutation(3, 1))
    print(get_lexicographic_permutation(3, 5))
    print(get_lexicographic_permutation(10, 1000000))