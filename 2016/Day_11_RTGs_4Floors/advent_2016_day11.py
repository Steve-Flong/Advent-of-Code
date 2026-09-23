import itertools
import random

map = {"lift": 1, "hg": 2, "h": 1, "lg": 3, "l": 1}
#map = {"lift": 1, "ptg": 2, "pt": 1, "rth": 2, "rthg": 2, "stg":1, "st":1, "thg":2, "th":3, "cug":2, "cu":2}
avoid = []
path = [list(map.values())]
map_list = []
temp_map = {}


def main():

    def move_items():
        global map
        global temp_map
        global path
        def valid(maps):
            gens = [x for x in map.keys() if (x != "lift" and "g" in x)]
            for gen in gens:
                temp_gens = gens.copy()
                temp_gens.remove(gen)
                microchip = gen[0:-1]
                for temp_gen in temp_gens:
                    if maps[microchip] == maps[temp_gen] and maps[microchip] != maps[gen]:
                        return False
            if maps["lift"] == 0 or maps["lift"] == 5:
                return False
            return True

        def poss_items_to_move():
            items_on_current_floor = [x for x, y in map.items() if y == map["lift"] and x != "lift"]
            poss_single_moves = [[i] for i in items_on_current_floor]
            if len(items_on_current_floor) > 1:
                poss_double_moves = [[i] for i in itertools.combinations(items_on_current_floor, 2)]
            else:
                poss_double_moves = []
            return poss_single_moves + poss_double_moves

        def vertical_move():
            if map["lift"] == 1:
                return [1]
            elif map["lift"] == 4:
                return [-1]
            else:
                return [1, -1]

        while sum(map.values()) != 20:

            if sum(map.values()) == 20:
                return path
            map_list.append(map)
            moves = vertical_move()
            items = poss_items_to_move()
            random_moves = random.sample(moves, len(moves))
            random_items = random.sample(items, len(items))
            good_move = False
            for lift in range(len(random_items)):
                for move in range(len(random_moves)):
                    if not good_move:
                        temp_map = map.copy()
                        if isinstance(random_items[lift][0], tuple):
                            for x in random_items[lift][0]:
                                temp_map[x] += random_moves[move]
                            temp_map["lift"] += random_moves[move]
                        elif isinstance(random_items[lift][0], str):
                            temp_map[random_items[lift][0]] += random_moves[move]
                            temp_map["lift"] += random_moves[move]
                        if list(temp_map.values()) not in path and valid(temp_map) and list(temp_map.values()) not in avoid:
                            path += [list(temp_map.values())]
                            # print(path)
                            map = temp_map.copy()
                            good_move = True
                            continue
            if not good_move:

                map_list.pop()
                map = map_list[-1]
                map_list.pop()
                print(path)

                temp = path.pop(-1)
                avoid.append(temp)
        return len(path)
    min = 1000
    for i in range(10):
        total = move_items()-1
        if total < min:
            print(path)
            min = total
    print(min)


if __name__ == "__main__":
    main()