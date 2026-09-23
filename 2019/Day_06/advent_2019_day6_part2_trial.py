from typing import List, Tuple, Dict, Set


def main():
    with open("advent_2019_day6.txt") as input:
        data = input.read()
        orbits: List = [(orbit[0], orbit[1]) for orbit in [x.split(")") for x in data.splitlines()]]
        print(orbits)
        route_list_you = backwards(orbits, 'YOU')
        route_list_san = backwards(orbits, 'SAN')
        for i in range(len(route_list_you)):
            if route_list_you[i] == route_list_san[i]:
                continue
            else:
                i -= 1
                branch = route_list_you[i]
                leg1 = (len(route_list_you) - 1) - route_list_you.index(branch)
                leg2 = (len(route_list_san) - 1) - route_list_san.index(branch)
                print(leg1+leg2)
                break


def backwards(orbits, node):
    route_list = []
    start = orbits[1].index(node)
    while orbits[start] != "COM":
        route_list.append(orbits[start])
        start = orbits[1].index(orbits[start])
    route_list.reverse()
    return route_list


if __name__ == '__main__':
    main()
