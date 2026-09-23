def main():
    array = [[0] * 1000 for _ in range(1000)]
    with open("advent_2015_day6.txt") as input:
        for line in input.read().splitlines():
            inst = line.split(" ")
            if len(inst) == 5:
                del inst[0]
            r = inst[1]
            co_ords1 = r.split(",")
            a = co_ords1[0]
            a = int(a)
            b = co_ords1[1]
            b = int(b)
            t = inst[3]
            co_ords2 = t.split(",")
            c = int(co_ords2[0])
            d = int(co_ords2[1])
            if inst[0] == "toggle":
                for i in range(a, c + 1):
                    for j in range(b, d + 1):
                        array[i][j] += 2
            if inst[0] == "on":

                for i in range(a, c + 1):
                    for j in range(b, d + 1):
                        array[i][j] += 1
            if inst[0] == "off":
                for i in range(a, c + 1):
                    for j in range(b, d + 1):
                        if array[i][j] > 0:
                            array[i][j] -= 1
        x = 0
        for i in range(1000):
            for j in range(1000):
                x += array[i][j]
        print(x)


if __name__ == '__main__':
    main()
