with open('input/input5', 'r') as input_file:
    offsets = [int(number) for number in input_file.read().strip().split('\n')]

index = 0
answer = 0

while 0 <= index < len(offsets):
    jumps = offsets[index]

    if offsets[index] >= 3:
        offsets[index] -= 1
    else:
        offsets[index] += 1

    index += jumps
    answer += 1

print(answer)
