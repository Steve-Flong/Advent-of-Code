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
        count_list=[]
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
                manhat_distance_list=[]
                for x in range(len(new_list)):
                    manhat_distance=abs(new_list[x][0]-i)+abs(new_list[x][1]-j)
                    manhat_distance_list.append({"co-ordinate": x , "number": manhat_distance })
                manhat_distance_list.sort(key=my_func)
### if it is equal lowest then leave as a "."
                if manhat_distance_list[0].get("number")==manhat_distance_list[1].get("number"):
                    continue

                else:
                    array[i][j]=manhat_distance_list[0].get("co-ordinate")

#### check if a coordinate value is on the outer edge of array, if not calculate how many of that value are in the array

        for i in range(len(new_list)):
            outside=False
            for x in range(360):
                for y in range(360):
                    if x==0 or y==0:
                        if array[x][y]==i:
                            outside=True
                            print("True")
                            continue
                    else:continue
            if outside==False:
                count=0
                for a in range(360):
                    for b in range(360):
                        if array[a][b]==i:
                            count += 1
                count_list.append(count)
            continue
        print(count_list)
        count_list.sort()
        print(count_list[-1])




def my_func(e):
    return e["number"]

if __name__ == '__main__':
    main()
