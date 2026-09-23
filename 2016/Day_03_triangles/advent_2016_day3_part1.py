def main():
    with open("advent_2016_day3.txt") as input:
        x = 0
        new_list1 = [[int(x) for x in y.split()] for y in input.read().splitlines()]
        print(new_list1)
        for triangle in new_list1:
            if (triangle[0]) < (triangle[1]) + (triangle[2]) and \
                    (triangle[1]) < (triangle[0]) + (triangle[2]) and \
                    (triangle[2]) < (triangle[0]) + (triangle[1]):
                x += 1
        print(x)


if __name__ == '__main__':
    main()
