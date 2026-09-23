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
filename = "advent_2017_day4.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
word_list=[]
new_string=""
x=0
list=data.splitlines()
valid=False

for line in list:
    words=line.split()
    word_list=[]
    for word in words:
        new_string=""

        new_word=sorted(word)
        for letter in new_word:
            new_string += letter

        word_list.append(new_string)

    for new_words in word_list:
        if word_list.count(new_words)>1:
            valid=False
            break
        else:
            valid=True
    if valid==True:
        x += 1
    else:
        continue

print(x)

