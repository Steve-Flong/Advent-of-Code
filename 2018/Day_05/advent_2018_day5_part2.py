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
    length_list=[]
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        new_data=data.replace(i,"")
        up=i.upper()
        newer_data=new_data.replace(up,"")
        length=react_polymer(newer_data)
        length_list.append(length)
    length_list.sort()
    print(length_list[0])



def react_polymer(string):
    list=[]
    for i in string:
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

    return (len(list))


if __name__ == '__main__':
    main()
