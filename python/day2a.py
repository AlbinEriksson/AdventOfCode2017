with open('input/input2', 'r') as inputfile:
    rows = [
        [int(number) for number in row.split('\t')]
        for row in inputfile.read().strip().split('\n')]

answer = 0

for row in rows:
    answer += max(row) - min(row)

print(answer)
