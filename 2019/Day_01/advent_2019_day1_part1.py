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
x=0
for module in list:                         # take the weight of the module
    module=float(module)                    # change to a float
    num=int(module/3)                       # divide by 3 then round down (int)
    fuel=num-2
    x += num
print (x)
