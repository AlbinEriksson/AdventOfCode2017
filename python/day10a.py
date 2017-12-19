with open('input/input10', 'r') as inputfile:
    lengths = [int(n) for n in inputfile.read().strip().split(',')]

numbers = list(range(256))
position = 0
skip_size = 0

for length in lengths:
    distance_from_end = len(numbers) - position - length
    if distance_from_end < 0:
        sub_list = numbers[position: ] + numbers[: -distance_from_end]
    else:
        sub_list = numbers[position: position + length]
    for number in sub_list:
        numbers.remove(number)
    for index, number in enumerate(sub_list):
        if distance_from_end < 0:
            if index < -distance_from_end:
                numbers.insert(0, number)
            else:
                numbers.insert(position, number)
        else:
            numbers.insert(position, number)
    position = (position + length + skip_size) % len(numbers)
    skip_size += 1

print(numbers[0] * numbers[1])
