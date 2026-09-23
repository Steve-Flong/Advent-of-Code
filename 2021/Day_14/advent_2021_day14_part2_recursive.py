from collections import defaultdict

def main():

    with open("advent_2021_day14.txt") as input:

        def expand_pair(pair, step):
            if step == 40:
                return
            left = pair[0]+rules[pair]
            right = rules[pair]+pair[1]
            element = rules[pair]
            elements[element] += 1
            expand_pair(left, step+1)
            expand_pair(right, step+1)
            return

        data = input.read().split("\n\n")
        template = data[0]
        pairs = data[1]
        elements = defaultdict(int)
        rules = {}
        for x in template:
            elements[x] += 1
        for line in pairs.splitlines():
            parts = line.split(" -> ")
            rules[parts[0]] = parts[1]
        for i in range(len(template) - 1):
            pair = template[i:i + 2]
            expand_pair(pair, 0)

        totals = {k: v for k, v in sorted(elements.items(), key=lambda item: item[1])}
        ordered = list(totals.values())
        print(ordered[-1]-ordered[0])
        print(ordered)


if __name__ == "__main__":
    main()