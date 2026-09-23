# change line 12 for part 2

def main():
    with open('advent_2021_day6.txt') as input:
        day = 0
        total = 0
        new_dict = {}
        dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for i in input.read().split(","):
                i = int(i)
                dict[i] += 1
        while day < 80:                                 # change to 256 for part 2
            for j in range(9):
                if j == 8:
                    new_dict[j] = dict[0]
                if j == 6:
                    value = (int(dict[0])+(int(dict[7])))
                    new_dict[j] = value
                elif j < 8:
                    new_dict[j] = dict[j+1]
            dict = new_dict.copy()
            new_dict = {}
            day += 1
        for x in range(9):
            total += dict[x]
        print(total)


if __name__ == '__main__':
    main()
