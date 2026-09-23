from typing import List, Tuple, Dict, Set


def main():
    with open("advent_2019_day6.txt") as input:
        data = input.read()
        orbits: List[str] = []
        orbiters: List[str] = []
        for orbit in [x.split(")") for x in data.splitlines()]:
            orbits.append(orbit[0])
            orbiters.append(orbit[1])
        route_list_you = backwards(orbits, orbiters, 'YOU')
        route_list_san = backwards(orbits, orbiters, 'SAN')
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


def backwards(orbits, orbiters, node):
    route_list = []
    start = orbiters.index(node)
    while orbits[start] != "COM":
        route_list.append(orbits[start])
        start = orbiters.index(orbits[start])
    route_list.reverse()
    return route_list


if __name__ == '__main__':
    main()
