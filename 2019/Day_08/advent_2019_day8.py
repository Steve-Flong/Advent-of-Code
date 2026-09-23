from typing import List, Tuple, Dict


def main():
    with open("advent_2019_day8.txt") as my_input:
        data = my_input.read()
        layers = []

        image = []
        while len(image) < 2:
            row = []
            while len(row) < 3:
                for j in data:
                    row.append(j)
            image.append(row)
        layers.append(image)
        print(layers)







if __name__ == "__main__":
    main()
