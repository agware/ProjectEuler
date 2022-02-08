def is_palindrome(val):

    if isinstance(val, int):
        val = str(val)
    
    if len(val) < 2:
        return True
    
    if val[0] != val[-1]:
        return False
    
    return is_palindrome(val[1:-1])

def reverse_num(num):
    val = list(str(num))
    val.reverse()
    return int(''.join(val))


class Lychrel:
    
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.hist = {}
    
    def is_lychrel(self, num):
        return self._test_lychrel(num, 0)

    def _test_lychrel(self, num, steps):
        if 0 < steps <= self.max_steps and is_palindrome(num):
            return False
        
        if steps > self.max_steps:
            self.hist[num] = True     
        elif num in self.hist:
            pass
        else:
            num_2 = reverse_num(num)
            self.hist[num] = self._test_lychrel(num + num_2, steps+1)

            if len(str(num)) <= len(str(num_2)):
                self.hist[num_2] = self.hist[num]
        
        return self.hist[num]

if __name__ == '__main__':
    limit = 10000
    lychrel = Lychrel(50)

    count = 0
    for i in range(limit, 0, -1):
        if lychrel.is_lychrel(i):
            count += 1
    
    print(count)