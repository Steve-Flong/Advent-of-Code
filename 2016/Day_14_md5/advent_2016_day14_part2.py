import hashlib


def main():
    def stretch_hash(index, string, multiple):
        while multiple > 0:
            if multiple == 2017:
                string = string + str(index)
            h = hashlib.md5(string.encode())
            string = h.hexdigest()
            multiple -= 1
        hashes[index] = string
        return string

    hashes = {}
    i = 0
    keys = []
    while len(keys) < 64:
        if i not in hashes:
            hashes[i] = stretch_hash(i, "ahsbgdzn", 2017)
            h2 = hashes[i]
        else:
            h2 = hashes[i]
        for x in range(len(h2) - 2):
            if h2[x] == h2[x + 1] == h2[x + 2]:
                char = h2[x] * 5
                for j in range(1, 1001):
                    k = i + j
                    if k not in hashes:
                        hashes[k] = stretch_hash(k, "ahsbgdzn", 2017)
                    else:
                        h2 = hashes[k]
                    if char in h2:
                        keys.append(i)
                        break
                break
        i += 1
    print(keys[63])


if __name__ == '__main__':
    main()