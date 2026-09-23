#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     23/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2020_day1.txt"
accessMode = "r"
my_file = open(filename, accessMode)
data=my_file.read()
list=data.split("\n")
sum=False
len=len(list)
for entry in range(len):                                # loop through each entry
    if sum:
        break
    y = len-entry-1
    x=1
    for sub_entry in range(y):                          # with a sub loop of entries to compare
        x = entry + sub_entry

        if int(list[x])+int(list[entry])==2020:         # set sum=True if a sum of 2020 is found
            sum=True
            print (int(list[x]))
            print (int(list[entry]))
            print (int(list[x])*int(list[entry]))
            break
        x += 1

