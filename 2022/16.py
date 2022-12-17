input = """Valve OQ has flow rate=17; tunnels lead to valves NB, AK, KL
Valve HP has flow rate=0; tunnels lead to valves ZX, KQ
Valve GO has flow rate=0; tunnels lead to valves HR, GW
Valve PD has flow rate=9; tunnels lead to valves XN, EV, QE, MW
Valve NQ has flow rate=0; tunnels lead to valves HX, ZX
Valve DW has flow rate=0; tunnels lead to valves IR, WE
Valve TN has flow rate=24; tunnels lead to valves KL, EI
Valve JJ has flow rate=0; tunnels lead to valves EV, HR
Valve KH has flow rate=0; tunnels lead to valves ZQ, AA
Valve PH has flow rate=0; tunnels lead to valves FN, QE
Valve FD has flow rate=0; tunnels lead to valves SM, HX
Valve SM has flow rate=7; tunnels lead to valves WW, RZ, FD, HO, KQ
Valve PU has flow rate=0; tunnels lead to valves VL, IR
Valve OM has flow rate=0; tunnels lead to valves CM, AA
Valve KX has flow rate=20; tunnel leads to valve PC
Valve IR has flow rate=3; tunnels lead to valves PU, CM, WW, DW, AF
Valve XG has flow rate=0; tunnels lead to valves RX, OF
Valve QE has flow rate=0; tunnels lead to valves PH, PD
Valve GW has flow rate=0; tunnels lead to valves JQ, GO
Valve HO has flow rate=0; tunnels lead to valves SM, TY
Valve WU has flow rate=0; tunnels lead to valves SG, RZ
Valve MS has flow rate=0; tunnels lead to valves UE, OF
Valve JS has flow rate=0; tunnels lead to valves DO, ZX
Valve YQ has flow rate=0; tunnels lead to valves BC, SG
Valve EJ has flow rate=0; tunnels lead to valves AA, LR
Valve EI has flow rate=0; tunnels lead to valves BV, TN
Valve NC has flow rate=0; tunnels lead to valves TS, BC
Valve AF has flow rate=0; tunnels lead to valves IR, HX
Valve OX has flow rate=0; tunnels lead to valves HR, BV
Valve BF has flow rate=0; tunnels lead to valves JQ, SY
Valve CA has flow rate=0; tunnels lead to valves YD, HX
Valve KQ has flow rate=0; tunnels lead to valves HP, SM
Valve NB has flow rate=0; tunnels lead to valves OQ, OF
Valve SY has flow rate=0; tunnels lead to valves BF, BV
Valve AA has flow rate=0; tunnels lead to valves KH, EJ, OM, TY, DO
Valve BC has flow rate=11; tunnels lead to valves WE, RX, YQ, LR, NC
Valve HR has flow rate=14; tunnels lead to valves OX, GO, JJ
Valve WE has flow rate=0; tunnels lead to valves DW, BC
Valve MW has flow rate=0; tunnels lead to valves JQ, PD
Valve DO has flow rate=0; tunnels lead to valves JS, AA
Valve PC has flow rate=0; tunnels lead to valves AK, KX
Valve YD has flow rate=0; tunnels lead to valves CA, OF
Valve RX has flow rate=0; tunnels lead to valves XG, BC
Valve CM has flow rate=0; tunnels lead to valves IR, OM
Valve HX has flow rate=6; tunnels lead to valves ZQ, NQ, AF, FD, CA
Valve ZQ has flow rate=0; tunnels lead to valves KH, HX
Valve BV has flow rate=21; tunnels lead to valves SY, OX, EI
Valve AK has flow rate=0; tunnels lead to valves PC, OQ
Valve UE has flow rate=0; tunnels lead to valves MS, JQ
Valve LR has flow rate=0; tunnels lead to valves BC, EJ
Valve JQ has flow rate=8; tunnels lead to valves MW, UE, BF, GW
Valve VL has flow rate=0; tunnels lead to valves PU, ZX
Valve EV has flow rate=0; tunnels lead to valves JJ, PD
Valve TS has flow rate=0; tunnels lead to valves NC, ZX
Valve RZ has flow rate=0; tunnels lead to valves SM, WU
Valve OF has flow rate=13; tunnels lead to valves XG, YD, NB, MS, XN
Valve WW has flow rate=0; tunnels lead to valves SM, IR
Valve TY has flow rate=0; tunnels lead to valves HO, AA
Valve XN has flow rate=0; tunnels lead to valves OF, PD
Valve SG has flow rate=15; tunnels lead to valves WU, YQ
Valve FN has flow rate=25; tunnel leads to valve PH
Valve KL has flow rate=0; tunnels lead to valves TN, OQ
Valve ZX has flow rate=5; tunnels lead to valves JS, HP, VL, NQ, TS""".splitlines()

# input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

from queue import Queue
from math import inf
from copy import copy
import numpy as np

rates = []
tunnels = []
names = []
for line in input:
    line = line.split('Valve ')[1]
    name = line[0:2]
    rate = line.split('rate=')[1]
    names.append(name)
    rates.append(int(rate.split(';')[0]))
    tunnel = rate.split('valve')[1]
    if tunnel[0] == 's':
        tunnel = tunnel[2:]
    else:
        tunnel = tunnel[1:]
    tunnels.append(tunnel.split(', '))

