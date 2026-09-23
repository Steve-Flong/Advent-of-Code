
def main():
    with open("advent2015_day23.txt") as input:
        inst = [x.replace(",", " ").split() for x in input.read().splitlines()]
        pointer = 0
        a = 0                                   # change to 1 for part 2
        b = 0
        while pointer < len(inst):
            cmd = inst[pointer][0]
            if cmd == "inc" and inst[pointer][1] == "b":
                b += 1
                pointer += 1
                continue
            if cmd == "jio":
                if a == 1:
                    pointer += int(inst[pointer][2])
                    continue
                else:
                    pointer += 1
                    continue
            if cmd == "inc":
                a += 1
                pointer += 1
                continue
            if cmd == "tpl":
                a *= 3
                pointer += 1
                continue
            if cmd == "hlf":
                a //= 2
                pointer += 1
                continue
            if cmd == "jie":
                if a % 2 == 0:
                    pointer += int(inst[pointer][2])
                    continue
                else:
                    pointer += 1
                    continue
            if cmd == "jmp":
                pointer += int(inst[pointer][1])
                continue
        print(b)


if __name__ == "__main__":
    main()



