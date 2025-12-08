inputfile = open("07.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

input = input.splitlines()

for i, line in enumerate(input):
    input[i] = ".." + line + ".."

############ A

# input[0] = input[0].replace("S", "|")

# splits = 0
# # for i, line in enumerate(input[:-1]):
# i = 0
# while i < len(input) -1 :
#     for j, char in enumerate(input[i]):
#         if char == "|":
#             if input[i+1][j] == ".":
#                 input[i+1] = input[i+1][:j] + "|" + input[i+1][j+1:]
#                 # print("here", input[i+1])
#             if input[i+1][j] == "^":
#                 input[i+1] = input[i+1][:j-1]+"|"+input[i+1][j:]
#                 input[i+1] = input[i+1][:j+1]+"|"+input[i+1][j+2:]
#                 splits += 1
#     print(input[i])
#     i += 1
# print(splits)

########### B

for i, line in enumerate(input):
    input[i] = list(input[i])

for i, char in enumerate(input[0]):
    if char == "S":
        input[0][i] = 1

# splits = 0
# for i, line in enumerate(input[:-1]):
i = 0
while i < len(input)-1:
    for j, char in enumerate(input[i]):
        if type(char) == int:
            if type(input[i+1][j]) == int:
                input[i+1][j] += input[i][j]
            if input[i+1][j] == ".":
                input[i+1][j] = input[i][j]
                # print("here", input[i+1])
            if input[i+1][j] == "^":
                if type(input[i+1][j-1]) == int:
                    input[i+1][j-1] += input[i][j]
                else:
                    input[i+1][j-1] = input[i][j]
                if type(input[i+1][j+1]) == int:
                    input[i+1][j+1] += input[i][j]
                else:
                    input[i+1][j+1] = input[i][j]
                # splits += 1
    print(input[i+1])
    i += 1
summ = 0
for stuff in input[-1]:
    if type(stuff) == int:
        summ += stuff
    
print(summ)





                    