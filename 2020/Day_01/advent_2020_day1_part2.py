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
    y = entry+1

    for sub_entry in range(len-y):
        if sum:
            break                          # with a sub loop of entries to compare
        x = sub_entry + 1
        for third in range(len-y-x):              # with a 3rd loop for the 3rd number
            a = third + 1
            if int(list[y])+int(list[x])+int(list[a])==2020:         # set sum=True if a sum of 2020 is found
                sum=True
                print (int(list[x]))
                print (int(list[y]))
                print (int(list[a]))
                print (int(list[x])*int(list[y])*int(list[a]))
                break
            x += 1
        y += 1

