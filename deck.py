


HEARTS = "H"
DIAMONDS = "D"
CLUBS = "C"
SPADES = "S"

def getcards():
    suits = [HEARTS, DIAMONDS, CLUBS, SPADES]
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank,suit))

    return deck

