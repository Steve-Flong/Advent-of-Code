def main():
    with open("advent_2016_day18.txt") as input:
        line = input.readline()
    count = line.count(".")
    for x in range(399999):
        new_line = ""
        traps = ["^^.", ".^^", "^..", "..^"]
        for y in range(len(line)):
            if y == 0:
                upper = "." + line[:2]
            elif y == len(line)-1:
                upper = line[-2:] + "."
            else:
                upper = line[y-1:y+2]
            if upper in traps:
                new_line += "^"
            else:
                new_line += "."
        count += new_line.count(".")
        line = new_line
    print(count)


if __name__ == "__main__":
    main()
