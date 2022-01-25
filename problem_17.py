class CountChars:

    under_20 = {
        1: 3,       # one
        2: 3,       # two
        3: 5,       # three
        4: 4,       # four
        5: 4,       # five
        6: 3,       # six
        7: 5,       # seven
        8: 5,       # eight
        9: 4,       # nine
        10: 3,      # ten
        11: 6,      # eleven
        12: 6,      # twelve
        13: 8,      # thirteen
        14: 8,      # fourteen
        15: 7,      # fifteen
        16: 7,      # sixteen
        17: 9,      # seventeen
        18: 8,      # eighteen
        19: 8,      # nineteen
    }

    tens = {
        2: 6,       # twenty
        3: 6,       # thirty
        4: 5,       # forty
        5: 5,       # fifty
        6: 5,       # sixty
        7: 7,       # seventy
        8: 6,       # eighty
        9: 6,       # ninety
    }

    @classmethod
    def count(cls, num):
        if num == 1000:
            return len('onethousand')
        
        if num % 100 == 0:
            return cls.under_20[num//100] + len('hundred')
        
        total = 0
        if num > 100:
            total += cls.under_20[num//100]
            total += len('hundredand')
            num %= 100
        
        if num >= 20:
            total += cls.tens[num//10]
            num %= 10

        if num == 0:
            return total
        
        return total + cls.under_20[num]

target = 1000

total = 0
for i in range(target):
    total += CountChars.count(i+1)

print(total)