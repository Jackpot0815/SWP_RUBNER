import random

#Klasse für ArrayList
class ArrayList:
    def init(self):
        self.data = []

    #Methode um neue Werte am Ende zur List hinzufügen
    def add_to_list(self, data):
        self.data.append(data)

    #Länge der Liste ausgeben
    def get_length(self):
        return len(self.data)

    #Alle Werte ausgeben
    def print_values(self):
        for data in self.data:
            print(data)

    #Löschen von bestimmten Elementen
    def delete(self, data):
        self.data = [x for x in self.data if x != data]


def main():
    array_list = ArrayList()

    #Die Liste Random befüllen
    for i in range(9):
        array_list.add_to_list("a")
        rndm = random.randint(1, 100)
        array_list.add_to_list(rndm)