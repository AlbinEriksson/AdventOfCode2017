with open('input/input3', 'r') as input_file:
    square = int(input_file.read().strip())

number = 0
grid = {(0, 0): 1}

x = 0
y = 0

while number < square:
    ring = max(abs(x), abs(y))
    if x == ring:
        if y == ring:
            x += 1
        elif y == -ring:
            x -= 1
        else:
            y -= 1
    elif x == -ring:
        if y == ring:
            x += 1
        else:
            y += 1
    elif y == -ring:
        x -= 1
    else:
        x += 1
    number = 0
    for offset in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        position = (offset[0] + x, offset[1] + y)
        if position in grid.keys():
            number += grid[position]
    grid[(x, y)] = number

print(number)
