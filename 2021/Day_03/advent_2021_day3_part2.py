

def main():

    with open('advent_2021_day3.txt') as input:
        data2 = input.read().splitlines()
        CO2_answer = ox_gen(data2, False)
        O2_answer = ox_gen(data2, True)
        print(CO2_answer*O2_answer)

def ox_gen(data2,oxy):
    x=0
    z=0
    y=0
    new_data=[]
    while z<12:
        list=[]
        if z>0:
            data2=new_data.copy()
        for line in range(len(data2)):
            list.append(data2[line][x])
        ones=list.count("1")
        zeros=list.count("0")
        new_data.clear()
        if (ones>zeros and oxy) or (ones<zeros and not oxy) or (ones==zeros and oxy):
            for y in range(len(data2)):
                if data2[y][z]=="1":
                    new_data.append(data2[y])
        elif (ones<zeros and oxy) or (ones>zeros and oxy==False) or (ones==zeros and not oxy):
            for y in range(len(data2)):
                if data2[y][z]=="0":
                    new_data.append(data2[y])
        z += 1
        x += 1
        if len(new_data)==1:
            break
    return int(new_data[0],2)


if __name__ == '__main__':
    main()
