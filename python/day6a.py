with open('input/input6', 'r') as input_file:
    banks = [int(blocks) for blocks in input_file.read().strip().split('\t')]

bank_history = []
answer = 0

while banks not in bank_history:
    bank_history.append([i for i in banks])

    blocks = max(banks)
    index = banks.index(blocks)
    banks[index] = 0

    for i in range(blocks):
        index = (index + 1) % len(banks)
        banks[index] += 1

    answer += 1

print(answer)
