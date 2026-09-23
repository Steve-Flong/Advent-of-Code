

def main():
    array = []
    new_list = []
    count=0
    for i in range(1000):
        array.append([])
        for j in range(1000):
            array[i].append(0)
    with open('advent_2021_day5.txt') as input:
        data=input.read()
        list=data.splitlines()
        for line in list:
            new_lines=line.replace(" -> ",",")
            new_line=new_lines.split(",")
            new_list.append(new_line)
            x1=int(new_line[0])
            x2=int(new_line[2])
            y1=int(new_line[1])
            y2=int(new_line[3])

            if x1==x2 or y1==y2:

                if x1>x2:
                    x1,x2=x2,x1
                if y1>y2:
                    y1,y2=y2,y1

                array[x1][y1] += 1
                if x1==x2:
                    while y1<y2:
                        y1 += 1
                        array[x1][y1]+= 1
                if y1==y2:
                    while x1<x2:
                        x1 += 1
                        array[x1][y1] +=1
                continue

            if x2>x1 and y2>y1:
                    array[x1][y1] +=1
                    while x1<x2:
                        x1 += 1
                        y1 += 1
                        array[x1][y1] +=1
            if x1>x2 and y1>y2:
                    array[x1][y1]+=1
                    while x2<x1:
                        x1-=1
                        y1-=1
                        array[x1][y1] +=1
            if x2>x1 and y1>y2:
                    array[x1][y1]+=1
                    while x1<x2:
                        x1+=1
                        y1-=1
                        array[x1][y1] +=1
            if x1>x2 and y2>y1:
                    array[x1][y1]+=1
                    while y1<y2:
                        y1+=1
                        x1-=1
                        array[x1][y1] +=1
        for j in range(1000):
            for k in range(1000):
                if array[j][k]>1:
                    count +=1
        print(count)









if __name__ == '__main__':
    main()
