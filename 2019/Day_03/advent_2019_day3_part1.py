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
    if new_list[0]==path:
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
                visited_blocks.append(location)
        continue

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
                if location in visited_blocks:
                    distance=abs(x)+abs(y)
                    crossovers.append(distance)
                continue
crossovers.sort()

print (crossovers[0])









