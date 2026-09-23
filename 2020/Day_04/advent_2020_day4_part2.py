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

        if "byr"in fields and (len(pass_dict['byr'])!=4 or int(pass_dict['byr'])<1920 or int(pass_dict["byr"])>2002):
            pass_dict.pop("byr")

        if "iyr" in fields and (len(pass_dict["iyr"])!=4 or int(pass_dict["iyr"])<2010 or int(pass_dict["iyr"])>2020):
            pass_dict.pop("iyr")

        if "eyr" in fields and (len(pass_dict["eyr"])!=4 or int(pass_dict["eyr"])<2020 or int(pass_dict["eyr"])>2030):
            pass_dict.pop("eyr")
        if "hgt" in fields:
            if "cm" in pass_dict["hgt"] and (int(pass_dict["hgt"][0:-2])<150 or int(pass_dict["hgt"][0:-2])>193):
                pass_dict.pop("hgt")
            elif "in" in pass_dict["hgt"] and (int(pass_dict["hgt"][0:-2])<59 or int(pass_dict["hgt"][0:-2])>76):
                pass_dict.pop("hgt")
            elif "cm" not in pass_dict["hgt"] and "in" not in pass_dict["hgt"]:
                pass_dict.pop("hgt")

        if "hcl" in fields:
            if (pass_dict["hcl"][0]!="#" or len(pass_dict["hcl"])!=7):
                pass_dict.pop("hcl")
            else:
                test_string="0123456789abcdef"
                for i in range(1,7):
                    if pass_dict["hcl"][i] not in test_string:
                        pass_dict.pop("hcl")

        eyes="amb,blu,brn,gry,grn,hzl,oth"
        if "ecl" in fields and (pass_dict["ecl"] not in eyes or len(pass_dict["ecl"])>3):
            pass_dict.pop("ecl")
        if "pid" in fields and ( pass_dict["pid"].isdigit==False or len(pass_dict["pid"])!=9):
            pass_dict.pop("pid")


        if "byr" in fields and "iyr" in fields and "eyr" in fields and "hgt" in fields and "hcl" in fields and "ecl" in fields and "pid" in fields:
            valid += 1
        continue
    print (valid)
if __name__ == '__main__':
    main()
