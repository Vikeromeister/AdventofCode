inputfile = open("01.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """L68
# L30
# R48
# L5
# R160
# L155
# L1
# L99
# R14
# L82"""

input = input.splitlines()

counter = 50
pwa = 0
pwb = 0
for line in input:
    num = int(line[1:])
    if line[0] == "R":
        counter += num
        while counter > 99:
            counter -= 100
            pwb += 1
    elif line[0] == "L":
        if counter == 0:
            pwb += abs(num//100)
            counter -= num
            while counter < 0:
                counter += 100
        else:
            counter -= num
            while counter < 0:
                counter += 100
                pwb += 1
            if counter == 0:
                pwb += 1
    else:
        print("wtf", line)
    if counter == 0:
        pwa += 1
    print (line, "->", counter, pwb)
print(pwa)
print(pwb)