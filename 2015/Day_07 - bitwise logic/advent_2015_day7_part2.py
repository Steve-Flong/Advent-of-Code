circuit = {"b": 956}
instructions = []


def main():
    def parse(step):
        print("Now parsing" + step)
        for wire_instruction in instructions:
            commands = wire_instruction
            if wire_instruction[len(wire_instruction) - 1] == step:
                break
        wire = commands[-1]
        if len(commands) == 3:
            if commands[0] not in circuit and not commands[0].isdigit():
                parse(commands[0])
            if commands[0].isdigit():
                circuit[wire] = int(commands[0])
            else:
                circuit[wire] = circuit[commands[0]]
            return

        if commands[0] == "NOT":
            if commands[1] not in circuit:
                parse(commands[1])
            circuit[wire] = 0xffff - circuit[commands[1]]
            return

        if commands[0] not in circuit and not commands[0].isdigit():
            parse(commands[0])

        if commands[2] not in circuit and not commands[2].isdigit():
            parse(commands[2])

        if commands[1] == "RSHIFT":
            if not commands[0].isdigit():
                circuit[wire] = circuit[commands[0]] >> int(commands[2])
            else:
                circuit[wire] = int(commands[0]) >> int(commands[2])

        if commands[1] == "LSHIFT":
            if not commands[0].isdigit():
                circuit[wire] = circuit[commands[0]] << int(commands[2])
            else:
                circuit[wire] = int(commands[0]) << int[commands[2]]

        if commands[1] == "AND":
            if commands[0].isdigit():
                circuit[wire] = int(commands[0]) & circuit[commands[2]]
            else:
                circuit[wire] = circuit[commands[0]] & circuit[commands[2]]

        elif commands[1] == "OR":

            if commands[0].isdigit():
                circuit[wire] = int(commands[0]) | circuit[commands[2]]
            else:
                circuit[wire] = circuit[commands[0]] | circuit[commands[2]]

    with open('advent_2015_day7.txt') as input:
        for line in input:
            instructions.append(line.split())
    parse('a')
    print(circuit.get('a'))


if __name__ == '__main__':
    main()

