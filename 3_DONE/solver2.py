file = open("input.txt", "r")

schematic = []
partNumbers = []
gearLocations = []
gearRatios = {}


for line in file:
    schematic.append(line)

def isSymbol(y, index):
    return schematic[y][index].isdigit() is False and schematic[y][index] != "."

def isGear(y, index, number):
    isGearLocation = isSymbol(y, index) is True and schematic[y][index] == "*"
    if isGearLocation == True:
        if (y, index) in gearRatios:
            gearRatios[(y, index)].append(number)
        else: 
            gearRatios[(y, index)] = [number]

        
def rangeContainsGear(y, startIndex, endIndex, number):
    try:
        if startIndex < 0:
            startIndex = 0

        for i in range(startIndex, endIndex):
            if i >= len(schematic[y]) - 1:
                continue
            if isGear(y, i, number) is True:
                return True
        return False
    except:
        print(f"{y}, {startIndex}, {endIndex}")

def hasAnAjacentSymbol(y, startIndex, endIndex, number):
    symbolToLeft = startIndex != 0 and isGear(y, startIndex - 1, number)
    symbolToRight = endIndex < len(schematic[y]) - 1 and isGear(y, endIndex, number)
    symbolOnTop = y != 0 and rangeContainsGear(y - 1, startIndex - 1, endIndex + 1, number)
    
    symbolOnBottom = False

    if y <= len(schematic) - 1 and rangeContainsGear(y + 1, startIndex - 1, endIndex + 1, number):
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

                if hasAnAjacentSymbol(lineNumber, startIndex, endIndex, number):
                    print("########")
                    print(f"adding number {number}")
                    print("########")
                    partNumbers.append(int(number))
                print("--------")
                print()
            else:
                i += 1


for lineNumber in range(len(schematic)):
    for charNumber in range(len(schematic[lineNumber])):
        if schematic[lineNumber][charNumber] == "*":
            gearLocations.append({lineNumber, charNumber})

for location in gearLocations:
    print(location)

scanSchematics()

sum = 0

for ratio in gearRatios.values():
    if len(ratio) == 2:
        print(ratio)
        sum += int(ratio[0]) * int(ratio[1])


#for number in partNumbers:
#    sum += number

print(sum)
