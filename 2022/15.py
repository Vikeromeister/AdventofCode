input = """Sensor at x=2557568, y=3759110: closest beacon is at x=2594124, y=3746832
Sensor at x=2684200, y=1861612: closest beacon is at x=2816974, y=2000000
Sensor at x=1003362, y=1946094: closest beacon is at x=1972523, y=2563441
Sensor at x=2142655, y=1481541: closest beacon is at x=1932524, y=967542
Sensor at x=2796219, y=1955744: closest beacon is at x=2816974, y=2000000
Sensor at x=3890832, y=1818644: closest beacon is at x=3454717, y=2547103
Sensor at x=2828842, y=1921726: closest beacon is at x=2816974, y=2000000
Sensor at x=2065227, y=583957: closest beacon is at x=1932524, y=967542
Sensor at x=2725784, y=2088998: closest beacon is at x=2816974, y=2000000
Sensor at x=3574347, y=927734: closest beacon is at x=1932524, y=967542
Sensor at x=2939312, y=2652370: closest beacon is at x=3454717, y=2547103
Sensor at x=2495187, y=3681541: closest beacon is at x=2431306, y=3703654
Sensor at x=2878002, y=2054681: closest beacon is at x=2816974, y=2000000
Sensor at x=1539310, y=3235516: closest beacon is at x=1972523, y=2563441
Sensor at x=545413, y=533006: closest beacon is at x=-538654, y=69689
Sensor at x=1828899, y=3980292: closest beacon is at x=2431306, y=3703654
Sensor at x=3275729, y=2937931: closest beacon is at x=3454717, y=2547103
Sensor at x=600131, y=3861189: closest beacon is at x=2431306, y=3703654
Sensor at x=2089895, y=28975: closest beacon is at x=1932524, y=967542
Sensor at x=2960402, y=3942666: closest beacon is at x=2594124, y=3746832
Sensor at x=3785083, y=3905392: closest beacon is at x=2594124, y=3746832
Sensor at x=1721938, y=1077173: closest beacon is at x=1932524, y=967542
Sensor at x=2515156, y=3751221: closest beacon is at x=2594124, y=3746832
Sensor at x=2469423, y=2109095: closest beacon is at x=2816974, y=2000000
Sensor at x=1776986, y=904092: closest beacon is at x=1932524, y=967542
Sensor at x=2789294, y=3316115: closest beacon is at x=2594124, y=3746832
Sensor at x=3538757, y=2695066: closest beacon is at x=3454717, y=2547103
Sensor at x=2299738, y=2708004: closest beacon is at x=1972523, y=2563441
Sensor at x=2388366, y=3234346: closest beacon is at x=2431306, y=3703654""".splitlines()
ROW = 2000000
MAX = 4000000


# input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()
# ROW = 10
# MAX = 20

from sympy import Interval, Union

def distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def check(point):
    if point[0] > MAX or point[0] < 0 or point[1] > MAX or point[1] < 0:
        return False
    for sensorId, sensor in enumerate(sensors):
        if distance(point, sensor) <= distances[sensorId]:
            return False
    return True

exclusionRange = Interval(0, 0)
sensors = []
distances = []
for line in input:
    stuff = line.split(', y=')
    sensor = (int(stuff[0].split('=')[1]), int(stuff[1].split(':')[0]))
    beacon = (int(stuff[1].split('=')[1]), int(stuff[2]))
    # print(sensor, beacon)
    dist = distance(sensor, beacon)
    sensors.append(sensor)
    distances.append(dist)
    radius = max(dist - abs(sensor[1] - ROW), 0)
    
    newRange = Interval(sensor[0] - radius, sensor[0] + radius)
    exclusionRange = Union(exclusionRange, newRange)

print(exclusionRange.measure)

for sensorId, sensor in enumerate(sensors):
    rad = distances[sensorId] + 1
    print(sensorId, rad)
    point = [sensor[0] - rad, sensor[1]]

    for i in range(rad):
        if check(point):
            print(point, 4000000*point[0] + point[1])
            exit()
        else:
            point[0] += 1
            point[1] += 1
    
    for i in range(rad):
        if check(point):
            print(point, 4000000*point[0] + point[1])
            exit()
        else:
            point[0] += 1
            point[1] -= 1
    
    for i in range(rad):
        if check(point):
            print(point, 4000000*point[0] + point[1])
            exit()
        else:
            point[0] -= 1
            point[1] -= 1
    
    for i in range(rad):
        if check(point):
            print(point, 4000000*point[0] + point[1])
            exit()
        else:
            point[0] -= 1
            point[1] += 1
    



    # for j in range(MAX):
    #     next = False
    #     for idSensor, sensor in enumerate(sensors):
    #         if distance((i, j), sensor) <= distances[idSensor]:
    #             next = True
    #             break
    #     if next == True:
    #         continue
    #     else:
    #         print(i, j, 4000000*i+j)
    #         exit()
