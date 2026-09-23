import hashlib


def main():
    i = 0
    x = 0
    dict_list = []
    position_list = []
    password = ""
    while x < 8:
        user = ("wtnhxymk" + str(i))
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()
        if h2.startswith("00000"):
            position = h2[5]
            character = h2[6]
            if position.isdigit() and int(position) < 8 and int(position) not in position_list:
                position = int(position)
                dict_list.append({"position": position, "character": character})
                position_list.append(position)
                x += 1
            i += 1
            continue
        i += 1
    dict_list.sort(key=my_func)
    for i in dict_list:
        password += i["character"]
    print(password)


def my_func(e):
    return e["position"]


if __name__ == '__main__':
    main()
