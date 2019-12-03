with open('input.txt', 'r') as f:
    inp = f.readline().split(',')
    inp[1] = 12
    inp[2] = 2
    print(inp)
    run = True
    index = 0
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
            else:
                pass
            index += 4
        except IndexError:
            run = False
        print(inp)
    print(inp[0])
