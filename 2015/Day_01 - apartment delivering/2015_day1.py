
def main():
    with open("2015_day1.txt") as my_input:
        count = 0
        position = 0
        for x in my_input.read():
            if x == "(":
                count += 1
            else:
                count -= 1
            position += 1
            if count == -1:
                print(position)
                break
            else:
                continue


if __name__ == "__main__":
    main()
    