def forloop():
    from prettytable import PrettyTable

    def while_loop(cleaned_code):
        final_code = []
        while_idx = None
        for i in range(len(cleaned_code)):
            codeline = cleaned_code[i]

            if 'while' in codeline:
                while_idx = i
                # The loop condition would be enclosed in brackets
                start_idx = codeline.index('(')
                end_idx = codeline.index(')')
                # Select the substring between start_idx and end_idx
                bool_condn = ''.join(codeline[start_idx:end_idx + 1])
                # Replace with
                final_code.append('if !{} goto({})'.format(bool_condn, None))
                while_idx = i
            elif '}' in codeline:
                final_code.append('goto({})'.format(while_idx + 1))
                #
                final_code[while_idx] = final_code[while_idx].replace('None', str(i + 2))
                while_idx = None
            else:
                final_code.append(codeline)
        return final_code

    with open('code.txt') as f:
        code = f.readlines()

    print('The Statement is:')
    print(''.join(code))

    cleaned_code = []
    for i in range(len(code)):
        if code[i] != '\n':
            if code[i][-1] == '\n':
                # don't include the \n at the end of each line
                cleaned_code.append(code[i][:-1].strip())
            else:
                # strip() removes the trailing whitespaces on both ends of string
                cleaned_code.append(code[i].strip())

    intermediate_code = []
    for i in range(len(cleaned_code)):
        codeline = cleaned_code[i]
        if 'for' in codeline:
            # for(init; condition; update1, update2, update3, etc.)\n
            conditions = codeline[4:-2].split(';')
            initialization = conditions[0].strip()
            break_condn = conditions[1].strip()
            updations = conditions[2].strip().split(',')
            intermediate_code.append(initialization)
            intermediate_code.append('while(' + break_condn + '){')
        elif '}' in codeline:
            for updation in updations:
                intermediate_code.append(updation + ';')
            intermediate_code.append('}')
        else:
            intermediate_code.append(codeline)

    # for(i=0; i<n; i++){
    #     // statements
    # }
    # is equivalent to:
    # i=0
    # while(i<n){
    #     // statements
    #     i++;
    # # }

    print('\nThe intermediate "while" code is:\n')
    for code in intermediate_code:
        print(code)

    final_code = while_loop(intermediate_code)

    print('\nThe Three Code generated is:')
    x1 = PrettyTable()
    x1.field_names = ['Index', 'Code']
    for i in range(len(final_code)):
        x1.add_row([i + 1, final_code[i]])

    print(x1)

def whileloop():
    from prettytable import PrettyTable

    def while_loop(cleaned_code):
        final_code = []
        while_idx = None
        for i in range(len(cleaned_code)):
            codeline = cleaned_code[i]

            if 'while' in codeline:
                while_idx = i
                # The loop condition would be enclosed in brackets
                start_idx = codeline.index('(')
                end_idx = codeline.index(')')
                # Select the substring between start_idx and end_idx
                bool_condn = ''.join(codeline[start_idx:end_idx + 1])
                final_code.append('if !{} goto({})'.format(bool_condn, None))
                while_idx = i
            elif '}' in codeline:
                final_code.append('goto({})'.format(while_idx + 1))
                final_code[while_idx] = final_code[while_idx].replace('None', str(i + 2))
                while_idx = None
            else:
                final_code.append(codeline)
        return final_code

    with open('code1.txt') as f:
        code = f.readlines()

    print('The Statement is:')
    print(''.join(code))

    cleaned_code = []
    for i in range(len(code)):
        if code[i] != '\n':
            if code[i][-1] == '\n':
                # don't include the \n at the end of each line
                cleaned_code.append(code[i][:-1].strip())
            else:
                cleaned_code.append(code[i].strip())

    final_code = while_loop(cleaned_code)

    final_code.append('END')

    print('\nThe Three Code Generated is:')
    x1 = PrettyTable()
    x1.field_names = ['Index', 'Code']
    for i in range(len(final_code)):
        x1.add_row([i + 1, final_code[i]])

    print(x1)

def if_else():
    from prettytable import PrettyTable

    x1 = PrettyTable()

    code = open('code3.txt', 'r')

    lines = code.read().splitlines()
    print('The Statement is :\n')
    for i in lines:
        print('\t', i)

    individual_lines = []

    for entry in lines:
        x = []
        x = entry.split(" ")
        individual_lines.append(x)

    goto, code1 = [], []
    for i in range(len(lines)):
        a = []
        if 'if' in lines[i]:
            a.append(lines[i])
            a.append('goto()')
            code1.append(a)
        elif 'return' in lines[i]:
            a.append('t1')
            a.append('=')
            a.append(individual_lines[i][-1][:len(individual_lines[i][-1]) - 1])
            code1.append(a)
            if ('if' in lines[i - 1]):
                code1.append(['goto()'])
            else:
                goto.append(len(code1))
        elif 'else' not in lines[i]:
            a.append(lines[i])
            code1.append(a)

    goto.append(len(code1) + 1)

    for i in range(len(code1)):
        if 'if' in code1[i][0]:
            code1[i][0] = code1[i][0].replace('A<B', '!A<B')

    j = -1
    for i in range(len(code1)):
        if 'goto()' in code1[i][0]:
            j += 1
            code1[i][0] = code1[i][0].replace('goto()', 'goto(' + str(goto[j]) + ')')
        elif 'goto()' in code1[i][-1]:
            j += 1
            code1[i][-1] = code1[i][-1].replace('goto()', 'goto(' + str(goto[j]) + ')')

    x1.field_names = ['Index', 'Code']
    for i in range(len(code1)):
        code2 = ""
        for j in code1[i]:
            code2 += j
        x1.add_row([i + 1, code2])

    x1.add_row([len(code1) + 1, "END"])
    print('\n\nThe Three Address Code Generated is :')
    print(x1)

if __name__ == '__main__':
    print("\n\nFor loop 3 address generation: \n")
    forloop()
    print("\n----------------BREAK-----------------")
    print("\n\nWhile loop 3 address generation: \n")
    whileloop()
    print("\n----------------BREAK-----------------")
    print("\n\nIf-Else loop 3 address generation: \n")
    if_else()
