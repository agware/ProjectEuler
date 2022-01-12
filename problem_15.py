class Lattice:
    def __init__(self, rows):
        self.rows = rows
        self.moves = {(rows, rows): 1}

    def get_moves_required(self, x, y):
        # this is because the symmetry of the problem lets us cheat/optimise a little
        # another possible option would be to use frozenset in place of the tuple
        if x < y:
            tmp = x
            x = y
            y = tmp
        
        if (x, y) in self.moves:
            return self.moves[(x, y)]
        
        count = 0
        if x < self.rows:
            count += self.get_moves_required(x+1, y)
        if y < self.rows:
            count += self.get_moves_required(x, y+1)
        
        self.moves[(x, y)] = count
        return count

if __name__ == '__main__':
    lattice = Lattice(20)
    print(lattice.get_moves_required(0,0))