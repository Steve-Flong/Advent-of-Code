#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     24/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def main():
    new_list=[]
    rules=[]
    messages=[]
    new_rules=[]
    valid1=False
    valid2=False
    correct=False
    filename = "advent_2020_day19.txt"
    accessMode = "r"
    my_file = open(filename, accessMode)
    data=my_file.read()
    list=data.split("\n")

    for i in list:                  # this loop splitting messages from rules
        if i.isalpha():             # and putting them into 2 lists
            messages.append(i)
        elif i=="":
            continue
        else:                       # create an empty list for the number of rules
            new_list.append('0')
            rules.append('0')


    for line in list:               # every line beginnning with a number is
        new_line=line.split(":")    # sorted into order of rule number
        number=new_line[0]
        if number.isnumeric():
            num=int(number)
            spaceless=new_line[1]
            spaceless1=spaceless.lstrip()
            spaceless2=spaceless1.split(" ")
            rules[num]=spaceless2





# create 3 functions....
# one to carry out the AND function
# one to carry out the OR function
# single function

def AND(x,y):

    x=int(x)
    y=int(y)
    rule1=rules[x]
    rule2=rules[y]
    if rule1==letter_to_be_validated:
        valid1=True

    elif "|" in rule1:
        valid1=OR(rule1[0],rule1[1],rule1[3],rule1[4])
    elif "|" not in rule1:
        valid1=AND(rule1[0],rule1[1])


    if rule2==letter_to_be_validated:
        valid2=True
    elif "|" in rule2:
        if len(rule2)==5:
            valid2=OR(rule2[0],rule2[1],rule2[3],rule2[4])
        if len(rule2)==3:
            valid2=OR(rule2[0],rule2[3])
    elif "|" not in rule1:
        valid=AND(rule2[0],rule2[1])
    if valid1 and valid2:
        return True

def OR(a,b,c,d):
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    and_return3=AND(a,b)
    and_return4=AND(c,d)
    if and_return3 or and_return4:
        return True

def single(x):
    x=int(x)
    rule=rules[x]




if __name__ == '__main__':
    main()
