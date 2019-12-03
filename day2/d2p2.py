for noun in range(0, 100):
    for verb in range(0, 100):
        with open('input.txt', 'r') as f:
            inp = f.read().split(',')
            index = 0
            inp[1] = noun
            inp[2] = verb
            run = True
            while run:
                try:
                    intcode = int(inp[index])
                    if intcode == 1:
                        inp[int(inp[index + 3])] = \
                            int(inp[int(inp[index + 1])]) + \
                            int(inp[int(inp[index + 2])])
                    elif intcode == 2:
                        inp[int(inp[index + 3])] = \
                            int(inp[int(inp[index + 1])]) * \
                            int(inp[int(inp[index + 2])])
                    elif intcode == 99:
                        run = False
                        continue
                    index += 4
                except IndexError:
                    run = False
                if int(inp[0]) == 19690720:
                    print(100 * int(noun) + int(verb))
