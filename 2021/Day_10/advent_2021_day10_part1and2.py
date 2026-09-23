def main():
    with open("advent_2021_day10.txt") as input:
        data = input.read()
        openers = {"{": "}", "(": ")", "[": "]", "<": ">"}
        illegal = []
        completes = []
        scores = {")": 1, "]": 2, "}": 3, ">": 4}
        error_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
        for string in data.splitlines():
            opening = []
            legal = True
            for char in string:
                if char in openers:
                    opening.append(openers[char])
                if char in openers.values():
                    if opening[-1] == char:
                        opening.pop()
                        continue
                    else:
                        illegal.append(char)
                        legal = False
                        break
            if legal:
                score = 0
                while opening:
                    opener = opening.pop()
                    score = (score * 5) + scores[opener]
                completes.append(score)
            completes.sort()

        total = 0
        for x in illegal:
            total += error_score[x]
        print("Part 1 answer = ", total)
        print("Part 2 answer = ", completes[len(completes) // 2])


if __name__ == "__main__":
    main()