import random

auswahl = ["s", "r", "p", "sp", "e"]


def computer(alist):
    random.shuffle(alist)
    com = alist[0]
    return com


def game():
    user = input("Deine Wahl: ")
    if user in auswahl:
        com = computer(auswahl)
        print("Computer: " + com)

        # Unentschieden
        if com == user:
            print("Unentschieden!")

        # Siccors/Schere
        elif com == "s" and user == "p":
            print("Du hast verloren!")
        elif com == "s" and user == "r":
            print("Du hast gewonnen!")
        elif com == "s" and user == "sp":
            print("Du hast gewonnen!")
        if com == "s" and user == "e":
            print("Du hast verloren!")

        # Rock/Stein
        elif com == "r" and user == "p":
            print("Du hast gewonnen!")
        elif com == "r" and user == "s":
            print("Du hast verloren!")
        if com == "r" and user == "sp":
            print("Du hast gewonnen!")
        if com == "r" and user == "e":
            print("Du hast verloren!")

        # Paper/Papier
        elif com == "p" and user == "s":
            print("Du hast gewonnen!")
        if com == "p" and user == "r":
            print("Du hast verloren!")
        if com == "p" and user == "sp":
            print("Du hast verloren!")
        if com == "p" and user == "e":
            print("Du hast gewonnen!")

        # Spock
        if com == "sp" and user == "s":
            print("Du hast verloren!")
        if com == "sp" and user == "r":
            print("Du hast verloren!")
        if com == "sp" and user == "p":
            print("Du hast gewonnen!")
        if com == "sp" and user == "e":
            print("Du hast gewonnen!")

        # Echse
        if com == "e" and user == "s":
            print("Du hast gewonnen!")
        if com == "e" and user == "r":
            print("Du hast gewonnen!")
        if com == "e" and user == "p":
            print("Du hast verloren!")
        if com == "e" and user == "sp":
            print("Du hast verloren!")
    else:
        print("Eingabe ist falsch")


def main():
    print("Spiel: Schere-Stein-Papier-Spock-Echse")
    print("Bitte wähle: Schere (s), Stein (r), Papier(p), Spock(sp), Echse (e)")
    game()


if __name__ == '__main__':
    main()
