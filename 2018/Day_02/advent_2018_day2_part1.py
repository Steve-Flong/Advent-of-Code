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
x=0                                     # number of boxes with axactly 2 of any letter
y=0                                     # number of boxes with exactly 3 of any letter

for box in list:

    twice=False                             # flag to set if twice a letter is found
    thrice=False                            # flag to set if 3 times a letter if found
    for letter in box:
        if twice and thrice:
            break
        count=box.count(letter)
        if count==2 and not twice:
            x += 1
            twice=True
            continue
        if count==3 and not thrice:
            y += 1
            thrice=True
            continue
print (x*y)
