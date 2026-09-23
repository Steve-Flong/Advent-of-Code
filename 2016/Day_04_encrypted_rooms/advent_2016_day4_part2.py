

def main():

    def shift(x, y):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        position = alphabet.index(x)
        if y == 0:
            return x
        if y >= len(alphabet)-position:
            new_position = position-(len(alphabet)-y)
            return alphabet[new_position]
        else:
            new_position=position+y
            return alphabet[new_position]

    checksum_list=[]
    sector_id_list=[]
    room_list=[]
    decrypted_list=[]
    with open("advent_2016_day4.txt") as input:
        for room in input.read().splitlines():
            checksum = ""
            sector_id = ""
            room_string = ""
            bracket1 = room.index("[")
            bracket2 = room.index("]")
            for i in range(bracket1+1, bracket2):
                checksum += room[i]
            checksum_list.append(checksum)
            for i in range(bracket1-3, bracket1):
                sector_id += room[i]
            sector_id = int(sector_id)
            sector_id_list.append(sector_id)
            for i in range(0, bracket1-4):
                room_string += room[i]
            room_list.append(room_string)


        for room in room_list:
            decrypted=""
            index=room_list.index(room)
            forward=sector_id_list[index]
            forward=float(forward)
            x=forward/26
            x=int(x)
            move = forward % 26
            move=int(move)

            for letter in room:
                if letter=="-":
                    decrypted += " "
                    continue

                new_letter = shift(letter,move)
                decrypted += new_letter
            decrypted_list.append(decrypted)
            if decrypted=="northpole object storage":
                print (forward)

            print(decrypted)


if __name__ == '__main__':
    main()
