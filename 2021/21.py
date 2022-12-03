import copy
from collections import defaultdict

# pos1 = 6
# pos2 = 8
# score1 = 0
# score2 = 0
# dice = 1
# rolls = 0
#
# while score1 < 1000 and score2 < 1000:
#     for i in range(3):
#         pos1 = (pos1 + dice) % 10
#         dice += 1
#         if dice == 101:
#             dice = 1
#         rolls += 1
#     score1 += pos1
#     print(rolls, score1, score2, rolls * score2)
#     for i in range(3):
#         pos2 = (pos2 + dice) % 10
#         dice += 1
#         if dice == 101:
#             dice = 1
#         rolls += 1
#     score2 += pos2
#     print(rolls, score1, score2, rolls * score2)

turn1 = True
summ1 = 0
summ2 = 0

player1 = []
player2 = []
for i in range(21):
    player1.append([])
    player2.append([])
    for j in range(11):
        player1[-1].append(0)
        player2[-1].append(0)
player1[0][6] = 1
player2[0][8] = 1


def zerodesu():
    return 0


states = defaultdict(zerodesu)
states[0, 0, 6, 8] = 1
wholeturn = 0


def turn():
    global states
    global player1
    global player2
    global turn1
    global summ1
    global summ2
    global wholeturn
    over = True
    nplayer = [[0] * 11 for kaki in range(31)]
    newstates = defaultdict(zerodesu)
    if turn1:
        for [scr1, scr2, pos1, pos2] in states.keys():
            newstates[scr1 + (pos1 + 3 - 1) % 10 + 1, scr2, (pos1 + 3 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2]
            newstates[scr1 + (pos1 + 4 - 1) % 10 + 1, scr2, (pos1 + 4 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2] * 3
            newstates[scr1 + (pos1 + 5 - 1) % 10 + 1, scr2, (pos1 + 5 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2] * 6
            newstates[scr1 + (pos1 + 6 - 1) % 10 + 1, scr2, (pos1 + 6 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2] * 7
            newstates[scr1 + (pos1 + 7 - 1) % 10 + 1, scr2, (pos1 + 7 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2] * 6
            newstates[scr1 + (pos1 + 8 - 1) % 10 + 1, scr2, (pos1 + 8 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2] * 3
            newstates[scr1 + (pos1 + 9 - 1) % 10 + 1, scr2, (pos1 + 9 - 1) % 10 + 1, pos2] += states[
                scr1, scr2, pos1, pos2]
        states = copy.deepcopy(newstates)
        for [scr1, scr2, pos1, pos2] in newstates.keys():
            if scr1 > 20:
                summ1 += newstates[scr1, scr2, pos1, pos2]
                states[scr1, scr2, pos1, pos2] = 0
    else:
        for [scr1, scr2, pos1, pos2] in states.keys():
            newstates[scr1, scr2 + (pos2 + 3 - 1) % 10 + 1, pos1, (pos2 + 3 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2]
            newstates[scr1, scr2 + (pos2 + 4 - 1) % 10 + 1, pos1, (pos2 + 4 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2] * 3
            newstates[scr1, scr2 + (pos2 + 5 - 1) % 10 + 1, pos1, (pos2 + 5 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2] * 6
            newstates[scr1, scr2 + (pos2 + 6 - 1) % 10 + 1, pos1, (pos2 + 6 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2] * 7
            newstates[scr1, scr2 + (pos2 + 7 - 1) % 10 + 1, pos1, (pos2 + 7 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2] * 6
            newstates[scr1, scr2 + (pos2 + 8 - 1) % 10 + 1, pos1, (pos2 + 8 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2] * 3
            newstates[scr1, scr2 + (pos2 + 9 - 1) % 10 + 1, pos1, (pos2 + 9 - 1) % 10 + 1] += states[
                scr1, scr2, pos1, pos2]
        states = copy.deepcopy(newstates)
        for [scr1, scr2, pos1, pos2] in newstates.keys():
            if scr2 > 20:
                summ2 += newstates[scr1, scr2, pos1, pos2]
                states[scr1, scr2, pos1, pos2] = 0
    turn1 = not turn1
    if turn1:
        wholeturn += 1


while True:
    print(summ1, summ2)
    # if turn1:
    #     print(wholeturn, player1)
    # else:
    #     print(wholeturn, player2)
    turn()
print(max(summ1, summ2))


