#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     19/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2017_day6.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()

list=data.split("\t")
length=len(list)
new_list=[]
list_of_banks=[]
for num in list:
    num=int(num)
    new_list.append(num)
new_tuple=tuple(new_list)
list_of_banks.append(new_tuple)          # create a list to search for infinite loop
infinite=False
y=0                                     # set number of redistributions


while not infinite:

    ord_list=new_list.copy()
    ord_list.sort()

    high=ord_list[-1]                       # this is the number which needs redistributing
    start=new_list.index(high)              # this is the index which needs redistributing
    new_list[start]=0                       # set the contents of start index to zero
    if start==length-1:
        x=0
    else:
        x = start + 1                           # set first index of redistribution
    for step in range(high):
        new_list[x] += 1
        if x==length-1:
            x=0
        else:
            x += 1
    y += 1

    new_tuple=tuple(new_list)
    if new_tuple in list_of_banks:
        infinite=True
        continue
    else:

        list_of_banks.append(new_tuple)

        continue

print(y)



