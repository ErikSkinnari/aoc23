file = open("input.txt", "r")

points = 0
cards = []

cardPager = {}
cardCounter = 1


for card in file:
    cards.append(card)


for row in file:
    row = row.replace("  ", " ").replace("  ", " ")
    #print(row)

    cardNumber = row.split(":")[0].split(" ")[1]
    winningNumbers = row.split(":")[1].split("|")[0].strip().split(" ")
    playerNumbers = row.split(":")[1].split("|")[1].strip().split(" ")
    #print(cardNumber)
    #print(winningNumbers)
    #print(playerNumbers)

    multiplier = 0
    for number in winningNumbers:
        if number in playerNumbers:
            #print(f"{number} is in {playerNumbers}")
            multiplier += 1

    print(multiplier)

    pointsToAdd = 0
    if multiplier == 1:
        pointsToAdd = 1
    elif multiplier > 1:
        pointsToAdd = 2 ** (multiplier - 1)
    print(f"points to add: {pointsToAdd}")
    points += pointsToAdd

print(points)


