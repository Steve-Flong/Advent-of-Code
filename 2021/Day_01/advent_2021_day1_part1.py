#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     01/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    depths=[]
    total=0
    filename="advent_2021_day1.txt"
    my_file=open(filename,"r")
    data=my_file.read()
    depths=data.split("\n")
    print(len(depths))
    for i in range(len(depths)):
        if 0<i<=len(depths):
            if int(depths[i])>int(depths[i-1]):
                total += 1
    print(total)


if __name__ == '__main__':
    main()
