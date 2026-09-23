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

print (" name_list :", name_list)
print (" sit_on_discs_list :", sit_on_discs_list)

for lines in sit_on_discs_list:
    if full:
        break
    print (" lines :", lines)
    new_line = lines.split(", ")
    print (" new_line :", new_line)
    for name in new_line:
        print(name)
        if name in name_list:
            full=True
            print("yes")
            continue
        else:
            print("no")
            full=False
            break

x=sit_on_discs_list.index(lines)-1
print (name_list[x])
print (weights[x])






