import re

encoded = 0
with open('advent_2015_day8.txt') as input:
    data = input.read()
    for line in data.splitlines():
        encoded += len(re.escape(line)) + 2

    characters = len(data.replace('\n',''))

print(encoded-characters)
