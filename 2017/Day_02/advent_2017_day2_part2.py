#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     17/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2017_day2.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
new_list=[]
check_sum=0
line_list=data.splitlines()
for line in line_list:
    new_line1=[]
    new_line=line.split("\t")
    for number in new_line:

        number=int(number)
        new_line1.append(number)
    new_line1.sort()
    new_line1.reverse()
    result=False


    y=len(new_line1)

    for i in range(y):
        if result:
            i -= 1

            break

        a=i+1
        while a < y:
            if new_line1[i] % new_line1[a] == 0:
                result=True
                break
            else:
                a += 1
        continue


    check_sum += new_line1[i]/new_line1[a]
print (check_sum)










