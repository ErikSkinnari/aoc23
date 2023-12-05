file = open("input.txt", "r")

cards = []
cardPager = {}
cardCounter = 0
numbersOfStartCards = 0

for card in file:
    cards.append(card)
    numbersOfStartCards += 1


for row in cards:
    row = row.replace("  ", " ").replace("  ", " ")
    cardNumber = int(row.split(":")[0].split(" ")[1].strip())
    winningNumbers = row.split(":")[1].split("|")[0].strip().split(" ")
    playerNumbers = row.split(":")[1].split("|")[1].strip().split(" ")

    points = 0
    for number in winningNumbers:
        if number in playerNumbers:
            points += 1

    print()
    print(f"CardNumber: {cardNumber}")
    print(f"points: {points}")

    nextCardNumber = cardNumber + 1
    extraCards = 0
    if cardNumber in cardPager:
        extraCards = cardPager[cardNumber]

    print(f"ExtraCards: {extraCards}")
    cardCounter += extraCards + 1
    print(f"nextCardNumber {nextCardNumber}")
    for i in range(nextCardNumber, nextCardNumber + points):
        print(f"i: {i}")
        if i > len(cards):
            priont(f"out of bounds: {i}")
            continue

        if i in cardPager:
            print("pager index exists")
            cardPager[i] = cardPager[i] + extraCards + 1
            print(cardPager[i])
        else:
            print("pager index created")
            cardPager[i] = extraCards + 1
            print(cardPager[i])

    print("------------")
#for p in cardPager.values():
#    print(p)



print(cardCounter)


