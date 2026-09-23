

def main():
    with open("advent_2016_day7.txt") as input:
        supports_ssl = 0
        for line in input.read().splitlines():
            outside = True
            outside_aba = False
            inside_bab = False
            aba_list = []
            bab_list = []
            i = 0
            x = len(line)
            while i < x-2:
                aba = ""
                bab = ""
                if line[i] == line[i+2] and line[i+1] != line[i] and outside:
                    aba += line[i] + line[i+1] + line[i+2]
                    if "[" not in aba and "]" not in aba:
                        aba_list.append(aba)
                    if aba in bab_list:
                        outside_aba = True
                if line[i] == line[i+2] and line[i+1] != line[i] and not outside:
                    bab += line[i+1] + line[i] + line[i+1]
                    if "[" not in bab and "]" not in bab:
                        bab_list.append(bab)
                    if bab in aba_list:
                        inside_bab = True
                if line[i] == "[":
                    outside = False
                    i += 1
                    continue
                if line[i] == "]":
                    outside = True
                    i += 1
                    continue
                i += 1
            if inside_bab | outside_aba:
                supports_ssl += 1
        print(supports_ssl)


if __name__ == '__main__':
    main()
