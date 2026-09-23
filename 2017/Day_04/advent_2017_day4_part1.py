#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     18/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2017_day4.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
word_list=[]
x=0
list=data.splitlines()
valid=False

for line in list:
    words=line.split()
    for word in words:
        if words.count(word)>1:
            valid=False
            break
        else:
            valid=True
    if valid==True:
        x += 1
    else:
        continue
print(x)







