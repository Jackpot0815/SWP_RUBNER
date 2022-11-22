import random
from collections import Counter

kartenInHand = []

statdc = {
    "Royal Flush": 0,
    "Vierling": 0,
    "Flush": 0,
    "Straße": 0,
    "Drilling": 0,
    "Paar": 0,
    "Highest Card": 0
}


class Karten(object):
    art = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    farben = ('H', 'P', 'Ka', 'Kr')

    def __init__(self, art, farben):
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


def check_pair(hand):
    werteliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kw = k[0]
            werteliste.append(kw)
        counter = Counter(werteliste)
        result = [i for i, j in counter.items() if j == 2]  # checkt wie oft ein element in einem array vorkommen und
    if len(result) == 1:  # speichert das ergebnis in einem dictionary -> das wird durch gefilltert
        return True  # kommt ein element 2 mal vor haben wir ein paar
    else:
        return False


def check_triple(hand):
    werteliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kw = k[0]
            werteliste.append(kw)
        counter = Counter(werteliste)
        result = [i for i, j in counter.items() if j == 3]  # kommt ein element 3 mal vor haben wir einen Drilling
    if len(result) == 1:
        return True
    else:
        return False


def check_quads(hand):
    werteliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kf = k[0]
            werteliste.append(kf)
        counter = Counter(werteliste)
        result = [i for i, j in counter.items() if j == 4]  ##kommt ein element 4 mal vor haben wir four of a kind
    if len(result) == 1:
        return True
    else:
        return False


def check_flush(hand):
    farbliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kw = k[1]  # -> hier split ich und wähle danach die farbe statt die zahle aus
            farbliste.append(kw)
        counter = Counter(farbliste)
        result = [i for i, j in counter.items() if j == 2]  # funkt gleich wie die paare nur diesmal mit farben
    if len(result) == 1:
        return True
    else:
        return False


def check_straight(hand):
    werteliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kw = k[0]
            werteliste.append(kw)
    werteliste.sort()
    counter = Counter(werteliste)
    result = [i for i, j in counter.items() if j == 1]     # ich checke ob auch 0 doppelte vorkommen und wenn ja breche ich sofort ab
    for w in werteliste:                                    # sonst gehe ich die liste durch und schaue ob 5 elemente jeweils 4 größer ist
        if result != 0:                                # als das erste in der Liste
            return False
        elif w == werteliste[w] - 4:
            return True


def check_royalf(hand):
    royal = [9, 10, 11, 12, 13]
    farbliste = []
    for x in range(5):
        for h in hand:
            k = h[x].split()
            kw = k[1]
            farbliste.append(kw)
        counter = Counter(farbliste)
        result = [i for i, j in counter.items() if j == 2]
    if len(result) == 1:
        return result
    else:
        return 0
    if check_flush(hand) > 0:
        if check_straight(hand).nList() == royal:
            return True
    else:
        return False


def main():
    for i in range(1000):                   #Wie oft poker "gespielt" wird
        hand = deck()
        if check_pair(hand) != 0:
            statdc["Paar"] += 1

        elif check_triple(hand) != 0:
            statdc["Drilling"] += 1

        elif check_quads(hand) != 0:
            statdc["Vierling"] += 1

        elif check_straight(hand) != 0:
            statdc["Straße"] += 1

        elif check_flush(hand) != 0:
            statdc["Flush"] += 1

        elif check_royalf(hand) != 0:
            statdc["Royal Flush"] += 1

        else:
            statdc["Highest Card"] += 1
    print(statdc)

if __name__ == '__main__':
    main()
