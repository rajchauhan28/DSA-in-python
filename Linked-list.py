from gi.overrides.Gdk import rectangle_union


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertATBegining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next_node = self.head
            self.head = new_node
    def print(self):
        st = ''
        itr = self.head
        while itr.next_node:
            if self.head is None:
                print(None)
            else:
                st = str(self.data) + " - "
                itr = itr.next_node

