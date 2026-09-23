import hashlib
import random

doors=[]
def get_hash(string):
    h = hashlib.md5(string.encode())
    return h.hexdigest()


def set_doors(hash, pos, doors):
    open = "bcdef"
    for i in range(4):
        if hash[i] in open:
            doors[i][1] = True
    x, y = pos
    if x == 0:
        doors[0][1] = False
    if x == 3:
        doors[1][1] = False
    if y == 0:
        doors[2][1] = False
    if y == 3:
        doors[3][1] = False
    return doors


def main():
    pos = (0, 0)
    path = "ihgpwlah"
    places_to_visit = []
    already_been =[]
    while pos != (3, 3) and not places_to_visit:
        doors = [["U", False], ["D", False], ["L", False], ["R", False]]
        x,y = pos
        doors = set_doors(get_hash(path), pos, doors)
        open = [x[0] for x in doors if x[1] is True]
        if not open:
            if places_to_visit:
                rewind = places_to_visit.pop(0)
                path = rewind[1]
                pos = rewind[0]
                continue
            else:
                path = path[:-1]
                continue
        if len(open) > 1:
            if (pos, path) not in places_to_visit and (pos, path) not in already_been:
                places_to_visit.append((pos, path))
                already_been.append((pos, path))
        move = random.choice(open)
        if move == "U":
            x -= 1
        elif move == "D":
            x += 1
        elif move == "L":
            y -= 1
        elif move == "R":
            y += 1
        pos = (x, y)
        path += move
    return path


if __name__ == "__main__":
    max = 20
    max_path = 20
    for i in range(100000):
        length = main()
        if len(length) > max:                       # changed from < for part 2
            max_path = length
            max = len(length)
    print(max)
    print(max_path)
