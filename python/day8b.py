with open('input/input8', 'r') as inputfile:
    variables = {}
    highest = 0
    for line in inputfile.read().strip().split('\n'):
        words = line.split(' ')
        assign_to = words[0]
        operation = words[1]
        amount = int(words[2])
        compare_var = words[4]
        comparator = words[5]
        compare_const = int(words[6])

        if assign_to not in variables:
            variables[assign_to] = 0

        if compare_var not in variables:
            variables[compare_var] = 0
        
        condition = False

        if comparator == '<':
            condition = variables[compare_var] < compare_const
        elif comparator == '<=':
            condition = variables[compare_var] <= compare_const
        elif comparator == '>':
            condition = variables[compare_var] > compare_const
        elif comparator == '>=':
            condition = variables[compare_var] >= compare_const
        elif comparator == '==':
            condition = variables[compare_var] == compare_const
        elif comparator == '!=':
            condition = variables[compare_var] != compare_const

        if condition:
            if operation == 'inc':
                variables[assign_to] += amount
            elif operation == 'dec':
                variables[assign_to] -= amount
        
        if variables[assign_to] > highest:
            highest = variables[assign_to]
    
    print(highest)
