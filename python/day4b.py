with open('input/input4', 'r') as input_file:
    lines = input_file.read().strip().split('\n')

answer = len(lines)

for line in lines:
    words = line.split(" ")
    sorted_words = [sorted(words[i]) for i in range(len(words))]
    for word in sorted_words:
        if sorted_words.count(word) > 1:
            answer -= 1
            break

print(answer)
