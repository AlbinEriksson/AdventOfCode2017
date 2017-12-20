with open('input/input11', 'r') as inputfile:
    steps = inputfile.read().strip().split(',')

x = 0
y = 0
z = 0
max_dist = 0

for step in steps:
    if step == 'n':
        x += 1
        z -= 1
    elif step == 'ne':
        y += 1
        z -= 1
    elif step == 'se':
        x -= 1
        y += 1
    elif step == 's':
        x -= 1
        z += 1
    elif step == 'sw':
        y -= 1
        z += 1
    elif step == 'nw':
        x += 1
        y -= 1
    dist = max(abs(x), abs(y), abs(z))
    if dist > max_dist:
        max_dist = dist

print(max_dist)
