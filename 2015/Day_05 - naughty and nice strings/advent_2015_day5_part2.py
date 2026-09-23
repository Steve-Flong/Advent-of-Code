def main():
    with open("advent_2015_day5.txt") as input:
        nice = 0
        for x in input.read().splitlines():
            length = len(x)
            pair = False
            one_letter_gap = False
            for i in range(length):
                if i < (length - 1):
                    j = i + 1
                    string = x[i] + x[j]
                    if x.count(string) >= 2:
                        pair = True
                for _ in range(length - j):
                    if i <= (length - 3) and x[i] == x[i + 2]:
                        one_letter_gap = True
                    j += 1
            if pair and one_letter_gap:
                nice += 1
        print(nice)


if __name__ == '__main__':
    main()
