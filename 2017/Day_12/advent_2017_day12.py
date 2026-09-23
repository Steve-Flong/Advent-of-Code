def main():
    with open("advent_2017_day12.txt") as input:
        def all_routes(start):
            queue = [x for x in d[start]]
            while queue:
                next = queue.pop()
                if next not in visited:
                    visited.append(next)
                for x in d[next]:
                    if x not in d[start]:
                        d[int(start)].append(x)
                        queue.append(x)
            return
        visited = []
        d = {}
        data = input.read()
        data2 = [x.split(" <-> ") for x in data.splitlines()]
        for y in data2:
            nums = [int(z) for z in y[1].split(", ")]
            d[int(y[0])] = nums
        groups = 0
        for x in d.keys():
            if x not in visited:
                all_routes(x)
                print("ID {} = {} programs".format(x, len(d[x])))
                groups += 1
        print(groups)


if __name__ == "__main__":
    main()
