
def find_maps(mol, mappings):
    mols = set()

    for mapping in mappings:
        for x in range(len(mol)):
            if mol[x:x + len(mapping[0])] == mapping[0]:
                mols.add(mol[:x] + mapping[1] + mol[x + len(mapping[0]):])
    return mols


with open('advent2015_day19.txt') as input:
    lines = [x.strip().split() for x in input]
    maps = []
    for i in lines[:-2]:
        maps.append((i[0], i[2]))
    molecule = lines[-1][0]
    result = find_maps(molecule, maps)
    print(len(result))

#############################################################part 2 not complete
#     def reduce(mole, count=0):
#
#         if mole == "e":
#             return count
#         for mapping in mappings:
#             for x in range(len(mole)):
#                 if mole[x:x + len(mapping[1])] == mapping[1]:
#                     print(mole[:x] + mole[x + len(mapping[1]):])
#                     return reduce(mole[:x] + mole[x + len(mapping[1]):], count + 1, ) + reduce(mole, count)
#
# with open('advent2015_day19.txt') as input:
#     lines = [x.strip().split() for x in input]
#     mappings = []
#     for i in lines[:-2]:
#         mappings.append((i[0], i[2]))
#     mol = lines[-1][0]
#     print(reduce(mol))