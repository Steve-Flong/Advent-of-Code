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
filename = "advent_2017_day5.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
new_list=[]
list=data.splitlines()

for num in list:
    num=int(num)
    new_list.append(num)
steps=0
x=0                             # position in the list
move = new_list[x]
length=len(new_list)            # length of the list

while x+move >=0 and x+move < length:

    new_list[x]=new_list[x]+1
    x += move
    steps +=1
    move=new_list[x]
steps += 1
print(steps)


