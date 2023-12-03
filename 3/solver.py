file = open("input.txt", "r")

schematic = []

for line in file:
    schematic.append(line)

for line in schematic:
    print(line)


def isSymbol(y, index):
    return schematic[y][index].isdigit() is False and schematic[y][index] != "."


def hasAnAjacentSymbol(y, startIndex, endIndex):
    symbolToLeft = startIndex != 0 and not isSymbol(y, startIndex - 1)
    return symbolToLeft

print(schematic[0])
print(hasAnAjacentSymbol(0, 0, 0))



