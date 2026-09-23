input = "3113322113"


def convert_with_one_pointer(x):
    new_string = ""
    count = 1
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            count += 1
        else:
            new_string += str(count) + str(x[i-1])
            count = 1
        if i == len(x)-1:
            new_string += str(count) + x[i]
    return new_string


def convert_with_2_pointers(x):
    list = []
    j = 0
    i = 0
    while j < len(x)-1:
        while x[j] == x[i] and j < len(x)-1:
            j += 1
        if j != len(x)-1:
            if x[j] != x[i]:
                list.append(x[i:j])
                i = j
        if j == len(x)-1:
            if x[j] != x[i]:
                list.append(x[i:j])
                list.append(x[j])
            else:
                list.append(x[i:])
    new_string = ""
    for x in list:
        new_string += str(len(x)) + str(x[0])
    return new_string


if __name__ == "__main__":
    for k in range(50):
        result = convert_with_2_pointers(input)
        input = result
    print(len(input))