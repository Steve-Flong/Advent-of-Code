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

num=input("What is the number? ")
num=int(num)
a=1                     # the data number as it increases
b=1                     # number of spaces it moves
x,y=0,0                 # co-ordinates

while a < num:

    for i in range(1,b+1):
        x += 1
        a += 1
        if a == num:
            print (abs(x)+abs(y))
            break



    for i in range(1,b+1):
        y += 1
        a += 1
        if a == num:
            (abs(x)+abs(y))
            break
    b += 1

    for i in range(1,b+1):
        x -= 1
        a += 1
        if a == num:
            (abs(x)+abs(y))
            break


    for i in range(1,b+1):
        y -= 1
        a += 1
        if a == num:
            print (x,y)
            break
    b +=1

print ("finished")

