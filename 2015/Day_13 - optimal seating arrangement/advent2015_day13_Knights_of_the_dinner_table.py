import itertools


def main():
    map = {}
    people = []
    with open("advent2015_day13.txt") as input:
        data = input.readlines()
        for i in data:
            j = i.split(" ")
            if j[2] == "lose":
                j[3] = -int(j[3])
            map[j[0] + (j[10])[:-2]] = int(j[3])
            if j[0] not in people:
                people.append(j[0])
        for i in people:                        # Added for part 2
            map["Steve" + i] = 0                #
            map[i + "Steve"] = 0                #
        people.append("Steve")                  #
        max_happiness = 0
        for order in itertools.permutations(people):
            happiness = 0
            for i in range(len(order)-1):
                happiness += map[order[i] + order[i + 1]] + map[order[i + 1] + order[i]]
            happiness += map[order[-1] + order[0]] + map[order[0] + order[-1]]
            if happiness > max_happiness:
                max_happiness = happiness
        print(max_happiness)


if __name__ == "__main__":
    main()
