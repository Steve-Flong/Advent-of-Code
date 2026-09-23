def main():
    with open("advent_2016_day1.txt") as input:
        x, y = 0, 0
        facing_list = ["north", "east", "south", "west"]
        a = 0
        found = False
        visited_blocks = []
        directions = input.read()
        list_of_directions = directions.split(", ")
        print(list_of_directions)
        for instruction in list_of_directions:
            if found:
                break
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
            number = int(forward)
            for blocks in range(number):
                if a == 0:
                    y += 1
                elif a == 1:
                    x += 1
                elif a == 2:
                    y -= 1
                else:
                    x -= 1
                location = (x, y)
                if location in visited_blocks:
                    print(abs(x) + abs(y))
                    found = True
                    break
                else:
                    visited_blocks.append(location)
                continue


if __name__ == '__main__':
    main()
