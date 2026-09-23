
def main():
    row = 1
    col = 1
    row_pointer = 1

    num = float(20151125)
    while not (row == 3010 and col == 3019):
        num = (num * 252533) % 33554393
        if row == 1:
            row_pointer += 1
            row = row_pointer
            col = 1
        else:
            col += 1
            row -= 1
    print(num)


if __name__ == "__main__":
    main()
