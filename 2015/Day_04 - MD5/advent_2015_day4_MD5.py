
import hashlib


def main():
    result = False
    i = 0
    while not result:
        i = str(i)
        user = ("iwrupvqb" + i)
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()

        if h2.startswith("000000"):
            print(i)
            result = True
            break
        i = int(i)
        i += 1


if __name__ == '__main__':
    main()

