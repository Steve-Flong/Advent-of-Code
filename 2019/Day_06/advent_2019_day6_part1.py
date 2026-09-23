from typing import List, Tuple, Dict, Set


def main():
    with open("advent_2019_day6.txt") as input:
        used: List[str] = []
        orbit_dict: Dict[str] = {}
        data = input.read()
        new_list = [x.split(")") for x in data.splitlines()]
# create a dictionary of adjacent orbits
        for orbit in new_list:
            if orbit[0] not in used:
                used.append(orbit[0])
                adjacent_list = [x[1] for x in new_list if x[0] == orbit[0]]
                orbit_dict[(orbit[0])] = adjacent_list
        visited = []
        totals_list = []
        orbits = 0
        print(dfs(visited, orbit_dict, 'COM', orbits, totals_list))


def dfs(visited, orbit_dict, node, orbits, totals_list):
    if node not in visited:
        visited.append(node)
        if node != "COM":
            orbits += 1
            totals_list.append(orbits)
        if node in orbit_dict:
            for neighbour in orbit_dict[node]:
                dfs(visited, orbit_dict, neighbour, orbits, totals_list)

    return sum(totals_list)


if __name__ == '__main__':
    main()
