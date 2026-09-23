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
filename = "advent_2017_day1.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
x=0
z=len(data)
a=int(z/2)

for i in range(z):
    p=i+a
    if i>=a:
        i=-i
    if data[i]==data[i+a]:
        y=int(data[i])
        x += y

    else:

        continue
print (x)