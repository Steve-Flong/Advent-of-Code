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
filename = "advent_2017_day7.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
new_list=[]
singles_list=[]
names_list=[]
sit_on_discs_list=[]
name_list=[]
master_list=[]
weights=[]
full=False
list=data.splitlines()
for line in list:                       # create 2 lists of singles and multiples
    if ">" in line:
        new_list.append(line)
    else:
        singles_list.append(line)


for line in new_list:                   # create 2 strings from each multiple
    split_list=line.split("-> ")         # one with names and weight, the other with the other discs which sit on it
    names_list.append(split_list[0])            # add these to their equivalent lists
    sit_on_discs_list.append(split_list[1])     #

for line in names_list:
    steve=line.split()
    name_list.append(steve[0])
    weights.append(steve[1])



for lines in sit_on_discs_list:
    new_line = lines.split(", ")
    for name in new_line:
        master_list.append(name)
for name in name_list:
    if name in master_list:
        continue
    else:
        break

x=name_list.index(name)
print (name)
print (weights[x])

