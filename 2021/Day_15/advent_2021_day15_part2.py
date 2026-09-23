from heapq import heappop, heappush
from math import inf
from collections import defaultdict
import numpy as np

def main():
    def dijkstras(graph, start):
        distances = {}
        for vertex in graph:
            distances[vertex] = inf
        distances[start] = 0
        vertices_to_explore = [(0, start)]
        while vertices_to_explore:
            current_distance, current_vertex = heappop(vertices_to_explore)
            for neighbor, edge_weight in graph[current_vertex]:
                new_distance = current_distance + edge_weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heappush(vertices_to_explore, (new_distance, neighbor))
        return distances

    def get_value(x, y):
        try:
            if x == -1 or y == -1 or x == 500 or y == 500:
                return None
            return array[x][y]
        except IndexError:
            return None

    with open("advent_2021_day15.txt") as input:
        data = input.read()
        array = np.empty((500, 500), dtype=int)
        small_array = [[int(x) for x in y] for y in data.splitlines()]
        for p in range(100):
            for q in range(100):
                array[p][q] = small_array[p][q]
        for a in range(0, 500, 100):
            for b in range(0, 500, 100):
                for x in range(100):
                    for y in range(100):
                        if a == 0 and b == 0:
                            continue
                        if a == 0:
                            array[x+a][y+b] = (array[x+a][y+b-100] + 1)
                        else:
                            array[x + a][y + b] = (array[x + a - 100][y + b] + 1)
                        if array[x+a][y+b] == 10:
                            array[x + a][y + b] = 1

        graph = defaultdict(list)
        for x in range(len(array)):
            for y in range(len(array[x])):
                adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for j, k in adjacents:
                    dist = get_value(x+j, y+k)
                    if dist:
                        graph[(x, y)].append(((x+j, y+k), dist))

        distances_from_d = dijkstras(graph, (0, 0))
        print(distances_from_d[(499, 499)])


if __name__ == "__main__":
    main()