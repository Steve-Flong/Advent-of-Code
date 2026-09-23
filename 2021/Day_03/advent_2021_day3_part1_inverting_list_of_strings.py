
def main():
    gamma_rate = ""
    epsilon_rate = ""
    with open('advent_2021_day3.txt') as input:
        list = ["" for x in range(12)]
        for line in input.read().splitlines():
            for digit in range(len(line)):
                list[digit] += (line[digit])
        for string in list:
            if string.count("1") > string.count("0"):
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        dec_gamma = int(gamma_rate, 2)
        dec_eps = int(epsilon_rate, 2)
        print(dec_gamma*dec_eps)


if __name__ == '__main__':
    main()
