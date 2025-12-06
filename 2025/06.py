inputfile = open("06.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

input = input.splitlines()

from math import prod

numbers = []
for ind, line in enumerate(input[:-1]):
    numbers.append([])
    for numstr in line.split():
        numbers[-1].append(int(numstr))
numbers = list(map(list, zip(*numbers)))

# print(numbers)

grand_total = 0
for index, operator in enumerate(input[-1].split()):
    if operator == "+":
        result = sum(numbers[index])
    elif operator == "*":
        result = prod(numbers[index])
    else:
        print("wtf", operator)
    grand_total += result

# print(grand_total)

########### B

numbers = []
for ind, line in enumerate(input[:-1]):
    numbers.append([])
    for character in line:
        numbers[-1].append(character)
numbers = list(map(list, zip(*numbers)))
# print(numbers)

for i, num in enumerate(numbers):
    numeral = ""
    for digit in num:
        numeral += digit
    try:
        numeral = int(numeral.split()[0])
    except:
        numeral = -1
    numbers[i] = numeral
numbers.append(-1)
# print(numbers)

grand_total = 0
for index, operator in enumerate(input[-1]):
    j = 0
    if operator == "+":
        result = 0
        while numbers[index+j] != -1:
            result += numbers[index+j]
            j += 1
        grand_total += result
    elif operator == "*":
        result = 1
        while numbers[index+j] != -1:
            result *= numbers[index+j]
            j += 1
        grand_total += result
    # print(operator, result)
print(grand_total)