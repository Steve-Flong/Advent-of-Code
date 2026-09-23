def main():

    with open("advent_2021_day14.txt") as input:
        data = input.read().split("\n\n")
        template = data[0]
        pairs = data[1]
        elements = {}
        rules = {}
        for line in pairs.splitlines():
            parts = line.split(" -> ")
            rules[parts[0]] = parts[1]
        polymer = list(template)
        for x in range(18):
            insertion_index = 1
            for i in range(len(template)-1):
                slice = template[i:i+2]
                polymer.insert(i+insertion_index, rules[slice])
                insertion_index += 1
            template = "".join(polymer)
        for element in template:
            if element not in elements:
                elements[element] = 1
            else:
                elements[element] += 1
        totals = {k: v for k, v in sorted(elements.items(), key=lambda item: item[1])}
        ordered = list(totals.values())
        print(ordered[-1]-ordered[0])


if __name__ == "__main__":
    main()