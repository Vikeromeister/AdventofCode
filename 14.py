from collections import defaultdict

poly = "NNSOFOCNHBVVNOBSBHCB"
testpoly = "NNCB"

testinput = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()

input = """HN -> S
FK -> N
CH -> P
VP -> P
VV -> C
PB -> H
CP -> F
KO -> P
KN -> V
NO -> K
NF -> N
CO -> P
HO -> H
VH -> V
OV -> C
VS -> F
PK -> H
OS -> S
BF -> S
SN -> P
NK -> N
SV -> O
KB -> O
ON -> O
FN -> H
FO -> N
KV -> S
CS -> C
VO -> O
SP -> O
VK -> H
KP -> S
SK -> N
NC -> B
PN -> N
HV -> O
HS -> C
CN -> N
OO -> V
FF -> B
VC -> V
HK -> K
CC -> H
BO -> H
SC -> O
HH -> C
BV -> P
OB -> O
FC -> H
PO -> C
FV -> C
BK -> F
HB -> B
NH -> P
KF -> N
BP -> H
KK -> O
OH -> K
CB -> H
CK -> C
OK -> H
NN -> F
VF -> N
SO -> K
OP -> F
NP -> B
FS -> S
SH -> O
FP -> O
SF -> V
HF -> N
KC -> K
SB -> V
FH -> N
SS -> C
BB -> C
NV -> K
OC -> S
CV -> N
HC -> P
BC -> N
OF -> K
BH -> N
NS -> K
BN -> F
PC -> C
CF -> N
HP -> F
BS -> O
PF -> S
PV -> B
KH -> K
VN -> V
NB -> N
PH -> V
KS -> B
PP -> V
PS -> C
VB -> N
FB -> N""".splitlines()

rules = []
for line in input:
    rules.append(line.split(" -> "))

newrules = {}
allpairs = []
legit = []
for rule in rules:
    legit.append(rule[1])
    legit.append(rule[0][0])
    legit.append(rule[0][1])
    # print(legit)
    allpairs.append(rule[0])
    newrules[rule[0]] = []
    for otherrule in rules:
        if rule[0][0] + rule[1] == otherrule[0]:
            newrules[rule[0]].append(otherrule[0])
        if rule[1] + rule[0][1] == otherrule[0]:
            newrules[rule[0]].append(otherrule[0])
# print(newrules)
pairs = defaultdict(list,{k:0 for k in allpairs})
legit = list(set(legit))

for i in range(len(poly)-1):
    # pairs.append(poly[i] + poly[i+1])
    pairs[poly[i] + poly[i+1]] += 1
# print(pairs)
print(pairs)


for i in range(40):
    newpairs = defaultdict(list, {k: 0 for k in allpairs})
    for pair in pairs.keys():
        for new in newrules[pair]:
            newpairs[new] += pairs[pair]
    pairs = newpairs
    print(pairs)

# print(pairs)

dict = defaultdict(list,{k:0 for k in legit})
# print(dict)
for pair in pairs.keys():
    dict[pair[0]] += pairs[pair]
    dict[pair[1]] += pairs[pair]
dict["N"] += 1
dict["B"] += 1
print(dict)


# for char in poly:
#     dict[char] += 1
#
# for [i, pair] in enumerate(pairs):
#     poly = pair
#     for step in range(40):
#         newpoly = poly
#         # print(i)
#         for [j, char] in enumerate(reversed(poly)):
#             for rule in rules:
#                 # print(poly[len(poly)-i-2] + char, rule[0])
#                 if poly[len(poly)-j-2] + poly[len(poly)-j-1] == rule[0]:
#                     # print(newpoly)
#                     newpoly = newpoly[len(poly)-i-1:] + rule[1] + newpoly[:len(poly)-i-1]
#                     # print(rule[1], "added to index", j)
#                     # print(newpoly)
#         # print(step, len(poly))
#         poly = newpoly


max = 0
min = 99999999999999999999999999
for count in dict.values():
    if count > max:
        max = count
    if count < min and count != 0:
        min = count
print((max-min)/2)

# def check(poly, round, index):
