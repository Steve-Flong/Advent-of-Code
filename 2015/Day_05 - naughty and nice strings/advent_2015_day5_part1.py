def main():
    with open("advent_2015_day5.txt") as input:
        nice = 0
        for x in input.read().splitlines():
            three_vowels = False
            not_string = False
            double = False
            vowel = 0
            if "ab" not in x and "cd" not in x and "pq" not in x and "xy" not in x:
                not_string = True
            for letter in x:
                if letter in "aeiou":
                    vowel += 1
                if vowel >= 3:
                    three_vowels = True
            length = len(x)
            for i in range(length):
                if i > 0 and x[i] == x[i - 1]:
                    double = True
            if not_string and three_vowels and double:
                nice += 1
        print(nice)


if __name__ == '__main__':
    main()
