
def main():
    newer_list = []
    output_list = []
    with open('advent_2021_day8.txt') as input:
        data = input.read().splitlines()
        list = [x.split(" | ") for x in data]
        patterns = [x[0].split() for x in list]
        for x in patterns:
            new_list = []
            for y in x:
                new_patterns = ""
                a = new_patterns.join(sorted(y))
                new_list.append(a)
            newer_list.append(new_list)

        output = [x[1].split() for x in list]
        for x in output:
            new_list = []
            for y in x:
                new_patterns = ""
                a = new_patterns.join(sorted(y))
                new_list.append(a)
            output_list.append(new_list)
        total = 0
        for i in newer_list:
            digits = ["z" for x in range(10)]
            true = int(0)
            outputs = output_list[newer_list.index(i)]
            while true < 4:
                for code in i:
                    if true == 4: break
                    if len(code) == 2 and code not in digits:
                        digits[1] = code
                        true = true + 1
                        continue
                    elif len(code) == 3 and code not in digits:
                        digits[7] = code
                        true = true + 1
                        continue
                    elif len(code) == 4 and code not in digits:
                        digits[4] = code
                        true = true + 1
                        continue
                    elif len(code) == 7 and code not in digits:
                        digits[8] = code
                        true = true + 1
                        continue

            while true < 6:
                if true == 6:
                    break
                for code in i:
                    if true == 6:
                        break
                    count = 0
                    for letter in digits[4]:
                        if letter in code:
                            count += 1

                        if count == 4 and len(code) == 6 and code not in digits and digits[9] == "z":
                            true = true + 1
                            digits[9] = code
                        else:
                            continue
                    count = 0
                    for letter in digits[1]:
                        if letter in code:
                            count += 1

                            if count == 2 and len(code) == 6 and code not in digits and digits[0] == "z":

                                true = true + 1
                                digits[0] = code
                            else:
                                continue
            while true < 7:
                for code in i:
                    if len(code) == 6 and code not in digits and digits[6] == "z":
                        digits[6] = code
                        true = true + 1
                        continue
            while true < 8:
                for code in i:
                    count = 0
                    for letter in digits[1]:
                        if letter in code:
                            count += 1
                            if count == 2 and code not in digits and digits[3] == "z":
                                true += 1
                                digits[3] = code
                            else:
                                continue

                    count = 0
                    for letter in digits[4]:
                        if letter in code:
                            count += 1
                            if count == 3 and code not in digits and digits[5] == "z":
                                digits[5] = code
                                true = true + 1
                            else:
                                continue
                continue
            while true < 10:
                for code in i:
                    if code not in digits:
                        digits[2] = code
                        true += 1
                continue
            number = ""
            for x in outputs:

                if x in digits:
                    y = str(digits.index(x))
                    number += y
            new_number = int(number)
            print(new_number)
            total += new_number

        print(total)


if __name__ == '__main__':
    main()
