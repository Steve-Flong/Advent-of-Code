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
filename = "advent_2018_day2.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
list=data.splitlines()
x=0
correct=0
final=""
number_of_boxes = len(list)

for box in list:
    if correct==25:
        break
    correct=0
    y=1

    x=list.index(box)
    a=number_of_boxes-x-1                       # sets "a" the number of loops ( comparisons)  for each box
    for i in range(a):
        correct=0
        compare=list[x+y]                       # sets the comparison box
        t=0
        for letter in box:

            if box[t]==compare[t]:
                correct += 1
            t += 1
        if correct==25:
            print (box)
            print (compare)


            break
        y += 1

