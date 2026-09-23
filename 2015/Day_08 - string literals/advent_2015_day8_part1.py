
def main():
    with open('advent_2015_day8.txt', 'rb') as input:
        code = 0
        memory = 0
        for string in input.readlines():
            code += (len(string))
            memory += (len(string[1:-1].decode('unicode_escape')))
        print(code-memory)


if __name__ == '__main__':
    main()
