target = 1000
val = 2 ** target
total = 0
while val > 0:
    total += val % 10
    val = val // 10

print(total)