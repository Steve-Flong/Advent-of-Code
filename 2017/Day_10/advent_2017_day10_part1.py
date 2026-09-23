def main():

    with open("advent_2017_day10.txt") as input:
        data = input.read()
        skip = 0
        total_shift = 0
        main_list = [x for x in range(256)]
        elements = [int(x) for x in data.split(",")]
        for length in elements:
            sublist = main_list[:length]
            sublist.reverse()
            new_list = sublist + main_list[length:]
            move = (skip + length) % 256
            total_shift += move
            main_list = new_list[move:] + new_list[:move]
            skip += 1
        final_shift = total_shift % 256
        final_list = main_list[-final_shift:] + main_list[:-final_shift]
        print(final_list)
        print(final_list[0]*final_list[1])


if __name__ == "__main__":
    main()