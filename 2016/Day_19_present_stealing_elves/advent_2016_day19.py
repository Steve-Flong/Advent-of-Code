def main():
    elves = [[i, 1] for i in range(400000)]
    i = 0
    while len(elves) > 1:
        print(len(elves))
        if i == len(elves)-1:
            elves[i][1] += elves[0][1]
            elves.pop(0)
            i = 0
            continue
        if i == len(elves)-2:
            elves[i][1] += elves[-1][1]
            elves.pop(-1)
            i = 0
            continue
        else:
            elves[i][1] += elves[i+1][1]
            elves.pop(i+1)
            i += 1
    print(elves[0][0]+1)


if __name__ == "__main__":
    main()
