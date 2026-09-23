def main():

    with open("advent_2017_day9.txt") as input:
        data = input.read()
        garbage = False
        miss_one = False
        score = 0
        group = 0
        garbage_count = 0
        for x in range(len(data)):
            if miss_one:
                miss_one = False
            elif data[x] == "!":
                miss_one = True
            elif garbage:
                if data[x] != ">":
                    garbage_count += 1
                else:
                    garbage = False
            elif data[x] == "<":
                garbage = True
            elif data[x] == "{":
                group += 1
                score += group
            elif data[x] == "}":
                group -= 1
        print("total score = {}".format(score))
        print("total garbage count = {}".format(garbage_count))


if __name__ == "__main__":
    main()
