import itertools


with open('advent2015_day9.txt') as input:
    path = {}
    locations = []
    for line in input:
        newline = line.split()
        city1 = newline[0]
        city2 = newline[2]
        distance = int(newline[4])

        path[city1 + city2] = distance
        path[city2 + city1] = distance

        locations.append(city1)
        locations.append(city2)

    locations = set(locations)  # find unique locations

    shortest_route_length = 999999
    for route in itertools.permutations(locations):
        route_length = 0
        for city1, city2 in zip(route[:-1], route[1:]):
            print(route)
            print(city1, city2)
            route_length += path[city1 + city2]
        if route_length < shortest_route_length:
            shortest_route_length = route_length
    print("Shortest route length:", shortest_route_length)

    longest_route_length = 0
    for route in itertools.permutations(locations):
        route_length = 0
        for city1, city2 in zip(route[:-1], route[1:]):
            route_length += path[city1 + city2]
        if route_length > longest_route_length:
            longest_route_length = route_length
    print("Longest route length:", longest_route_length)