#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     07/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open('advent_2018_day6.txt') as input:
        data=input.read()
        co_ords=data.splitlines()
        new_list=[]
        array=[]
        count=0
        for i in range(360):
            array.append([])
            for j in range(360):
                array[i].append(".")
        for co_ord in co_ords:
            numbers=co_ord.split(", ")
            x=[]
            for number in numbers:
                number=int(number)
                x.append(number)
            new_list.append(x)
        for i in range(len(new_list)):
            array[(new_list[i][0])][(new_list[i][1])]=i

#### calculate the manhatten distance to each main coordinate from each point in array

        for i in range(360):
            for j in range(360):
                manhat_distance=0
                for x in range(len(new_list)):
                    manhat_distance += (abs(new_list[x][0]-i)+abs(new_list[x][1]-j))
                if manhat_distance<10000:
                    count += 1

        print(count)

if __name__ == '__main__':
    main()
