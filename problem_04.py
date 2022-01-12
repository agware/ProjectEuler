import queue

class Node:
    def __init__(self, val_1, val_2, height=0):
        self.max_val = max(val_1, val_2)
        self.min_val = min(val_1, val_2)
        self.height = height
    
    def to_string(self):
        return f'{self.max_val} * {self.min_val} = {self.max_val*self.min_val}'

def is_palindrome(val):
    val = str(val)
    
    for i in range(len(val)//2):
        if val[i] != val[len(val)-i-1]:
            return False
    
    return True


target = 999

my_queue = queue.Queue()
my_queue.put(Node(target, target))

height_prev = -1

while True:
    node = my_queue.get()

    if is_palindrome(node.max_val*node.min_val):
        print(node.to_string())
        break

    if height_prev < node.height and node.max_val != node.min_val:
        my_queue.put(Node(node.max_val-1, node.min_val, node.height+1))
    
    my_queue.put(Node(node.max_val, node.min_val-1, node.height+1))
    height_prev = node.height
