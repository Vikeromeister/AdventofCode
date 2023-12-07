input = """Time:        46     85     75     82
Distance:   208   1412   1257   1410""".splitlines()

# input = """Time:      7  15   30
# Distance:  9  40  200""".splitlines()

input[0] = input[0].split(':')[1]
input[1] = input[1].split(':')[1]

times = []
distances = []
for stuff in input[0].split():
    if stuff != '':
        times.append(int(stuff))
for stuff in input[1].split():
    if stuff != '':
        distances.append(int(stuff))

total = 1
for i, time in enumerate(times):
    for held in range(time):
        if (time - held) * held > distances[i]:
            minheld = held
            break
    options = time + 1 - minheld * 2
    total = total * options
print(total)

input = """Time:        46857582
Distance:   208141212571410""".splitlines()

# input = """Time:      7  15   30
# Distance:  9  40  200""".splitlines()

input[0] = input[0].split(':')[1]
input[1] = input[1].split(':')[1]

times = []
distances = []
for stuff in input[0].split():
    if stuff != '':
        times.append(int(stuff))
for stuff in input[1].split():
    if stuff != '':
        distances.append(int(stuff))

total = 1
for i, time in enumerate(times):
    for held in range(time):
        if (time - held) * held > distances[i]:
            minheld = held
            break
    options = time + 1 - minheld * 2
    total = total * options
print(total)