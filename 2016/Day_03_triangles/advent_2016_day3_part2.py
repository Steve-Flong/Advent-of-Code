
def main():
    with open("advent_2016_day3.txt") as input:
        x = 0
        new_list1 = []
        new_list = [x.split() for x in input.read().splitlines()]
        for i in range(3):
            for each in new_list:
                new_list1.append(int(each[i]))
        b = 0
        num = len(new_list1)
        real_num = int(num / 3)
        for a in range(real_num):
            if (new_list1[b]) < (new_list1[b + 1]) + (new_list1[b + 2]) and (new_list1[b + 1]) < (new_list1[b]) + \
                    (new_list1[b + 2]) and (new_list1[b + 2]) < (new_list1[b]) + (new_list1[b + 1]):
                x += 1
                b += 3
            else:
                b += 3
        print(x)


if __name__ == '__main__':
    main()
