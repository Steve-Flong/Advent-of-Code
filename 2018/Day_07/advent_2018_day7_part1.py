#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     30/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    instructions=[]
    steps_list1=[]
    steps_list2=[]

    ready_list=[]

    completed_list=[]
    with open('advent_2018_day7.txt') as input:
        for line in input:
            instructions.append(line.split())
    for line in instructions:
        steps_list1.append(line[1])
        steps_list2.append(line[7])

    for letter in steps_list1:
        if letter not in steps_list2:
            if letter not in ready_list:
                ready_list.append(letter)
    ready_list.sort()

    while len(ready_list)>0:
        ready_list.sort()
        i=0
        step=ready_list[i]
        completed_list.append(step)
        while step in steps_list1:
                x= steps_list1.index(step)
                y= steps_list2[x]
                if steps_list2.count(y)==1:
                    ready_list.append(y)
                del steps_list1[x]
                del steps_list2[x]

        ready_list.remove(step)
        ready_list.sort()
        print(ready_list)




    print(completed_list)

if __name__ == '__main__':
    main()

