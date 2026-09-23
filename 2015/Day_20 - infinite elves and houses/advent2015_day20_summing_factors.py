import itertools

# factors of input times 10
input = 29000000


def main():
    def factors(n):
        return set(itertools.chain.from_iterable((i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0))

    for house in itertools.count(1):
        list = factors(house)

        if sum(list) * 10 >= input:
            print("house = {}".format(house))
            break


if __name__ == "__main__":
    main()
