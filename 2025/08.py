inputfile = open("08.txt", "r")
input = inputfile.read()
inputfile.close()

# input = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

input = input.splitlines()

from math import dist

boxes = []
for line in input:
    boxes.append(list(map(int,line.split(","))))

# print(boxes)

########### A

# distances = []
# for i, box1 in enumerate(boxes):
#     distances.append([])
#     for j, box2 in enumerate(boxes):
#         if i >= j:
#             distances[-1].append(999999999)
#         else:
#             distances[-1].append(dist(boxes[i], boxes[j]))
# # print(len(distances), len(distances[0]))

# circuits = []
# for i in range(len(input)):
#     circuits.append(i+1)
# # print(len(circuits), circuits)

# for iterator in range(1000):
#     smallest = 99999999999999
#     for i, distancerow in enumerate(distances):
#         for j, distance in enumerate(distances[i]):
#             if distance < smallest:
#                 smallest = distance
#                 n = i
#                 m = j
#     # print("Pair:", n, m, "coordinates", boxes[n], boxes[m])
#     newcircuit = min(circuits[n], circuits[m])
#     oldcircuit = max(circuits[n], circuits[m])
#     for k, circuit in enumerate(circuits):
#         if circuit == oldcircuit:
#             circuits[k] = newcircuit
    
#     for i, circuit1 in enumerate(circuits):
#         for j, circuit2 in enumerate(circuits):
#             if circuit1 == circuit2:
#                 distances[n][m] = 99999999999
#                 distances[m][n] = 99999999999

# print(circuits)

# from statistics import mode

# product = 1
# for i in range(3):
#     culprit = mode(circuits)
#     product *= circuits.count(culprit)
#     while culprit in circuits:
#         circuits.remove(culprit)
#     print(circuits)

# print(product)

########## B

distances = []
for i, box1 in enumerate(boxes):
    distances.append([])
    for j, box2 in enumerate(boxes):
        if i >= j:
            distances[-1].append(9999999999)
        else:
            distances[-1].append(dist(boxes[i], boxes[j]))
# print(len(distances), len(distances[0]))

circuits = []
for i in range(len(input)):
    circuits.append(i+1)
# print(len(circuits), circuits)

while True:
    smallest = 888888888
    for i, distancerow in enumerate(distances):
        for j, distance in enumerate(distances[i]):
            if distance < smallest:
                smallest = distance
                n = i
                m = j
    # print("Pair:", n, m, "coordinates", boxes[n], boxes[m])
    if smallest == 888888888:
        break
    newcircuit = min(circuits[n], circuits[m])
    oldcircuit = max(circuits[n], circuits[m])
    for k, circuit in enumerate(circuits):
        if circuit == oldcircuit:
            circuits[k] = newcircuit
    
    for i, circuit1 in enumerate(circuits):
        for j, circuit2 in enumerate(circuits):
            if circuit1 == circuit2:
                distances[i][j] = 9999999999
                distances[j][i] = 9999999999

print(boxes[n][0]*boxes[m][0])