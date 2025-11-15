class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def push(self, value):
        new_node = Node(value)
        if not self.tail:  # List is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    def pop(self):
        if self._length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._length -= 1
        return value

    def shift(self):
        if self._length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:  # List is empty
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self._length += 1

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current is self.head and current is self.tail:
                    self.head = self.tail = None
                elif current is self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current is self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self._length -= 1
                return
            current = current.next
        raise ValueError("Value not found")

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next