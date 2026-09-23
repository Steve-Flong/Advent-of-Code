#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     22/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


x=0
for num in range(193651,649729):
    two_digits=False
    increase=False
    list=[]
    num=str(num)
    for digit in num:
        digit=int(digit)
        list.append(digit)
    if (list[0]==list[1] and list[1]!=list[2]) or (list[1]==list[2] and list[1]!=list[0] and list[2]!=list[3]) or (list[2]==list[3] and list[1]!=list[2] and list[4]!=list[3])\
    or (list[3]==list[4] and list[3]!=list[2] and list[4]!=list[5]) or (list[5]==list[4] and (list[3]!=list[4])):
        two_digits=True
    if list[0]<=list[1] and list[1]<=list[2] and list[2]<=list[3] and list[3]<=list[4] and list[4]<=list[5]:
        increase=True
    if two_digits and increase:
        x += 1
    continue
print(x)


