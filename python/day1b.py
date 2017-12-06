with open('input/input1', 'r') as inputfile:
    sequence = inputfile.read().strip()

half_length = len(sequence) // 2
answer = 0

for index, char in enumerate(sequence):
    if index < half_length:
        char2 = sequence[index + half_length]
    else:
        char2 = sequence[index - half_length]
    
    if char == char2:
        answer += int(char)

print(answer)
