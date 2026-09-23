def main():
    with open("advent_2016_day2.txt") as input:

        array = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]
        x, y = 2, 0
        for line in input.read().splitlines():
            for inst in line:
                if inst == "U":
                    if x == 0 or array[(x - 1)][y] == 0:
                        continue
                    else:
                        x -= 1
                        continue

                if inst == "D":
                    if x == 4 or array[(x + 1)][y] == 0:
                        continue
                    else:
                        x += 1
                        continue

                if inst == "L":
                    if y == 0 or array[x][y - 1] == 0:
                        continue
                    else:
                        y -= 1
                        continue

                if inst == "R":
                    if y == 4 or array[(x)][y + 1] == 0:  # as above with right hand edge
                        continue
                    else:
                        y += 1
                        continue
            print(array[x][y])


if __name__ == '__main__':
    main()
