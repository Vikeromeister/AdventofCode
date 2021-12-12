input = """4836484555
4663841772
3512484556
1481547572
7741183422
8683222882
4215244233
1544712171
5725855786
1717382281""".splitlines()

octos = []

for [i, line] in enumerate(input):
    octos.append([])
    for char in line:
        octos[i].append(int(char))


def flash(i, j):
    global octos
    global flashed
    if flashed[i][j]:
        return None
    flashed[i][j] = True

    if i > 0:  # i-1
        if j > 0:  # i-1 j-1
            octos[i-1][j-1] += 1
            if octos[i-1][j-1] > 9:
                flash(i-1, j-1)

        octos[i-1][j] += 1 # i-1 j
        if octos[i - 1][j] > 9:
            flash(i - 1, j)

        if j < len(octos[i])-1:
            octos[i-1][j+1] += 1
            if octos[i-1][j+1] > 9:
                flash(i-1, j+1)
    # i
    if j > 0:
        octos[i][j - 1] += 1
        if octos[i][j - 1] > 9:
            flash(i, j - 1)

    if j < len(octos[i])-1:
        octos[i][j + 1] += 1
        if octos[i][j + 1] > 9:
            flash(i, j + 1)
    # i+1
    if i < len(octos) - 1:
        if j > 0:
            octos[i+1][j - 1] += 1
            if octos[i+1][j - 1] > 9:
                flash(i+1, j - 1)

        octos[i + 1][j] += 1
        if octos[i + 1][j] > 9:
            flash(i + 1, j)

        if j < len(octos[i]) - 1:
            octos[i+1][j + 1] += 1
            if octos[i+1][j + 1] > 9:
                flash(i+1, j + 1)
    return None

flashcounter = 0
step = 0
while True:
    sync = True
    step += 1
    flashed = [[False for i in range(len(input))] for j in range(len(input[0]))]
    for [i, line] in enumerate(octos):
        for [j, num] in enumerate(line):
            octos[i][j] += 1
    for [i, line] in enumerate(octos):
        for [j, num] in enumerate(line):
            if octos[i][j] > 9:
                flash(i, j)
    for [i, line] in enumerate(octos):
        for [j, num] in enumerate(line):
            if flashed[i][j]:
                # print(i, j, "flashed with value", octos[i][j])
                octos[i][j] = 0
                flashcounter += 1
    if step == 100:
        print(flashcounter)
    for line in flashed:
        for oreg in line:
            if not oreg:
                sync = False
    if sync:
        print("step", step, "they all flashed in sync")
        break

