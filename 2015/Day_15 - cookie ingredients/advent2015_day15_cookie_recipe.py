import itertools
import operator


def cookies(n, nums):
    max_value = 0
    for var in itertools.combinations_with_replacement(range(n + 1), 3):
        combi = list(map(operator.sub, var + (n,), (0,) + var))
        if max(combi) < n and 0 not in combi:
            totals = []
            for i in range(4):
                total = (int(combi[0]) * nums[0][i]) + (int(combi[1]) * nums[1][i]) \
                        + (int(combi[2]) * nums[2][i]) + (int(combi[3]) * nums[3][i])
                if total < 0:
                    total = 0
                totals.append(total)
            val = totals[0] * totals[1] * totals[2] * totals[3]
            # calories = (int(combi[0]) * nums[0][4]) + (int(combi[1]) * nums[1][4]) \
            #            + (int(combi[2]) * nums[2][4]) + (int(combi[3]) * nums[3][4])
            # for part 2....uncomment lines 18 + 19....and calories == 500 added to line 21
            if val > max_value:
                max_value = val
    return max_value


if __name__ == "__main__":
    with open("advent2015_day15.txt") as input:
        ingreds = {}
        values = []
        for line in input.read().splitlines():
            items = line.split(": ")
            parts = items[1].split(", ")
            value = []
            for x in parts:
                y = x.split(" ")
                value.append(int(y[1]))
            values.append(value)
        print(cookies(100, values))
