with open("advent_2016_day10.txt") as input:
    bots = {}
    inst = {}
    queue = {}
    output = {}
    for row in input.read().splitlines():
        new_row = row.split()
        if new_row[0] == "value":
            if new_row[5] not in bots:
                bots[new_row[5]] = [int(new_row[1])]
            else:
                bots[new_row[5]].append(int(new_row[1]))
                bots[new_row[5]].sort()
                queue[new_row[5]] = bots[new_row[5]]
        if new_row[0] == "bot":
            inst[new_row[1]] = new_row[2:]

    while [17, 61] not in queue.values():                   # while queue.values() for part 2
        current = queue.popitem()
        instruction = inst[current[0]]
        if instruction[3] == "bot":
            if instruction[4] not in bots:
                bots[instruction[4]] = [int(current[1][0])]
            else:
                bots[instruction[4]].append(int(current[1][0]))
                bots[instruction[4]].sort()
                queue[instruction[4]] = bots[instruction[4]]
        if instruction[3] == "output":
            output[instruction[4]] = int(current[1][0])
        if instruction[8] == "bot":
            if instruction[9] not in bots:
                bots[instruction[9]] = [int(current[1][1])]
            else:
                bots[instruction[9]].append(int(current[1][1]))
                bots[instruction[9]].sort()
                queue[instruction[9]] = bots[instruction[9]]
        if instruction[9] == "output":
            output[instruction[9]] = int(current[1][1])
    print(queue)
    print(output)

