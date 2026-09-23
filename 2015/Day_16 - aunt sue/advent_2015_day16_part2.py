facts = {"children": 3,
         "cats": 7,
         "samoyeds": 2,
         "pomeranians": 3,
         "akitas": 0,
         "vizslas": 0,
         "goldfish": 5,
         "trees": 3,
         "cars": 2,
         "perfumes": 1
         }


def main():
    with open("advent2015_day16.txt") as input:
        data = input.read()
        for sue in data.splitlines():
            dna = sue.split(", ")
            further_split_0 = dna[0].split(": ")
            item_1 = further_split_0[1]
            no_1 = int(further_split_0[2])
            further_split_1 = dna[1].split(": ")
            item_2 = further_split_1[0]
            no_2 = int(further_split_1[1])
            further_split_2 = dna[2].split(": ")
            item_3 = further_split_2[0]
            no_3 = int(further_split_2[1])
            items = {item_1: no_1, item_2: no_2, item_3: no_3}
            greater_than = ["cats", "trees"]
            less_than = ["pomeranians", " goldfish"]
            count = 0
            for item in items:
                if item in greater_than:
                    if items[item] > facts[item]:
                        count += 1
                elif item in less_than:
                    if items[item] < facts[item]:
                        count += 1
                else:
                    if items[item] == facts[item]:
                        count += 1
            if count == 3:
                print(further_split_0[0])


if __name__ == "__main__":
    main()