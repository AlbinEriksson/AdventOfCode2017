with open('input/input9', 'r') as inputfile:
    stream = inputfile.read().strip()

in_garbage = False
ignore_next = False
garbage = 0
for c in stream:
    if ignore_next:
        ignore_next = False
        continue
    elif not in_garbage:
        if c == '<':
            in_garbage = True
    else:
        if c == '>':
            in_garbage = False
        elif c == '!':
            ignore_next = True
        else:
            garbage += 1
print(garbage)
