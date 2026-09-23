#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     21/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2019_day2.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
list=[]
old_list=data.split(",")
for i in old_list:
    i=int(i)
    list.append(i)

loops=int((len(list)/4)+1)                   # set the number of loops from length of the instructions/4
pos=0
for loop in range(loops):
    store_position=list[pos+3]
    var1=list[list[pos+1]]
    var2=list[list[pos+2]]


    if list[pos]==1:
        list[store_position]=(var1 + var2)
    if list[pos]==2:
        list[store_position]=(var1*var2)
    pos += 4
    if list[pos]==99:
        break
    else:
        continue


print(list[0])
