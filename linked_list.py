class EmptyException(Exception):
    pass

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
            return

        if index < 0 or index > self.size:
            raise IndexError('Index out of range')

        if index == 0:
            self.head = Node(data, self.head)
            self.size += 1
            return

        node = self.head
        temp = 0
        while temp < index - 1:
            temp += 1
            node = node.next
        node.next = Node(data, node.next)
        self.size += 1

    def append(self, data):
        self.size += 1

        if self.head is None:
            self.head = Node(data)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        temp = 0
        node = self.head
        while temp < index - 1:
            temp += 1
            node = node.next
        node.next = node.next.next
        self.size -= 1

    def pop(self):
        if self.head is None:
            raise EmptyException('List is empty')
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None
        self.size -= 1

    def popleft(self):
        if self.head is None:
            raise EmptyException('List is empty')
        self.head = self.head.next
        self.size -= 1

    def print(self):
        if self.head is None:
            return
        node = self.head
        while node:
            print(node.data)
            node = node.next
        print("None")