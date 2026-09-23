decomp = ""


with open("advent_2016_day9.txt") as input:
    full = "".join(i for i in input.read().splitlines())
    i = 0
    pointer_1 = 0
    pointer_2 = 0
    while i < len(full):
        if full[i] == "(":
            pointer_1 = i + 1
            while full[i] != ")":
                i += 1
            comp_nums = full[pointer_1:i].split("x")
            pointer_1 = i + 1
            pointer_2 = pointer_1+int(comp_nums[0])
            try:
                decomp += full[pointer_1: pointer_2] * int(comp_nums[1])
            except IndexError:
                decomp += full[pointer_1:] * int(comp_nums[1])
                print(len(full))
                break
            i = pointer_2
            continue
        else:
            pointer_1 = i
            if pointer_1 == len(full)-1:
                decomp += full[pointer_1]
                break
            while full[i] != "(" and i < len(full)-1:
                i += 1
            try:
                decomp += full[pointer_1: i]
            except IndexError:
                decomp += full[pointer_1:]
    #print(decomp)
    print(len(decomp))


