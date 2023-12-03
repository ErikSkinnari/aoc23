sumOfValidGameIds = 0
sumOfPowers = 0

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

    minimumReds = 0
    minimumGreens = 0
    minimumBlues = 0

    gameId = row.split(":")[0].split(" ")[1]
    gameRounds = row.split(":")[1].split(";")
    for round in gameRounds:
        print(round)
        for colorAmount in round.split(","):
            qty = int(colorAmount.strip().split(" ")[0])
            col = colorAmount.strip().split(" ")[1]
            print(qty)
            print(col)
            if col == "red" and qty > minimumReds:
                minimumReds = qty
            elif col == "green" and qty > minimumGreens:
                minimumGreens = qty
            elif col == "blue" and qty > minimumBlues:
                minimumBlues = qty
            #validColorPick = int(qty) <= cubeQuantity(col)
            #if validColorPick is False:
             #   validGame = False
              #  continue
    #if validGame is True:
     #   sumOfValidGameIds = sumOfValidGameIds + int(gameId)
    sumOfPowers = sumOfPowers + (minimumReds * minimumGreens * minimumBlues)

print(sumOfPowers)

