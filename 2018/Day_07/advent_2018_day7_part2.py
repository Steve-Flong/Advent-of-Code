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
    alphabet={}
    alphabet2={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
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
                alphabet[letter]=0
    ready_list.sort()
    t=0
    while len(ready_list)>0:

        ready_list.sort()
        print(ready_list)
        step=ready_list[0]
        completed_list.append(step)
        while step in steps_list1:
                x= steps_list1.index(step)
                y= steps_list2[x]
                if steps_list2.count(y)==1 :
                    ready_list.append(y)
                    alphabet[y]=0

                del steps_list1[x]
                del steps_list2[x]


        ready_list.sort()
        for j in ready_list:
            if alphabet[j]==alphabet2[j]+60:
                ready_list.remove(j)
            else: alphabet[j] += 1
        t += 1


    print(t)

if __name__ == '__main__':
    main()

