def main():
    with open("advent_2021_day10.txt") as input:
        data = input.read()
        openers = {"{": "}", "(": ")", "[": "]", "<": ">"}
        illegal = []
        score = {")": 3, "]": 57, "}": 1197, ">": 25137}
        for string in data.splitlines():
            opening = []
            for char in string:
                if char in openers:
                    opening.append(openers[char])
                if char in openers.values():
                    if opening[-1] == char:
                        opening.pop()
                        continue
                    else:
                        illegal.append(char)
                        break
        total = 0
        for x in illegal:
            total += score[x]
        print(total)


if __name__ == "__main__":
    main()
