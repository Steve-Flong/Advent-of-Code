import numpy as np

INPUT = 21

def find_elf(elves):
    if len(elves) <= 2:
        return elves[0] + 1

    if len(elves) % 2:
        return find_elf(np.roll(elves[::2], 1))
    else:
        return find_elf(elves[::2])

def new_rules(elves):
    n = len(elves)
    if n <= 2:
        return elves[0] + 1
    facing = n // 2
    if n % 2:
        removed = n - (n+1)//3
        new = np.roll(elves, -facing)[1::3]
    else:
        removed = n - n//3
        new = np.roll(elves, -facing)[2::3]
    print(new)
    return new_rules(np.roll(new, facing-removed))

elf_circle = np.arange(INPUT)

print(find_elf(elf_circle))
print(new_rules(elf_circle))