inputfile = open("04.txt", "r")
input = inputfile.read()
inputfile.close()

from copy import deepcopy

# input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

input = input.splitlines()
input.insert(0, "."*len(input[1]))
input.append("."*len(input[0]))
for i in range(len(input)):
    input[i] = "." + input[i] + "."
print(input)

newstate = deepcopy(input)
available = 0
while(True):
    newavailable = 0
    for i in range(1, len(input)-1):
        for j in range(1, len(input[0])-1):
            if input [i][j] == '@':
                surrounding = -1
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if input[i+k][j+l] == '@':
                            surrounding += 1
                if surrounding < 4:
                    newavailable += 1
                    newstate[i] = newstate[i][:j] + '.' + newstate[i][j+1:]
                    print(i-1, j-1, surrounding)
    available += newavailable
    if newavailable == 0:
        break
    input = deepcopy(newstate)

print (available)

        # surrounding = 0
        # directions = ""
        # if input[i][j] == '@':
        #     if i > 0:
        #         if j > 0:
        #             if input [i-1][j-1] == '@':
        #                 surrounding += 1
        #         if j < len(input[0])-1:
        #             if input [i-1][j+1] == '@':
        #                 surrounding += 1
        #         if input [i-1][j] == '@':
        #             surrounding += 1
        #     if i < len(input)-1:
        #         if j > 0:
        #             if input [i+1][j-1] == '@':
        #                 surrounding += 1
        #                 directions += "left-down, "
        #         if j < len(input[0])-1:
        #             if input [i+1][j+1] == '@':
        #                 surrounding += 1
        #                 directions += "right-down, "
        #         if input [i+1][j] == '@':
        #             surrounding += 1
        #             directions += "down, "
        #     if j > 0:
        #         if input[i][j-1] == '@':
        #             surrounding += 1
        #             directions += "left, "
        #     if j < len(input[0])-1:
        #         if input[i][j+1] == '@':
        #             surrounding += 1
        #             directions += "right, "
            