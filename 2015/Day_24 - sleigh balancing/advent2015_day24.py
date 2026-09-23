from itertools import combinations
from operator import mul
import functools


def main():
    with open('advent2015_day24.txt') as file:
        weights = [int(x) for x in file.read().splitlines()]
        group_size = sum(weights) / 4
        for i in range(len(weights)):
            list = [functools.reduce(mul, c) for c in combinations(weights, i)
                    if sum(c) == group_size]
            if list:
                return min(list)


if __name__ == "__main__":
    print(main())
