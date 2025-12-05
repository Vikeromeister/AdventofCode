inputfile = open("05.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

input = input.splitlines()

for ind, line in enumerate(input):
    if line == '':
        ranges = input[:ind]
        items = input[ind+1:]
        break

freshies = 0
for itemstr in items:
    item = int(itemstr)
    # fresh = False
    for range in ranges:
        bottom, top = range.split('-')
        if item >= int(bottom) and item <= int(top):
            # fresh = True
            freshies += 1
            break
print(freshies)

#############
##### B #####
#############

for ind, range in enumerate(ranges):
    ranges[ind] = [int(range.split("-")[0]), int(range.split("-")[1])]

while (True):
    merged = False
    for inda, rangeA in enumerate(ranges):
        for indb, rangeB in enumerate(ranges[inda+1:]):
            if rangeB[0] <= rangeA[1] and rangeA[0] <= rangeB[1]:
                ranges[inda][0] = min(rangeA[0], rangeB[0])
                ranges[inda][1] = max(rangeA[1], rangeB[1])
                ranges.pop(inda+1+indb)
                merged = True
                print ("")
                print(inda, indb, ranges)
                break
        if merged:
            break
    if not merged:
        break

freshcounter = 0
for range in ranges:
    freshcounter += range[1]-range[0]+1

print(freshcounter)