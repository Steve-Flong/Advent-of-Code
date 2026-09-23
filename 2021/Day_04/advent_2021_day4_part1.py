import sys


def main():
    global score
    new_cards = []
    array = []
    cards = {}
    with open('advent_2021_day4.txt') as input:
        data = input.read()
        list = data.split("\n\n")
        numbers = list[0]
        numbers_list = numbers.split(",")
        del list[0]
        for x in range(100):
            array.append([])
            new_list = list[x].split("\n")
            new_card = []
            for i in range(5):
                row = new_list[i].split()
                new_card.append(row)
                array[x].append([])
                for j in range(5):
                    array[x][i].append(0)
            new_cards.append(new_card)

        line_win = False
        for num in numbers_list:
            num = int(num)
            for card in range(100):
                for row in range(5):
                    for column in range(5):
                        if num == int(new_cards[card][row][column]):
                            array[card][row][column] = 1
                            print(num)
                            line_win = test_number(array, new_cards, cards)
                            global score
                            if line_win:

                                if len(cards.keys()) == 100:
                                    print("this should finish")
                                    print("the answer is ", score * num)
                                    print(len(cards.keys()))
                                    print(array[card])
                                    print(new_cards[card])
                                    sys.exit()


def test_number(array, new_cards, cards):
    global score
    line_win = False
    for card in range(100):
        horiz = ""
        vert = ["", "", "", "", ""]
        score = int(0)
        for line in range(5):
            for digit in range(5):
                vert[digit] += str(array[card][line][digit])
                horiz += str(array[card][line][digit])
            if horiz == "11111" and card not in cards:
                cards[card] = 1
                line_win = True
                print("hor")
                for row in range(5):
                    for column in range(5):

                        if array[card][row][column] == 0:
                            value = int(new_cards[card][row][column])
                            score = score + value
                print(cards)

                return True
            else:
                continue

        if "11111" in vert and card not in cards:
            cards[card] = 1
            line_win = True
            print("vert")
            for row in range(5):
                for column in range(5):
                    if array[card][row][column] == 0:
                        value = int(new_cards[card][row][column])
                        score = score + value
            print(cards)

            return True
        else:
            continue


if __name__ == '__main__':
    main()
