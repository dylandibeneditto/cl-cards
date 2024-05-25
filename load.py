def load_set(set):
    betweenCard = ";\n"  # delimiter for between cards
    betweenSide = ":"  # delimiter for between sides of the card
    
    f = open(set, "r").read()
    cards = f.split(betweenCard)  # character in quotes decides the split between cards
    result = []
    for card in cards:
        if betweenSide in card:
            result.append(card.split(betweenSide, 1)) 
            print(result)
    return result
