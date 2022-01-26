import re

def prepare_data():

    text = ''
    with open('data/p022_names.txt') as f:
        lines = f.readlines()
        for line in lines:
            text += line

    text = re.sub('"', '', text)
    names = text.split(',')

    return names

def get_character_score(char):
    return ord(char) - ord('A') + 1


def get_name_score(name):
    total = 0
    for x in name:
        total += get_character_score(x)
    
    return total

def solve_problem(names):
    names.sort()

    total = 0
    for i in range(len(names)):
        total += (i+1)*get_name_score(names[i])

    return total

if __name__ == '__main__':
    data = prepare_data()
    print(solve_problem(data))