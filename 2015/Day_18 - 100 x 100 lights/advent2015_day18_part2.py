def main():
    def get_value(x, y):
        try:
            if x == -1 or y == -1:
                return None
            return array[x][y] == "#"
        except IndexError:
            return None

    with open("advent2015_day18.txt") as input:
        data = input.read()
        array = [[x for x in y] for y in data.splitlines()]
        array_2 = [[x for x in y] for y in data.splitlines()]
        cycle = False
        for i in (0, 99):
            for j in (0, 99):
                array[i][j] = "#"
                array_2[i][j] = "#"
        for _ in range(100):
            count = 0
            if cycle:
                for x in range(len(array)):
                    for y in range(len(array[x])):
                        array[x][y] = array_2[x][y]
            for x in range(len(array)):
                for y in range(len(array[x])):
                    value = array[x][y]
                    adjacent = filter(lambda a: a is True,
                                      [get_value(x - 1, y), get_value(x + 1, y), get_value(x, y - 1),
                                       get_value(x, y + 1), get_value(x+1, y+1), get_value(x-1, y-1),
                                       get_value(x-1, y+1), get_value(x+1, y-1)])
                    lit = [x for x in adjacent]
                    if (x, y) == (0, 99) or (x, y) == (0, 0) or (x, y) == (99, 99) or (x, y) == (99, 0):
                        count += 1
                        continue
                    if value == "#" and (len(lit) == 2 or len(lit) == 3):
                        count += 1
                        continue
                    elif value == "#":
                        array_2[x][y] = "."
                        continue
                    if value == "." and len(lit) == 3:
                        array_2[x][y] = "#"
                        count += 1
                        continue
                    elif value == ".":
                        continue
            print(count)
            cycle = True


if __name__ == "__main__":
    main()