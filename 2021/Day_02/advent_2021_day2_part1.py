#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     02/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    forward=0
    down=0

    with open('advent_2021_day2.txt') as input:
        data = input.read()
        for string in data.split("\n"):
            direction, magnitude = string.split(" ")
            if direction == "forward":
                forward += int(magnitude)
            if direction == "down":
                down += int(magnitude)
            if direction == "up":
                down -= int(magnitude)
        print(forward*down)


if __name__ == '__main__':
    main()
