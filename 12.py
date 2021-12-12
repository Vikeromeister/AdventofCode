input = """GC-zi
end-zv
lk-ca
lk-zi
GC-ky
zi-ca
end-FU
iv-FU
lk-iv
lk-FU
GC-end
ca-zv
lk-GC
GC-zv
start-iv
zv-QQ
ca-GC
ca-FU
iv-ca
start-lk
zv-FU
start-zi
""".splitlines()

edges = []
for line in input:
    edges.append(line.split("-"))
# print(edges)

def move(cave, visited):
    # print(cave)
    visits = visited[:]
    global routecounter
    if cave in visited and cave[0].islower():  # invalid
        # print( "current cave", cave, "already visited, route:", visited)
        return None
    visits.append(cave)
    if cave == "end":  # end
        routecounter += 1
        # print("end cave reached, route nr", routecounter, visits)
        return None
    for edge in edges:
        if edge[0] == cave:
            move(edge[1], visits)
        if edge[1] == cave:
            move(edge[0], visits)
    return None


def moveb(cave, visited):
    visits = visited[:]
    global routecounter
    if cave == "start" and visited != []:
        return None
    if visited.count(cave) == 2:  # invalid
        # print("current cave", cave, "already visited twice, route:", visited)
        return None
    # print(len(visited), len(set(visited)))
    if cave in visited and len(visited) != len(set(visited)):
        return None
    if cave[0].islower():
        visits.append(cave)
    if cave == "end":  # end
        routecounter += 1
        # print("end cave reached, route nr", routecounter, visits)
        return None
    for edge in edges:
        if edge[0] == cave:
            moveb(edge[1], visits)
        if edge[1] == cave:
            moveb(edge[0], visits)
    return None


routecounter = 0
move("start", [])
print(routecounter)

routecounter = 0
moveb("start", [])
print(routecounter)
