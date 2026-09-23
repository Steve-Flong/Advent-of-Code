
def main():
    array = []
    with open("advent_2016_day18.txt") as input:
        line = input.readline()
        array.append(line)
    for x in range(39):
        new_line = ""
        traps = ["^^.", ".^^", "^..", "..^"]
        for y in range(len(line)):
            if y == 0:
                upper = "." + array[-1][:2]

            elif y == len(line)-1:
                upper = array[-1][-2:] + "."
            else:
                upper = array[-1][y-1:y+2]
            if upper in traps:
                new_line += "^"
            else:
                new_line += "."
        array.append(new_line)
    count = 0
    for i in range(len(array)):
        count += array[i].count(".")
    print(count)


if __name__ == "__main__":
    main()