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
sum=1
b=1                     # number of spaces it moves
x,y=0,0                 # co-ordinates
list=[]
while sum < num:
    list.append((x,y))
    list.append(sum)
    for i in range(1,b+1):
        sum=0
        x += 1
        list.append((x,y))

        if (x-1,y) in list:
            place=list.index((x-1,y))
            sum += list[place+1]

        if (x-1,y+1) in list:
            place=list.index((x-1,y+1))
            sum += list[place+1]

        if (x,y+1) in list:
            place=list.index((x,y+1))
            sum += list[place+1]

        if (x+1,y+1) in list:
            place=list.index((x+1,y+1))
            sum += list[place+1]

        list.append(sum)
        if sum > num:
            print (sum)
            break



    for i in range(1,b+1):
        sum=0
        y += 1
        list.append((x,y))

        if (x,y-1) in list:
            place=list.index((x,y-1))
            sum += list[place+1]

        if (x-1,y-1) in list:
            place=list.index((x-1,y-1))
            sum += list[place+1]

        if (x-1,y) in list:
            place=list.index((x-1,y))
            sum += list[place+1]

        if (x-1,y+1) in list:
            place=list.index((x-1,y+1))
            sum += list[place+1]

        list.append(sum)
        if sum > num:
            print (sum)
            break
    b += 1

    for i in range(1,b+1):
        sum=0
        x -= 1
        list.append((x,y))

        if (x+1,y) in list:
            place=list.index((x+1,y))
            sum += list[place+1]

        if (x+1,y-1) in list:
            place=list.index((x+1,y-1))
            sum += list[place+1]

        if (x,y-1) in list:
            place=list.index((x,y-1))
            sum += list[place+1]

        if (x-1,y-1) in list:
            place=list.index((x-1,y-1))
            sum += list[place+1]

        list.append(sum)

        if sum > num:
            print (sum)
            break


    for i in range(1,b+1):
        y -= 1
        sum=0

        list.append((x,y))

        if (x,y+1) in list:
            place=list.index((x,y+1))
            sum += list[place+1]

        if (x+1,y+1) in list:
            place=list.index((x+1,y+1))
            sum += list[place+1]

        if (x+1,y) in list:
            place=list.index((x+1,y))
            sum += list[place+1]

        if (x+1,y-1) in list:
            place=list.index((x+1,y-1))
            sum += list[place+1]

        list.append(sum)

        if sum > num:
            print (sum)
            break
    b +=1

print ("finished")
