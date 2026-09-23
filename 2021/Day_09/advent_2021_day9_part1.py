
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

        result = 0
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
                    result += value + 1
        print(result)


if __name__ == '__main__':
    main()
