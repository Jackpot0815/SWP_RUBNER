import random

#Klasse für Knoten
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Klasse mit Konstruktor damit man die liste insanzieren kann
class LinkedList:
    def __init__(self):
        self.head = None

    #Methode um neue Werte am Ende zur List hinzufügen
    def add_to_list(self, data):
        new_node = Node(data) #Knoten
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    #Länge der Liste ausgeben
    def get_length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1 #Counter zählt pro node hoch (Länge
            current_node = current_node.next
        return count

    #Alle Werte ausgeben
    def print_values(self):
        current_node = self.head #Knoten
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    #Löschen von bestimmten Elementen
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next


def main():
    linked_list = LinkedList()

    #Die Liste Random befüllen
    for i in range(9):
        linked_list.add_to_list("a")
        rndm = random.randint(1, 100)
        linked_list.add_to_list(rndm)
        linked_list.add_to_list("b")

    #Ausgabe:
    print("Länge der Datenstruktur: ", linked_list.get_length())
    print("Elemente in der Datenstruktur: ")
    linked_list.print_values()

    #Delete
    print("Delete: ")
    linked_list.delete("a")
    linked_list.print_values()

if __name__ == '__main__':
    main()

