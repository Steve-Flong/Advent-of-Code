def main():
    with open("advent_2016_day12.txt") as input:
        inst = [x.split() for x in input.read().splitlines()]

    a = 0
    b = 0
    c = 1
    d = 0
    dict = {"a": a, "b": b, "c": c, "d": d}
    i = 0
    while i < len(inst):
        if inst[i][0] == "cpy":
            try:
                dict[inst[i][2]] = int(inst[i][1])
            except:
                dict[inst[i][2]] = dict[inst[i][1]]
        if inst[i][0] == "inc":
            dict[inst[i][1]] += 1
        if inst[i][0] == "dec":
            dict[inst[i][1]] -= 1
        if inst[i][0] == "jnz":
            try:
                if int(inst[i][1]) != 0:
                    i += int(inst[i][2])
                    continue
            except:
                if dict[inst[i][1]] != 0:
                    i += int(inst[i][2])
                    continue

        i += 1
    print(dict)
    print(a, b, c, d)


if __name__ == "__main__":
    main()
