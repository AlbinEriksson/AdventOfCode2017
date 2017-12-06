with open('input/input1', 'r') as inputfile:
    sequence = inputfile.read().strip()

answer = 0

for index, char in enumerate(sequence):
    if index == len(sequence) - 1:
        char2 = sequence[0]
    else:
        char2 = sequence[index + 1]
    
    if char == char2:
        answer += int(char)

print(answer)
