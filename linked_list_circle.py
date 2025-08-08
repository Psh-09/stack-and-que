class EmptyException(Exception):
    pass

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range')

        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.size += 1
            return

        if index == 0:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
            self.size += 1
            return

        temp = 0
        prev = self.head
        while temp < index - 1:
            temp += 1
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.size += 1
            return

        node = self.head
        while node.next != self.head:
            node = node.next
        node.next = new_node
        new_node.next = self.head
        self.size += 1

    def delete(self, index):
        if self.head is None or index < 0 or index >= self.size:
            raise IndexError('Index out of range')

        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        if index == 0:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            self.size -= 1
            return

        temp = 0
        prev = self.head
        while temp < index - 1:
            temp += 1
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1

    def pop(self):
        if self.size == 0:
            raise EmptyException('List is empty')

        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        node = self.head
        while node.next.next != self.head:
            node = node.next
        node.next = self.head
        self.size -= 1

    def popleft(self):
        if self.size == 0:
            raise EmptyException('List is empty')

        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        last = self.head
        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        last.next = self.head
        self.size -= 1

    def print(self):
        if self.head is None:
            print("None")
            return
        node = self.head
        for _ in range(self.size):
            print(node.data)
            node = node.next