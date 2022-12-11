input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

input ="""noop
noop
noop
addx 3
addx 7
noop
noop
noop
noop
addx 6
noop
addx -1
noop
addx 5
addx 1
noop
addx 4
noop
noop
noop
noop
addx 6
addx -1
noop
addx 3
addx -13
addx -22
noop
noop
addx 3
addx 2
addx 11
addx -4
addx 11
addx -10
addx 2
addx 5
addx 2
addx -2
noop
addx 7
addx 3
addx -2
addx 2
addx 5
addx 2
addx -2
addx -8
addx -27
addx 5
addx 2
addx 21
addx -21
addx 3
addx 5
addx 2
addx -3
addx 4
addx 3
addx 1
addx 5
noop
noop
noop
noop
addx 3
addx 1
addx 6
addx -31
noop
addx -4
noop
noop
noop
noop
addx 3
addx 7
noop
addx -1
addx 1
addx 5
noop
addx 1
noop
addx 2
addx -8
addx 15
addx 3
noop
addx 2
addx 5
noop
noop
noop
addx -28
addx 11
addx -20
noop
addx 7
addx -2
addx 7
noop
addx -2
noop
addx -6
addx 11
noop
addx 3
addx 2
noop
noop
addx 7
addx 3
addx -2
addx 2
addx 5
addx 2
addx -16
addx -10
addx -11
addx 27
addx -20
noop
addx 2
addx 3
addx 5
noop
noop
noop
addx 3
addx -2
addx 2
noop
addx -14
addx 21
noop
addx -6
addx 12
noop
addx -21
addx 24
addx 2
noop
noop
noop""".splitlines()

def cycle():
    global summ, left, toadd, x, time, screen
    if time in [20, 60, 100, 140, 180, 220]:
        # print(f"x is {x}, time is {time}, signal strength is {x*time}, summ is {summ}")
        summ += time * x
    left -= 1
    if left == 0:
        x += toadd
    if time % 40 == 1:
        screen.append('')
    if abs((time % 40) - x) < 2:
        screen[-1] = screen[-1] + '#'
    else:
        screen[-1] = screen[-1] + ' '
    time += 1
    
time = 1
x = 1
left = 0
toadd = 0
summ = 0
screen = []

for command in input:
    if command == 'noop':
        left = 1
        toadd = 0
        cycle()
    else:
        left = 2
        toadd = int(command.split(' ')[1])
        cycle()
        cycle()
    # print(command, time, x)

print(summ)
for row in screen:
    print(row)