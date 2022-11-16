import random

kartenInHand = []


class Karten(object):
    art = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    farben = ('H', 'P', 'Ka', 'Kr')

    def __init__(self, art, farben):
        if art == 1:
            self.art = 'A'  # Wenn die art der Karte 1 ist ist es eig eine Ass, das wird hier zugewiesen.
        elif art == 13:
            self.art = 'K'  # König
        elif art == 12:
            self.art = 'Q'  # Dame
        elif art == 11:
            self.art = 'J'  # Bube
        else:
            self.art = art
        self.farben = farben


def deck():
    deck_array = []  # leeres array für des kartendeck die man zieht
    for farben in Karten.farben:  # farbe der karten im Deck
        for art in Karten.art:  # art der karten im Deck
            karte = Karten(art, farben)  # neue Karte erstellen
            k = str(karte.art) + " " + karte.farben
            deck_array.append(k)  # und sie zu den karten im Deck hinzufügen
    return austeilen(deck_array)


def austeilen(hand):
    kartenInHand.append(
        random.sample(hand, 5))  # Eine random karte aus dem deck auswählen und zum kurtenInHand hinzufügen
    return kartenInHand  # -> ohne Duplikate -> wegen dem sample


# def check_Pair(hand):
#   l=[]
#  for card in hand:
#     l.append(Karten.art)
# print(l)

if __name__ == '__main__':
    print(deck())
    # check_Pair(deck())
