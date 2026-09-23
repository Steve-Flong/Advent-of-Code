import random


def main():
    path = {(1, 1): 0}
    input = 1364

    def check_valid(coords):
        x, y = coords
        if x < 0 or y < 0:
            return False
        wall = (bin(input + (x*x) + (3*x) + (2*x*y) + y + (y*y)).count("1"))
        if wall % 2 == 0:
            return True
        else:
            return False

    def maze(ords, count):
        while ords != (31,39):
            x, y = ords
            rand = random.choices([(x-1, y), (x+1, y), (x, y+1), (x, y-1)])
            for new in rand:
                if check_valid(new) and new not in path:
                    ords = new
                    count += 1
                    path[new] = count
                    break
                if check_valid(new) and new in path:
                    ords = new
                    count = path[new]
                    break
        return count

    min = 1000
    for x in range(10):
        y = maze((1, 1), 0)
        if y < min:
            min = y
    print(min)


if __name__ == "__main__":
    main()