fib_1 = 1
fib_2 = 1
count = 2

while fib_2 < 10 ** 999:
    tmp = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = tmp

    count += 1

print(count)
