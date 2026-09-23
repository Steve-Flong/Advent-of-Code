def main():
    with open("advent_2021_day10.txt") as input:
        data = input.read()
        openers = {"{": "}", "(": ")", "[": "]", "<": ">"}
        completes = []
        scores = {")": 1, "]": 2, "}": 3, ">": 4}
        for string in data.splitlines():
            opening = []
            illegal = False
            for char in string:
                if char in openers:
                    opening.append(openers[char])
                if char in openers.values():
                    if opening[-1] == char:
                        opening.pop()
                        continue
                    else:
                        illegal = True
                        break
            if not illegal:
                score = 0
                while opening:
                    opener = opening.pop()
                    score = (score*5) + scores[opener]
                completes.append(score)
        completes.sort()
        print(completes[len(completes)//2])


if __name__ == "__main__":
    main()