name_to_index = {v: k for k, v in enumerate(names)}
for tunnel in tunnels:
    for i in range(len(tunnel)):
        tunnel[i] = name_to_index[tunnel[i]]

# print(rates)
# print(tunnels)

# graph = []
# for i in range(len(input)):
#     graph.append([])
#     for j in range(len(input)):
#         if j in tunnels[i]:
#             graph[i].append(1)
#         else:
#             graph[i].append(0)
# print(graph)

# for i in range(len(graph)):
#     for j in range(len(graph)):
#         if graph[i][j] 

def leastDistance(graph, source):
    Q = Queue()
    # create a dictionary with large distance(infinity) of each vertex from source
    distance = [inf for k in range(len(tunnels))]
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({source})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited_vertices:
                # update the distance
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                    Q.put(u)
        visited_vertices.update({u})
        # print(distance)
        # print(Q.queue)
    return distance

# def adjMatrix(adjList, nodes):
#     n = len(adjList)
#     adjMatrix = np.nan * np.ones((n, n))
#     np.fill_diagonal(adjMatrix, 0)
#     for i in range(n):
#         for j in adjList[i]:
#             adjMatrix[i, j] = 1
#     for node in nodes:
#         weights = {endnode:}

graph = []
for i in range(len(tunnels)):
    graph.append(leastDistance(tunnels, i))
# print(graph)

for i in range(len(rates)-1, -1, -1):
    if rates[i] == 0 and names[i] != 'AA':
        # print("rate is zero")
        graph.pop(i)
        for line in graph:
            line.pop(i)
        rates.pop(i)
        names.pop(i)

# print(names)
# print(rates)
# print(graph)

def move(place, visited, time, pressure):
    global largest
    pressure = pressure + rates[place] * time
    moved = False
    for node, distance in enumerate(graph[place]):
        if distance > 0 and distance < time and node not in visited:
            newVisited = copy(visited)
            newVisited.append(node)
            move(node, newVisited, time-distance-1, pressure)
            moved = True
    if not moved:
        if pressure > largest:
            largest = pressure

def doublemove(me, elephant, visited, time, pressure, opened):
    global largest
    # print(me, elephant, visited, time, pressure)
    newVisited = copy(visited)
    newVisited.append(me['goal'])
    newVisited.append(elephant['goal'])
    newVisited = list(set(newVisited))
    newelephant = copy(elephant)
    newelephant['time'] -= 1
    newme = copy(me)
    newme['time'] -= 1
    if time == 0:
        if pressure > largest:
            largest = pressure
            print(names)
            print(opened)
            checkSum = 0
            for i, left in enumerate(opened):
                checkSum += (26-left) * rates[i]
            print(checkSum, pressure)
        return
    moved = False
    if me['time'] == 0:
        opened[me['goal']] = 26 - time
        if elephant['time'] == 0:
            opened[elephant['goal']] = 26 - time
            pressure += (rates[me['goal']] + rates[elephant['goal']]) * time
            newVisited.append(me['goal'])
            newVisited.append(elephant['goal'])
            for node0, distance0 in enumerate(graph[me['goal']]):
                for node1, distance1 in enumerate(graph[elephant['goal']]):
                    if distance0 > 0 and distance1 > 0 and node0 not in newVisited and node1 not in newVisited and node0 != node1:
                        newme['goal'] = node0
                        newme['time'] = distance0
                        newelephant['goal'] = node1
                        newelephant['time'] = distance1
                        doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
                        # if node0 == 6 or node1 == 6:
                        #     print(newme, newelephant, time)
                        moved = True
            # if not moved:
            #     doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
        else:
            pressure += rates[me['goal']] * time
            # newVisited.append(me['goal'])
            for node, distance in enumerate(graph[me['goal']]):
                if distance > 0 and node not in newVisited:
                    newme['goal'] = node
                    newme['time'] = distance
                    doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
                    moved = True
            # if not moved:
            #     doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
    elif elephant['time'] == 0:
        pressure += rates[elephant['goal']] * time
        opened[elephant['goal']] = 26 - time
        # newVisited.append(elephant['goal'])
        for node, distance in enumerate(graph[elephant['goal']]):
            if distance > 0 and node not in newVisited:
                newelephant['goal'] = node
                newelephant['time'] = distance
                doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
                moved = True
    else:
        doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
        moved = True
    if not moved:
        doublemove(newme, newelephant, newVisited, time-1, pressure, opened)
        # if pressure > largest:
        #     largest = pressure
        #     print(names)
        #     print(opened)
        # return
    # if opened[6] == 3:
        # print(opened)

largest = 0
start = names.index("AA")
move(start, [], 30, 0)
print(largest)

largest = 0
startMe = {'goal': start, 'time': 0}
startElephant = {'goal': start, 'time': 0}
open = []
for i in range(len(rates)):
    open.append(inf)
doublemove(startMe, startElephant, [], 26, 0, open)
print(largest)
print(graph)