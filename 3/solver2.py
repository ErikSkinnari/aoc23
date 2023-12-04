file = open("input.txt", "r")

schematic = []
partNumbers = []
gearLocations = []
gearRatios = {}


for line in file:
    schematic.append(line)

def isSymbol(y, index):
    return schematic[y][index].isdigit() is False and schematic[y][index] != "."

def rangeContainsSymbol(y, startIndex, endIndex):
    try:
        if startIndex < 0:
            startIndex = 0

        for i in range(startIndex, endIndex):
            if i >= len(schematic[y]) - 1:
                continue
            if isSymbol(y, i) is True:
                return True
        return False
    except:
        print(f"{y}, {startIndex}, {endIndex}")

def hasAnAjacentSymbol(y, startIndex, endIndex):
    symbolToLeft = startIndex != 0 and isSymbol(y, startIndex - 1)
    symbolToRight = endIndex < len(schematic[y]) - 1 and isSymbol(y, endIndex)
    symbolOnTop = y != 0 and rangeContainsSymbol(y - 1, startIndex - 1, endIndex + 1)
    
    symbolOnBottom = False

    if y <= len(schematic) - 1 and rangeContainsSymbol(y + 1, startIndex - 1, endIndex + 1):
        symbolOnBottom = True

    hasAjacentSymbol = symbolToLeft or symbolToRight or symbolOnTop or symbolOnBottom
    return hasAjacentSymbol


def getNumber(string):
    number = ""
    for i in range(len(string)):
        if string[i].isdigit():
            number += string[i]
        else:
            return number


def scanSchematics():
    for lineNumber in range(len(schematic)):
        startIndex = 0
        endIndex = 0
        i = 0

        while i <= (len(schematic[lineNumber]) - 1):
            if schematic[lineNumber][i].isdigit():
                startIndex = i
                number = getNumber(schematic[lineNumber][i:])
                i = i + len(number)
                endIndex = i

                print()
                print("--------")
                
                try:
                    print(schematic[lineNumber-1][startIndex - 1:endIndex + 1])
                except:
                    print(schematic[lineNumber-1][startIndex - 1:endIndex])
                try:
                    print(schematic[lineNumber][startIndex - 1:endIndex + 1])
                except:
                    print(schematic[lineNumber][startIndex - 1:endIndex])
                try:
                    print(schematic[lineNumber+1][startIndex - 1:endIndex + 1])
                except:
                    print()

                if hasAnAjacentSymbol(lineNumber, startIndex, endIndex):
                    print("########")
                    print(f"adding number {number}")
                    print("########")
                    partNumbers.append(int(number))
                print("--------")
                print()
            else:
                i += 1

#scanSchematics()

for lineNumber in range(len(schematic)):
    for charNumber in range(len(schematic[lineNumber])):
        if schematic[lineNumber][charNumber] == "*":
            gearLocations.append({lineNumber, charNumber})

for location in gearLocations:
    print(location)

sum = 0

for number in partNumbers:
    sum += number

#print(sum)
