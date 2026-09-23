#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     23/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2020_day2.txt"
accessMode = "r"
num=[]
letters=[]
password=[]
my_file = open(filename, accessMode)
data=my_file.read()
new_data=data.split("\n")
for line in new_data:
    new_line=line.split(" ")
    num.append(new_line[0])
    letters.append(new_line[1])
    password.append(new_line[2])
count=0
len=len(password)
for i in range(len):
    y=0
    word=password[i]
    numbers=num[i]
    numbers2=numbers.split("-")
    low=int(numbers2[0])-1
    high=int(numbers2[1])-1
    letter=letters[i]
    letter2=letter[0]
    if word[(low)] == letter2:
        y += 1
    if word[(high)] == letter2:
        y += 1
    if y==1:
        count += 1
print(count)

