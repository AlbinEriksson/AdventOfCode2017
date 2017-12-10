with open('input/input4', 'r') as input_file:
    lines = input_file.read().strip().split('\n')

answer = len(lines)

for line in lines:
    words = line.split(" ")
    for word in words:
        if words.count(word) > 1:
            answer -= 1
            break

print(answer)
