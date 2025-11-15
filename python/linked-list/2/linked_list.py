class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        
        pop_value = self.tail.value
        if self.length > 1:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
        else:
            self.head = self.tail = None
        
        self.length -= 1
        return pop_value
    
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        
        shift_value = self.head.value
        if self.length > 1:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
        else:
            self.head = self.tail = None
        
        self.length -= 1
        return shift_value
    
    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def delete(self, target):
        data = self.head
        while data:
            if data.value == target:
                if data is self.head and data is self.tail:
                    self.head = self.tail = None
                elif data is self.head:
                    self.head = self.head.next
                    self.head.prev.next = None
                    self.head.prev = None
                elif data is self.tail:
                    self.tail = self.tail.prev
                    self.tail.next.prev = None
                    self.tail.next = None
                else:
                    data.next.prev = data.prev
                    data.prev.next = data.next
                    data.prev = None
                    data.next = None
                self.length -= 1
                return
            
            data = data.next
        
        raise ValueError("Value not found")
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        data = self.head
        while data:
            yield data.value
            data = data.next