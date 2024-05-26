import re

def load_set(set_file):
    betweenCard = ";"  # delimiter for between cards
    betweenSide = ":"  # delimiter for between sides of the card
    
    f = open(set_file, "r").read()
    cards = re.split(f'{betweenCard}\n|{betweenCard}', f)  # character in quotes decides the split between cards
    result = []
    for card in cards:
        if betweenSide in card:
            result.append(card.split(betweenSide, 1)) 
    return result
