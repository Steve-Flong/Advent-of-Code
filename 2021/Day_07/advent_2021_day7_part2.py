

def main():
    with open('advent_2021_day7.txt') as input:
        data = input.read()
        list = data.split(",")
        list.sort()
        max = int(list[-1])
        results_list = []
        for i in range(max):
            total = 0
            for j in list:
                total += 0.5*(abs(int(j)-i))*(abs((int(j)-i))+1)
            results_list.append(total)
        copy = results_list.copy()
        copy.sort()
        print(results_list.index(copy[0]))
        print(copy[0])


if __name__ == '__main__':
    main()
