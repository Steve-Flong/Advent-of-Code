def main():
    with open('advent_2021_day9.txt') as input:
        data = input.read()
        floor = [list(map(int, row)) for row in data.splitlines()]

        def get_value(row, col):
            if row == -1 or col == -1:
                return None
            try:
                return floor[row][col]
            except IndexError:
                return None

        def check_neighbours(row, col):
            if row == -1 or col == -1:
                return None
            elif row == 100 or col == 100:
                return None
            else:
                return row, col

        def get_neighbours(co_ords):
            x, y = co_ords
            adjacent2 = filter(lambda v: v is not None, [
                check_neighbours(x, y + 1),
                check_neighbours(x - 1, y),
                check_neighbours(x, y - 1),
                check_neighbours(x + 1, y)
            ])
            for i in adjacent2:
                p, q = i
                if i not in visited and i not in to_visit and floor[p][q] < 9:
                    to_visit.append(i)
            return

        def find_valley(coords):
            visited.append(coords)
            get_neighbours(coords)
            while to_visit:
                new_coords = to_visit.pop()
                visited.append(new_coords)
                get_neighbours(new_coords)

            return len(visited)

        low_points = []
        for row_index, row in enumerate(floor):
            for col_index in range(len(row)):
                adjacent = filter(lambda v: v is not None, [
                    get_value(row_index, col_index + 1),
                    get_value(row_index - 1, col_index),
                    get_value(row_index, col_index - 1),
                    get_value(row_index + 1, col_index)
                ])
                value = floor[row_index][col_index]
                if all([value < a for a in adjacent]):
                    low_points.append((row_index, col_index))
        sub_totals = []
        for point in low_points:
            visited = []
            to_visit = []
            sub_total = find_valley(point)
            sub_totals.append(sub_total)
        sub_totals.sort()
        result = sub_totals[-1] * sub_totals[-2] * sub_totals[-3]
        print(result)


if __name__ == '__main__':
    main()