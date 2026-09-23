def main():
    with open("advent_2016_day1.txt") as input:
        x, y = 0, 0
        facing_list = ["north", "east", "south", "west"]
        a = 0
        directions = input.read()
        list_of_directions = directions.split(", ")
        for instruction in list_of_directions:
            turn = instruction[0]
            if turn == "R" and a < 3:
                a += 1
            elif turn == "R" and a == 3:
                a = 0
            elif turn == "L" and a > 0:
                a -= 1
            else:
                a = 3
            forward = instruction[1:]
            if a == 0:
                y += int(forward)
            elif a == 1:
                x += int(forward)
            elif a == 2:
                y -= int(forward)
            else:
                x -= int(forward)
            continue
        print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
