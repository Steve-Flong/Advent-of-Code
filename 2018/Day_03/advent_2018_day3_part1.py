#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     20/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

filename = "advent_2018_day3.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
list=data.splitlines()
id=[]                                       # list of ID's
location=[]                                 # list of locations
area=[]                                     # list of areas covered
co_ords=[]
array=[[0]*1000 for i1 in range(1000)]
total=0
for line in list:                           # this splits all the data
    separate=line.split(" @ ")              # into 3 lists of
    id.append(separate[0])                  # ID's
    data=separate[1]                        #
    new_data=data.split(": ")               #

    location.append(new_data[0])            # locations and

    area.append(new_data[1])                # areas

pos=0
for co_ords in location:
    steve=co_ords.split(",")
    x,y = int(steve[0]),int(steve[1])
    new_area = area[pos]
    bob=new_area.split("x")
    a,b = int(bob[0]), int(bob[1])
    for j in range(x,x+a):
        for k in range(y,y+b):
            array[j][k] += 1
    pos += 1

for x in range(1000):
    for y in range(1000):
        if array[x][y] >=2:
            total += 1
print (total)

overlap=False                               # added overlap for part 2
pos=0
for co_ords in location:
    overlap=False
    steve=co_ords.split(",")
    x,y = int(steve[0]),int(steve[1])
    new_area = area[pos]
    bob=new_area.split("x")
    a,b = int(bob[0]), int(bob[1])
    for j in range(x,x+a):
        for k in range(y,y+b):
            if array[j][k] >= 2:

                overlap=True                    # overlap for part 2
    if not overlap:                          #
        print (id[pos])
        break                     #
    pos += 1

















