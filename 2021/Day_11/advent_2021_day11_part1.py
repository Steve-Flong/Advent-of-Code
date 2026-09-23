def main():
    with open("advent_2021_day11.txt") as input:
        data = input.read()
        cavern_map = [[int(x) for x in y] for y in data.splitlines()]
        moves = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        flashes = 0

        def check_adj(row, col):
            if row == -1 or col == -1 or row == 10 or col == 10:
                return None
            else:
                return (row, col)

        def flash(row, col):
            flashed.add((row, col))
            cavern_map[row][col] = 0
            adjacent = filter(lambda v: v is not None, [
                check_adj(row + x, col + y) for x, y in moves
            ])
            for x, y in adjacent:
                if (x, y) not in flashed:
                    cavern_map[x][y] += 1
                    if cavern_map[x][y] > 9:
                        flash(x, y)
            return

        for step in range(100):
            flashed = set()
            for row_i, row in enumerate(cavern_map):
                for col_i in range(len(row)):
                    if (row_i, col_i) not in flashed:
                        cavern_map[row_i][col_i] += 1
                        if cavern_map[row_i][col_i] > 9:
                            flash(row_i, col_i)
            flashes += sum(list(y.count(0) for y in cavern_map))
        print(flashes)


if __name__ == "__main__":
    main()