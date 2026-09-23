from collections import defaultdict


def main():
    def traverse(twice, start='start', seen=None):
        if seen is None:
            seen = {"start"}
        if start == 'end':
            yield 1
        for x in links[a]:
            if x.islower():
                if x not in seen:
                    yield from traverse(twice, x, seen.union({b}))
                elif twice and x not in {'start', 'end'}:
                    yield from traverse(False, x, seen)
            else:
                yield from traverse(twice, b, seen)

    with open("advent_2021_day12_part1.txt") as input:
        data = input.read()
        links = defaultdict(list)
        for line in data.splitlines():
            a, b = line.split('-')
            links[a].append(b)
            links[b].append(a)

    print(sum(traverse(twice=False)))
    print(sum(traverse(twice=True)))


if __name__ == "__main__":
    main()
