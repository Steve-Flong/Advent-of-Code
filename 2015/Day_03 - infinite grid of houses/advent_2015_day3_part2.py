visited = []
number_of_visits = []
x, y = 0, 0
a, b = 0, 0


def main():
    def grid_ref_check_even():
        grid_ref = x, y
        if grid_ref in visited:
            place = visited.index(grid_ref)
            number_of_visits[place] += 1
        else:
            visited.append(grid_ref)
            number_of_visits.append(1)
        return

    def grid_ref_check_odd():

        grid_ref = a, b
        if grid_ref in visited:
            place = visited.index(grid_ref)
            number_of_visits[place] += 1
        else:
            visited.append(grid_ref)
            number_of_visits.append(1)
        return

    def function_even():
        global x, y
        if move == "^":
            y += 1
            grid_ref_check_even()
        elif move == "v":
            y -= 1
            grid_ref_check_even()
        elif move == "<":
            x -= 1
            grid_ref_check_even()
        elif move == ">":
            x += 1
            grid_ref_check_even()
        else:
            return

    def function_odd():
        global a, b
        if move == "^":
            b += 1
            grid_ref_check_odd()
        elif move == "v":
            b -= 1
            grid_ref_check_odd()
        elif move == "<":
            a -= 1
            grid_ref_check_odd()
        elif move == ">":
            a += 1
            grid_ref_check_odd()
        else:
            return

    with open("advent_2015_day3.txt") as input:
        grid_ref_even = x, y  # santa
        visited.append(grid_ref_even)
        number_of_visits.append(2)
        q = 0
        for move in input.read():
            if q % 2 == 0:
                function_even()
            else:
                function_odd()
            q += 1
        print(len(visited))


if __name__ == '__main__':
    main()
