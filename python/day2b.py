with open('input/input2', 'r') as inputfile:
    rows = [
        [int(number) for number in row.split('\t')]
        for row in inputfile.read().strip().split('\n')]

answer = 0

for row in rows:
    for index1, number1 in enumerate(row):
        for index2, number2 in enumerate(row):
            if index1 != index2: 
                quotient = number1 / number2
                if int(quotient) == quotient:
                    answer += quotient

print(answer)
