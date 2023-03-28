import random

#Klasse für Knoten
class Node:
    def init(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Klasse mit Konstruktor damit man die liste insanzieren kann
class DoublyLinkedList:
    def init(self):
        self.head = None
        self.tail = None

    #Methode um neue Werte am Ende zur List hinzufügen
    def add_to_list(self, data):
        new_node = Node(data) #Knoten
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

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
        while current and current.data != data:
            current = current.next
        if current is None:
            return
        if current.prev is None:
            self.head = current.next
            self.head.prev = None
        elif current.next is None:
            self.tail = current.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev


def main():
    linked_list = DoublyLinkedList()

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

if __name__ == 'main':
    main()