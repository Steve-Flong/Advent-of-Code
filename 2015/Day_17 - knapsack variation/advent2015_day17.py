max_size = 150


# part 1
def containers(current_size, sizes):
    if current_size == max_size:
        return 1
    if current_size > max_size or len(sizes) == 0:
        return 0
    start = sizes[0]
    rest = sizes[1:]
    return containers(current_size + start, rest) + containers(current_size, rest)


# part 2
def containers_2(current_size, sizes, count=4):
    if current_size == max_size and count == 0:
        return 1
    if current_size > max_size or len(sizes) == 0:
        return 0
    start = sizes[0]
    rest = sizes[1:]
    return containers_2(current_size + start, rest, count-1) + containers_2(current_size, rest, count)


if __name__ == "__main__":
    with open("advent2015_day17.txt") as input:
        boxes = [int(x) for x in input.readlines()]
        print(containers(0, boxes))
        print(containers_2(0, boxes))
