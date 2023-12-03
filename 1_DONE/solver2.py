input = open("input.txt", "r")

sum = 0

def stringToInteger(string):
    if string == "one":
        return 1
    elif string == "two":
        return 2
    elif string == "three":
        return 3
    elif string == "four":
        return 4
    elif string == "five":
        return 5
    elif string == "six":
        return 6
    elif string == "seven":
        return 7
    elif string == "eight":
        return 8
    elif string == "nine":
        return 9
    elif string == "zero":
        return 0
    else:
        return -1


def getFirstNumber(string):
    for i in range(len(string) -1):
        number = getNumber(string[i:])
        if number != -1:
            return number

def getLastNumber(string):
    for i in range(len(string) -1, -1, -1):
        number = getNumber(string[i:])
        if number != -1:
            return number

def getNumber(string):
    print(string)

    if string[0].isdigit():
        return string[0]
    elif len(string) >= 3:
        three = string[:3]
        possibleNumber = stringToInteger(three)
        if possibleNumber != -1:
            return possibleNumber
        if len(string) >= 4:
            possibleNumber = stringToInteger(string[:4])
            if possibleNumber != -1:
                return possibleNumber
        if len(string) >= 5:
            possibleNumber = stringToInteger(string[:5])
            if possibleNumber != -1:
                return possibleNumber
    return -1


for line in input:
    print(line)
    num1 = str(getFirstNumber(line))
    num2 = str(getLastNumber(line))
    numberAsString = num1 + num2
    number = int(numberAsString)

    #print(numberAsString)
    #print(f"number: {number}")

    sum = sum + number

    print(f"sum: {sum}")
    #print("--\n")


                
