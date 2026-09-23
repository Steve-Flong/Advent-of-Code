import json


def count(obj):
    if type(obj) == int:
        return obj
    if type(obj) == list:
        return sum([count(x) for x in obj])
    if type(obj) == dict:
        return sum([count(obj[key]) for key in obj.keys()])
        # part 2 with line 10 removed and 12-14 included
        # if 'red' in obj.values():
        #     return 0
        # return sum([count(obj[key]) for key in obj.keys()])
    return 0


if __name__ == "__main__":
    with open("advent2015_day12.txt") as input:
        new = input.read()
        data = json.loads(new)
    print(count(data))
