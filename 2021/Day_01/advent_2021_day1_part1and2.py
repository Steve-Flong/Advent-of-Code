#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     01/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    depths=[]
    trebles=[]
    total=0

    with open('advent_2021_day1.txt') as input:
        data=input.read()
        depths=data.split("\n")
        for i in range(len(depths)-2):
            sum=int(depths[i])+int(depths[i+1])+int(depths[i+2])
            trebles.append(sum)
        for j in range(len(trebles)):
            if j>0:
                if trebles[j]>trebles[j-1]:
                    total += 1
    print(total)

if __name__ == '__main__':
    main()
