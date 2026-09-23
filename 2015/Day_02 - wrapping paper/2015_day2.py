
def main():
    total_surface_area = 0
    total_ribbon = 0
    with open("2015_day2.txt") as input:
        for box in input.read().splitlines():
            dimensions = box.split("x")
            new_box = [int(x) for x in dimensions]
            new_box.sort()

            surface_area = (3*new_box[0] * new_box[1]) + (2*new_box[0]*new_box[2]) + (2*new_box[1]*new_box[2])
            total_surface_area=total_surface_area+surface_area

            ribbon = ((2*new_box[0]) + (2*new_box[1]) + (new_box[0]*new_box[1]*new_box[2]))
            total_ribbon = total_ribbon+ribbon

        print("Total Paper = " + str(total_surface_area) + " Square Feet")
        print("Total Ribbon = " + str(total_ribbon) + " Feet")


if __name__ == '__main__':
    main()













