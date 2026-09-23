def main():
    with open("advent_2017_day7.txt") as input:
        def calculate_weight(platform):

            if platform not in towers_list:
                return singles_dict[platform]
            temp_list = []
            for x in towers[platform]:
                weight = calculate_weight(x)
                temp_list.append(weight)
            print(platform + " = " + str(temp_list))
            for y in temp_list:
                if temp_list.count(y) == 1:
                    print("this is unbalanced..." + str(temp_list))
                    odd = temp_list.index(y)
                    diff = abs(temp_list[odd-1]-temp_list[odd])
                    print(towers[platform][odd])
                    print("correct weight = " + str(singles_dict[towers[platform][odd]]-diff))
                    quit()
            return singles_dict[platform] + sum(temp_list)

        data = input.read()
        towers_list = []
        singles_dict = {}
        towers = {}
        for line in data.splitlines():
            weights = line.split()
            if ">" in line:
                towers_list.append(weights[0])
                disc = weights[3:]
                towers[weights[0]] = [x.strip(",") for x in disc]
            singles_dict[weights[0]] = int(weights[1].strip("()"))

        calculate_weight("bpvhwhh")


if __name__ == '__main__':
    main()
