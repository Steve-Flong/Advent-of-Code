def main():

    with open("advent_2017_day11.txt") as input:
        dircs = {"ne": 0, "nw": 0, "sw": 0, "se": 0, "n": 0, "s": 0}
        data = input.read()
        dir = data.strip("\n").split(",")
        for each in dir:
            dircs[each] += 1
        print(dircs)
        dircs["se"] += 43
        dircs["sw"] += 43
        north_east = dircs["ne"] - dircs["sw"]
        south_east = dircs["se"] - dircs["nw"]
        print(north_east+south_east)

if __name__ == "__main__":
    main()