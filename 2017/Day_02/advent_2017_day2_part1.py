#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     17/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2017_day2.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
new_list=[]
check_sum=0
line_list=data.splitlines()
for line in line_list:
    new_line1=[]
    new_line=line.split("\t")
    for number in new_line:

        number=int(number)
        new_line1.append(number)
    new_line1.sort()
    x=len(new_line1)
    y=new_line1[(x-1)]
    z=y-(new_line1[0])
    check_sum +=z
    new_list.append(new_line1)


print(check_sum)
