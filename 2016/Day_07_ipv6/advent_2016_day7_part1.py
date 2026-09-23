
def main():
    with open("advent_2016_day7.txt") as input:
        supports_tls = 0
        for line in input.read().splitlines():
            outside = True
            outside_abba = False
            inside_abba = False
            i = 0
            while i < len(line)-4:
                if line[i] == line[i+3] and line[i+1] == line[i+2] and outside:
                    outside_abba = True
                if line[i] == line[i+3] and line[i+1] == line[i+2] and not outside:
                    inside_abba = True
                if line[i] == "[":
                    outside = False
                    i += 1
                    continue
                if line[i] == "]":
                    outside = True
                    i += 1
                    continue
                i += 1
            if outside_abba and not inside_abba:
                supports_tls += 1
        print(supports_tls)


if __name__ == '__main__':
    main()
