inputfile = open("03.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

input = input.splitlines()

total_joltage = 0
for bank in input:
    largest = 0
    largest_ind = 0
    for ind, battery in enumerate(bank[:-1]):
        if int(battery) > largest:
            largest_ind = ind
            largest = int(battery)
    second = 0
    for battery in bank[largest_ind+1:]:
        if int(battery) > second:
            second = int(battery)
    bank_joltage = int(str(largest) + str(second))
    total_joltage += bank_joltage
    print(bank_joltage, total_joltage)

###############
###### B ######
###############

def find_highest (todo, bank):
    largest = 0
    largest_ind = 0
    for ind, battery in enumerate(bank[:len(bank)-(todo-1)]):
        if int(battery) > largest:
            largest_ind = ind
            largest = int(battery)
    if todo == 1:
        returnable = str(largest)
    else:
        returnable = str(largest) + find_highest (todo-1, bank[largest_ind+1:])
    return returnable


total_joltage = 0
for line in input:
    bank_joltage = int(find_highest(12, line))
    total_joltage += bank_joltage
    print(bank_joltage, total_joltage)