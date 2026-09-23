def compress(string):
    i = 0
    while True:
        pin_1 = i
        if "(" not in string:
            return len(string)
        while string[i] != "(" and i < len(string) - 1:
            i += 1
        extra = i - pin_1
        pin_2 = i + 1
        while string[i] != ")" and i < len(string) - 1:
            i += 1
        comp_nums = string[pin_2:i].split("x")
        pin_1 = i + 1
        pin_2 = pin_1 + int(comp_nums[0])
        return extra + (int(comp_nums[1]) * compress(string[pin_1: pin_2])) + compress(string[pin_2:])


with open("advent_2016_day9.txt") as input:
    full = "".join(i for i in input.read().splitlines())
    print(compress(full))
