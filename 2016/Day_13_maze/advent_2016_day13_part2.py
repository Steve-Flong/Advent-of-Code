import random
input = 1364


def check_valid(coords):
    x, y = coords
    if x < 0 or y < 0:
        return False
    wall = (bin(input + (x*x) + (3*x) + (2*x*y) + y + (y*y)).count("1"))
    if wall % 2 ==0:
        return True
    else:
        return False

def maze(ords, steps):
    path = {(1, 1): 0}
    steps = 0
    while steps < 50:

        x, y = ords
        rand = random.choices([(x-1, y), (x+1, y), (x, y+1), (x, y-1)])
        for new in rand:
            if check_valid(new) and new not in path:
                ords = new
                steps += 1
                path[new] = steps
                break
            if check_valid(new) and new in path:
                ords = new
                steps += 1
                break

    return len(path.keys())

max = 0
for x in range(10):
    y = maze((1,1), 0)
    if y > max:

        max = y
print(max)