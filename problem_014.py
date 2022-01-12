class Collatz:
    chain_length = {1: 1}
    longest_root = 1
    longest_length = 1

    def get_length(self, num):
        if num <= 0:
            return 0

        if num not in self.chain_length:
            self._add_number(num)
        
        return self.chain_length[num]


    def get_longest_root(self):
        return self.longest_root

    
    def get_longest_length(self):
        return self.longest_length


    def _add_number(self, num):
        if num <= 0 or num in self.chain_length:
            return None
        
        next_num = self.calc_collatz(num)
        self._add_number(next_num)
        
        self.chain_length[num] = self.chain_length[next_num] + 1
        
        self._update_longest(num)
    

    def _update_longest(self, num):
        if num not in self.chain_length:
            return None

        if self.chain_length[num] > self.longest_length:
            self.longest_length = self.chain_length[num]
            self.longest_root = num


    @staticmethod
    def calc_collatz(num):
        if num % 2 == 0:
            return num // 2
        
        return 3*num + 1
    

if __name__ == '__main__':
    limit = 1000000
    collatz = Collatz()

    for i in range(1,limit):
        _ = collatz.get_length(i)
    
    print(collatz.get_longest_root())
    print(collatz.get_longest_length())
