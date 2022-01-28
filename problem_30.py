# upper limit is: 6 * 9^5 = 354,294

def get_limit(target):
    power9 = 9**target
    count = 1
    x = power9
    while count < len(str(x)):
        x += power9
        count += 1
    
    return x

def solve(target):
    limit = get_limit(target)
    powers = [x**target for x in range(10)]
    answer = 0
    for num in range(10, limit+1):
        total = 0
        x = num
        while total < num and x > 0:
            total += powers[x % 10]
            x = x // 10
        
        if total == num and x == 0:
            answer += total

    print(answer)

if __name__ == '__main__':
    solve(4)
    solve(5)