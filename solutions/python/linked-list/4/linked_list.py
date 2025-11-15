class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._length = 0
    
    def push(self, value):
        self.insert(value, 1)
    
    def unshift(self, value):
        self.insert(value, 0)
    
    def pop(self):
        return self.delete(self.tail.value if self.tail else None, not len(self))
    
    def shift(self):
        return self.delete(self.head.value if self.head else None, not len(self))
    
    def __len__(self):
        return self._length
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def insert(self, value, push):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        elif push:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self._length += 1
    
    def delete(self, value, empty=False):
        if empty: raise IndexError("List is empty")
        node = self.head
        while node:
            if node.value == value:
                if node is self.head and node is self.tail:
                    self.head = self.tail = None
                elif node is self.head:
                    self.head = node.next
                    self.head.prev = None
                elif node is self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                self._length -= 1
                return value
            node = node.next
        raise ValueError("Value not found") #must be "not found" even if empty