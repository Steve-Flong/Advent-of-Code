
def main():
    def find_next_allowed(num):
        min = num
        result = True
        while result:
            result = False
            for x in data:

                if int(x[0]) == min:
                    min = int(x[1]) + 1
                    result = True
                    continue
                elif int(x[0]) < min < int(x[1]):
                    min = int(x[1]) + 1
                    result = True
                    continue
        return min

    def find_next_blocked(num):
        min = 4294967295
        result = True
        end = False
        while result:
            result = False
            for x in data:
                if int(x[0]) > num and int(x[0]) < min:
                    min = int(x[0])
                    result = True
                    continue
        if min == 4294967295:
            end = True
        return min, end

    with open("advent_2016_day20.txt") as input:
        data = [x.split("-") for x in input.read().splitlines()]
        end = False
        allowed = 0
        n = 0
        while not end:
            num = find_next_allowed(n)
            if num > 4294967295:
                allowed += 1
                return allowed
            x, end = find_next_blocked(num)
            # print(x,y)
            # print(num)
            allowed += x - num
            n = x
        return allowed


if __name__ == "__main__":
    print(main())