#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     21/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2019_day1.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
list=data.splitlines()
total=0

for module in list:
    x=0
    negative=False
    while not negative:             # create a continuous loop until the extra fuel is zero

        module=float(module)
        num=int(module/3)
        current_fuel=num-2
        if current_fuel <=0:
            negative=True
            continue
        x += current_fuel
        module=current_fuel

    total += x
print (total)
