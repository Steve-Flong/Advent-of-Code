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
    dict_list=[]
    valid=0
    filename="advent_2020_day4.txt"
    my_file=open(filename,"r")
    data=my_file.read()
    new_data=data.rsplit("\n\n")                            # split the data into a list separated by the empty linebreaks
    for i in range(len(new_data)):
        x=new_data[i].replace("\n"," ")
        new_data[i]=x.strip()
    for string in new_data:
        pass_dict = dict((j.strip(), k.strip())             # create a dictionary for each string
             for j, k in (element.split(':')
             for element in string.split(' ')))

        fields=pass_dict.keys()
        if "cid" in fields and len(fields)==8:
            valid += 1
        if "cid" not in fields and len(fields)>=7:
            valid += 1
        continue
    print (valid)
if __name__ == '__main__':
    main()
