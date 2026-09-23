def main():
    array = [["."] * 50 for i in range(6)]
    with open("advent_2016_day8.txt") as input:
        for com in input.read().splitlines():
            coms = com.split(" ")
            if coms[0] == "rect":
                nums = coms[1].split("x")
                for x in range(int(nums[1])):
                    for y in range(int(nums[0])):
                        array[x][y] = "#"
            if coms[1] == "row":
                row = int(coms[2].split("=")[1])
                shift = int(coms[4])

                for i in range(shift):
                    new_row = ["" for j in range(50)]
                    for x in range(50):
                        new_row[x] = array[row][x - 1]
                    array[row] = new_row
            if coms[1] == "column":
                col = int(coms[2].split("=")[1])
                shift = int(coms[4])
                for i in range(shift):
                    new_col = ["" for i in range(6)]
                    for x in range(6):
                        new_col[x] = array[x - 1][col]
                    for x in range(len(new_col)):
                        array[x][col] = new_col[x]
    count = 0
    for x in range(6):
        for y in range(50):
            if array[x][y] == "#":
                count += 1
    print(count)


if __name__ == "__main__":
    main()