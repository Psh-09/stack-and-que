class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        new_node.prev = node

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return
        
        node = self.head
        temp = 0
        while temp < index - 1:
            temp += 1
            node = node.next
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        new_node.prev = node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return
        
        node = self.head
        temp = 0
        while temp < index:
            temp += 1
            node = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1

    def print_forward(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def print_backward(self):
        node = self.head
        if node is None:
            return
        while node.next:
            node = node.next
        while node:
            print(node.data)
            node = node.prev
