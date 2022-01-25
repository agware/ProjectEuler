target = 100
val = 1
for i in range(target, 0, -1):
    val *= i

total = 0
while val > 0:
    total += val % 10
    val = val // 10

print(total)