#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     20/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2018_day1.txt"
accessMode = "r"
my_File = open(filename, accessMode)
new_list=[]                         # list of frequencies encountered
x=0                                 # current frequency
data=my_File.read()
list=data.splitlines()
found=False
while not found:

    for num in list:
        num=int(num)
        x += num
        if x in new_list:
            print(x)
            found=True
            break
        else:
            new_list.append(x)








