
def main():

    with open("advent_2017_day8.txt") as input:

        ls = [x.strip().split() for x in input.readlines()]
        d = {"==": "eq", ">=": "ge", "<=": "le", "!=": "ne", ">": "gt", "<": "lt"}
        l, h = {}, 0
        for y in ls:
            if getattr(l.get(y[4], 0), "__"+d[y[5]]+"__")(int(y[6])):
                l[y[0]] = l.get(y[0], 0) + (int(y[2]) if y[1] == "inc" else -int(y[2]))
                h = max(h, l[y[0]])
        print(max(l.values()))
        print(h)


if __name__ == "__main__":
    main()
