

def main():
    def my_func(e):
        return e["count"]
    with open("advent_2016_day6.txt") as input:
        list = input.read().splitlines()
        new_list = [[] for _ in range(8)]
        password = ""
        for line in list:
            length = len(line)
            for i in range(length):
                new_list[i] += line[i]
        for new_line in new_list:
            dict_list = []
            letter_list = []

            for letter in new_line:
                if letter in letter_list:
                    continue
                count = new_line.count(letter)
                dict_list.append({"letter": letter, "count": count})
                letter_list.append(letter)
            dict_list.sort(key=my_func)
            password += dict_list[0]["letter"]   # change to index -1 for part 2 for least common character
        print(password)


if __name__ == '__main__':
    main()

