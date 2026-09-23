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


def func(a,j):                                  # function arguments determine right and down of slope

    filename = "advent_2020_day3.txt"
    accessMode = "r"
    my_file = open(filename, accessMode)
    data=my_file.read()
    lines=data.split("\n")
    width=float(len(lines[0]))
    height=float(len(lines))
    list=[]
    a=int(a)
    j=int(j)
    b=a
    no_of_widths=int((height*a)/(j*width))+1        # this decides how many repeats of the grid are required as
                                                    # determined by steps right and down, and size of current grid
    tree=0
    for x in lines:
        y=x*no_of_widths
        list.append(y)                          # create the full map
    count=0
    for x in list:                              # for each line add a to horizontal and check for #

        if count>0 and count % j==0:            # j is the number of rows it jumps each time
            if x[a]=="#":
                tree += 1
            a += b
        count += 1
    return tree


tree=0
num=input ("How many right? ")
down=input ("How many down? ")
result = func(num, down)
print(result)




