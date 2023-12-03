sumOfValidGameIds = 0

def cubeQuantity(color):
    if color == "red":
        return 12
    elif color == "green":
        return 13
    elif color == "blue":
        return 14
    else:
        return 0


file = open("input.txt", "r")

for row in file:
    print(row)
    validGame = True

    gameId = row.split(":")[0].split(" ")[1]
    gameRounds = row.split(":")[1].split(";")
    print(gameId)
    for round in gameRounds:
        print(round)
        for colorAmount in round.split(","):
            qty = colorAmount.strip().split(" ")[0]
            col = colorAmount.strip().split(" ")[1]
            print(qty)
            print(col)
            validColorPick = int(qty) <= cubeQuantity(col)
            if validColorPick is False:
                validGame = False
                continue
    if validGame is True:
        sumOfValidGameIds = sumOfValidGameIds + int(gameId)

print(sumOfValidGameIds)

