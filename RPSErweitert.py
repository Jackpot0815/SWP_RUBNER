import random
import json

auswahl = ["stein", "papier", "schere", "spock", "echse"]
Speicher = {"spieler": 0, "cpu": 0, "unentschieden": 0, "stein": 0, "papier": 0, "schere": 0, "spock": 0, "echse": 0}
dataFile = {}
gewichtung = [0, 0, 0, 0, 0]


def combine(a, b):
    for i in a:
        dataFile[i] = a[i] + b[i]
    return a


def reset():
    dataFile = {"spieler": 0, "cpu": 0, "unentschieden": 0, "stein": 0, "schere": 0, "papier": 0, "spock": 0, "echse": 0}
    Speicher = dataFile
    gewichtung = [0, 0, 0, 0, 0]
    f = open("Speicher.txt", "w")
    json.dump(dataFile, f)
    f.close()


def update():
    f = open("Speicher.txt", "r")
    save = f.read()
    if save:
        save_json = json.loads(save)
        combine(Speicher, save_json)
    f.close()
    f = open("Speicher.txt", "w")
    json.dump(dataFile, f)
    f.close()


def CPU():
    count = 0
    for i in dataFile:
        if "spieler" not in i and "cpu" not in i and "unentschieden" not in i:
            if dataFile[i] == 0:
                gewichtung[count] = dataFile[i] + 0.01
            else:
                gewichtung[count] = dataFile[i]
            count += 1

    move = gewichtung[len(gewichtung) - 1]
    gewichtung.remove(gewichtung[len(gewichtung) - 1])
    gewichtung.insert(0, move)
    choice = random.choices(auswahl, k=1, weights=gewichtung)
    return choice[0]


def Gewinner(player, cpu):
    spielerWahl = auswahl.index(player)
    cpuWahl = auswahl.index(cpu)
    if (spielerWahl + 2) > 4:
        spielerWahl = spielerWahl - 5
    if (auswahl[spielerWahl + 2] == auswahl[cpuWahl]) or (auswahl[spielerWahl - 1] == auswahl[cpuWahl]):
        gewinner = "Spieler hat gewonnen!"
        Speicher["spieler"] += 1
    elif (auswahl[spielerWahl - 2] == auswahl[cpuWahl]) or (auswahl[spielerWahl + 1] == auswahl[cpuWahl]):
        gewinner = "Computer hat gewonnen!"
        Speicher["cpu"] += 1
    else:
        gewinner = "Unentschieden!"
        Speicher["unentschieden"] += 1
    return gewinner


def game():
    update()
    counter = 1
    print("Spiel: Schere-Stein-Papier-Spock-Echse\n")
    while counter == 1:
        print("Menü, wählen Sie:")
        print(">SPIEL STARTEN (spielen)")
        print(">STATS (stats)")
        print(">SPEICHERN (speichern)")
        print(">STATS NEU SETZEN (neusetzen)")
        print(">VERLASSEN (verlassen)")
        choice = str(input().lower())
        if choice == "spielen":
            status = 1
            while status == 1:
                print("Bitte wähle: Schere, Stein, Papier, Spock, Echse")
                spielerWahl = str(input().lower())
                if auswahl.count(spielerWahl) == 0:
                    print("Wählen Sie bitte eine existierende Form aus!")
                else:
                    Speicher[spielerWahl] += 1
                    cpuWahl = CPU()
                    print("\nDeine Wahl: ", spielerWahl.upper())
                    print("Wahl der CPU: ", cpuWahl.upper())
                    resultat = Gewinner(spielerWahl, cpuWahl)
                    print("\nErgebnis: ", resultat)
                    cont = 1
                    while cont == 1:
                        print("\nNoch einmal spielen? (Ja/Nein)")
                        decision = input().lower()
                        if decision == "ja":
                            status = 1
                            cont = 0
                        elif decision == "nein":
                            cont = 0
                            status = 0
                        else:
                            cont = 1
                            status = 0
            counter = 1
        elif choice == "stats":
            print(dataFile)
            print()
            counter = 1
        elif choice == "speichern":
            update()
            print("Deine Stats wurden geupdated!\n")
            counter = 1
        elif choice == "neusetzen":
            reset()
            print("Deine gespeicherten Daten wurden zurückgesetzt!\n")
            counter = 1
        elif choice == "verlassen":
            counter = 0
        else:
            counter = 1
            print("Wählen Sie bitte eine valide Auswahl!\n")


if __name__ == '__main__':
    update()
    game()
