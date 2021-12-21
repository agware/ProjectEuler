from utils import prime_sieve

target = 100

total = 0

for i in range(1, target):
    for j in range(i+1, target+1):
        total += i*j

print(2*total)