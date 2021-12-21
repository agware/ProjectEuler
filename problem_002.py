limit = 4000000

fib_1 = 1
fib_2 = 2

total = 0
while fib_2 < 4000000:
    if fib_2 % 2 == 0:
        total += fib_2

    tmp_val = fib_2
    fib_2 += fib_1
    fib_1 = tmp_val

print(total) 