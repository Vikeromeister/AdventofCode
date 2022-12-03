x_target = [241, 275]
y_target = [-75, -49]
# print(75*76/2)
# print(22*23/2)

def sim(x, y):
    x_curr = 0
    y_curr = 0
    x_vel = x
    y_vel = y
    while (x_curr < 276 and x_vel > 0) or y_curr > -76:
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
        x_curr += x_vel
        y_curr += y_vel
        if x_curr in range(241,276) and y_curr in range(-75,-48):
            print(x, y)
            return x, y
    return None

velocities = []
for x in range(21, 277):
    print("x=", x)
    for y in range(-77, 77):
        if sim(x, y):
            velocities.append(sim(x, y))

print(velocities)
print(len(velocities))

for i in range(-75, -48):
    print(i)