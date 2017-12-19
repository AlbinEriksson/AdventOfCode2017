with open('input/input9', 'r') as inputfile:
    stream = inputfile.read().strip()

score = 0
group_depth = 0
in_garbage = False
ignore_next = False
for c in stream:
    if ignore_next:
        ignore_next = False
        continue
    elif not in_garbage:
        if c == '<':
            in_garbage = True
        elif c == '{':
            group_depth += 1
            score += group_depth
        elif c == '}':
            group_depth -= 1
    else:
        if c == '>':
            in_garbage = False
        elif c == '!':
            ignore_next = True
print(score)
