inputfile = open("02.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

input = input.split(',')

# summa=0
# for ID_range in input:
#     start, finish = ID_range.split("-")
#     start = int(start)
#     finish = int(finish)
#     for num in range(start, finish+1):
#         numstring = str(num)
#         if numstring[:len(numstring)//2] == numstring[len(numstring)//2:]:
#             summa+=num
#             # print (ID_range, num, "->", summa)
# print(summa)
# print ("")

def check(ID):
    invalid = False
    length = len(ID)
    if len(ID) > 1 and len(set(ID)) == 1:
        invalid = True
        # print (ID, 'all the same')
    if length == 4:
        if ID[0:2] == ID[2:4]:
            invalid = True
            # print (ID, "2x2:")
    if length == 6:
        if ID[:2] == ID[2:4] == ID[4:]:
            invalid = True
            # print (ID, "3x2")
        if ID[:3] == ID[3:]:
            invalid = True
            # print (ID, "2x3")
    if length == 8:
        if ID[:4] == ID[4:]:
            invalid = True
            print (ID, "2x4")
    if length == 9:
        if ID[:3] == ID[3:6] == ID[6:]:
            invalid = True
            print (ID, "3x3")
    if length == 10:
        if ID[:5] == ID[5:]:
            invalid = True
            print (ID, "2x5")
        if ID[:2] == ID[2:4] == ID[4:6] == ID[6:8] == ID[8:]:
            invalid = True
            print (ID, "5x2")
    return invalid


summb=0
longest = 0
for ID_range in input:
    start, finish = ID_range.split("-")
    start = int(start)
    finish = int(finish)
    for num in range(start, finish+1):
        numstring = str(num)
        if len(numstring) > longest:
            # longest = len(numstring)
            pass
        if check(numstring):
            summb+=num
            if len(numstring) > 7:
                print (ID_range, num, "->", summb)

print(longest)
print(summb)