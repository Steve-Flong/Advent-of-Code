def main():
    total = 0
    checksum_list = []
    sector_id_list = []
    room_list = []
    with open("advent_2016_day4.txt") as input:
        list = input.read().splitlines()
        for room in list:
            checksum = ""
            sector_id = ""
            room_string = ""
            bracket1 = room.index("[")
            bracket2 = room.index("]")
            for i in range(bracket1 + 1, bracket2):
                checksum += room[i]
            checksum_list.append(checksum)
            for i in range(bracket1 - 3, bracket1):
                sector_id += room[i]
            sector_id = int(sector_id)
            sector_id_list.append(sector_id)
            for i in range(0, bracket1 - 4):
                room_string += room[i]
                new_room_string = room_string.replace("-", "")
            room_list.append(new_room_string)
        dummy = []
        for room in room_list:
            dict_list = []
            for letter in room:
                count = room.count(letter)
                count = int(count)
                dummy.append(count)
                if {"letter": letter, "count": count} in dict_list:
                    continue
                dict_list.append({"letter": letter, "count": count})
            dict_list.sort(key=dict_sort_count)
            v = len(dummy)
            equal = True
            for numbers in range(v):
                if numbers > 0:
                    if dummy[numbers] != dummy[numbers - 1]:
                        equal = False  #
            if equal:
                dict_list.reverse()
            dict_list.reverse()
            letters = ""
            counts = []
            for i in range(len(dict_list)):
                letter = dict_list[i]
                letters += letter["letter"]
                counts.append(letter["count"])
            len2 = len(counts)
            p = 0
            for i in range(len2):
                if i < p:
                    continue
                if i < (len2 - 1):
                    if counts[i] == counts[i + 1]:
                        number = counts.count(counts[i])
                        p = i + number
                        re_order_string = ""
                        re_order_list = []
                        new_string = ""
                        for j in range(number):
                            if (i + j) < (len2):
                                re_order_list.append(letters[i + j])
                                re_order_string += letters[i + j]
                        re_order_list.sort()
                        for q in re_order_list:
                            new_string += q
                        letters = letters.replace(re_order_string, new_string)
            x = room_list.index(room)
            checksum = checksum_list[x]
            if letters.startswith(checksum):
                total += sector_id_list[x]
                continue
        print(total)


def dict_sort_count(e):
    return e["count"]


if __name__ == '__main__':
    main()
