#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     28/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    filename="advent_2018_day5.txt"
    my_file=open(filename,"r")
    data=my_file.read()
    list=[]
    for i in data:
        list.append(i)


    i=0
    while i<len(list)-1 and i>=0:
        if (list[i]).swapcase()==list[i+1]:
            del list[i]
            del list[i]

            if i>0:
                i -= 1
            continue
        i += 1

    print (len(list))


if __name__ == '__main__':
    main()
