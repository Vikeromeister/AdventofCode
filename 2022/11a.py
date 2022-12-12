input = """Monkey 0:
  Starting items: 65, 58, 93, 57, 66
  Operation: new = old * 7
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 1:
  Starting items: 76, 97, 58, 72, 57, 92, 82
  Operation: new = old + 4
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 2:
  Starting items: 90, 89, 96
  Operation: new = old * 5
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 1

Monkey 3:
  Starting items: 72, 63, 72, 99
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 4:
  Starting items: 65
  Operation: new = old + 1
  Test: divisible by 2
    If true: throw to monkey 6
    If false: throw to monkey 2

Monkey 5:
  Starting items: 97, 71
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 6:
  Starting items: 83, 68, 88, 55, 87, 67
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 7:
  Starting items: 64, 81, 50, 96, 82, 53, 62, 92
  Operation: new = old + 5
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 0""".split('\n\n')


input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n\n")

class Monkey:
    def __init__(self, raw):
        lines = raw.splitlines()

        items = []
        for item in lines[1].split(', '):
            items.append(item)
        # print(items)
        items[0] = items[0].split(' ')[4]
        self.items = []
        for item in items:
            self.items.append(int(item))
        
        self.operand = lines[2].split(' ')[7]
        self.operator = lines[2].split(' ')[6]

        self.test = int(lines[3].split(' ')[5])
        self.true = int(lines[4].split(' ')[9])
        self.false = int(lines[5].split(' ')[9])

        self.counter = 0
    
    def __str__(self):
        output = f"""Items: {self.items}
Operation: new = old {self.operator} {self.operand}
Test: divisible by {self.test}
If True throw to monkey {self.true}
If false throw to monkey {self.false}"""
        return output
    
    def monkey_do(self):
        global monkeys
        # for id, item in enumerate(self.items):
        while len(self.items) > 0:
            item = self.items[0]
            if self.operator == '+':
                if self.operand == 'old':
                    new = item + item
                else:
                    new = item + int(self.operand)
            else:
                if self.operand == 'old':
                    new = item * item
                else:
                    new = item * int(self.operand)
            self.items[0] = int(new/3)
            self.counter += 1
            # print(monkeys)
            # print(self.false)
            if self.items[0] % self.test == 0:
                monkeys[self.true].items.append(self.items.pop(0))
            else:
                monkeys[self.false].items.append(self.items.pop(0))

monkeys = []
for monkey_raw in input:
    monkeys.append(Monkey(monkey_raw))
# print(monkeys)
for i in range(20):
    for monkey in monkeys:
        # print(monkey)
        monkey.monkey_do()
    print(f'round {i}')
    for j, monkey in enumerate(monkeys):
        print(j, monkey.items)

print(' ')

for monkey in monkeys:
    print(monkey.counter)