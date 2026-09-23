def main():
    with open("advent_2016_day2.txt") as input:
        x = 5
        for line in input.read().splitlines():
            for inst in line:
                if inst == "U":
                    if x in (4, 5, 6, 7, 8, 9):
                        x -= 3
                        continue
                if inst == "D":
                    if x in (1, 2, 3, 4, 5, 6):
                        x += 3
                    continue
                if inst == "R":
                    if x in (1, 2, 4, 5, 7, 8):
                        x += 1
                    continue
                if inst == "L":
                    if x in (2, 3, 5, 6, 8, 9):
                        x -= 1
                    continue
            print(x)


if __name__ == '__main__':
    main()
