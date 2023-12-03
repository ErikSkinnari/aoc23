input = open("input.txt", "r")

sum = 0

def getFirstDigitCharacter(string):
    for i in range(len(string) -1):
        if string[i].isdigit():
            return string[i]

def getLastDigitCharacter(string):
    for i in range(len(string) -1, -1, -1):
        if string[i].isdigit():
            return string[i]

for line in input:
    print("\n--")
    print(line)

    digitOne = getFirstDigitCharacter(line)
    digitTwo = getLastDigitCharacter(line)


    print(f"1: {digitOne}")
    print(f"2: {digitTwo}")

    numberAsString = digitOne + digitTwo
    number = int(numberAsString)

    print(numberAsString)
    print(f"number: {number}")

    sum = sum + number

    print(f"sum: {sum}")
    print("--\n")


                
