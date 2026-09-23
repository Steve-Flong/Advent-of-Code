
def dragon_curve(string, disk):
    a = string
    b = a
    reverse = b[::-1]
    new_reverse = ""
    for digit in reverse:
        if digit == "0":
            new_reverse += "1"
        else:
            new_reverse += "0"
    result = a + "0" + new_reverse
    if len(result) < disk:
        return dragon_curve(result, disk)
    else:
        return result


def create_checksum(str, disk):
    new_string = ""
    if len(str) > disk:
        useful_data = str[:disk]
    else:
        useful_data = str
    for i in range(0, len(useful_data),2):
        if useful_data[i] == useful_data[i+1]:
            new_string += "1"
        else:
            new_string += "0"
    if len(new_string) % 2 == 0:
        return create_checksum(new_string, disk)
    else:
        return new_string


if __name__ == "__main__":
    print(create_checksum(dragon_curve("00101000101111010", 35651584), 35651584))