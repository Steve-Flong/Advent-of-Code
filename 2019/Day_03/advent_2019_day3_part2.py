#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     16/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2019_day3.txt"
accessMode = "r"
myFile = open(filename, accessMode)
x,y=0,0
location=(x,y)
new_list=[]
count1_list=[]
count2_list=[]
found=False
visited_blocks=[]
crossovers=[]
directions=myFile.read()
list = directions.split("\n")           # list of 2 strings, one for each path
for string in list:
    a=string.split(",")
    new_list.append(a)

for path in new_list:

    x,y=0,0
    location=(x,y)
    if new_list[0]==path:                           # initial path
        count1=-1
        visited_blocks.append(location)
        for com in path:
            number=int(com[1:])
            for i in range(number):
                if com[0]=="R":
                    x += 1
                elif com[0]=="U":
                    y += 1
                elif com[0]=="D":
                    y -= 1
                elif com[0]=="L":
                    x -= 1
                location=(x,y)
                count1 += 1
                visited_blocks.append(location)     # add each location to list
                count1_list.append(count1)          # add the count at that point to another list


        continue

    count2 = 0
    for com in path:                                # path 2 comparing with trail of first path

        number=int(com[1:])
        for i in range(number):
                if com[0]=="R":
                    x += 1
                if com[0]=="U":
                    y += 1
                if com[0]=="D":
                    y -= 1
                if com[0]=="L":
                    x -= 1
                location=(x,y)
                count2 += 1
                if location in visited_blocks:              # if the location is in the list at line 54
                    place=visited_blocks.index(location)    # get the index

                    count1=count1_list[place]               # get the count from the equivalent count1 list

                    crossovers.append(count1+count2)        # add both counts and add to crossover list

                continue
crossovers.sort()                                           # sort the list and print the first i.e. the lowest
print(crossovers[0])











