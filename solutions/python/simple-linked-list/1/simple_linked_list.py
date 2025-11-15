class EmptyListException(Exception):
    def __init__(self, message = "The list is empty."):
        super().__init__(message)

class Node:
    def __init__(self, number):
        self.current_song = number
        self.next_song = None
    
    def value(self):
        return self.current_song
    
    def next(self):
        return self.next_song

class LinkedList:
    def __init__(self, numbers=None):
        self.header = None
        self.size = 0
        if numbers:
            for number in numbers: self.push(number)
    
    def head(self):
        if not self.header: raise EmptyListException()
        return self.header
    
    def push(self, value):
        new_node = Node(value)
        new_node.next_song = self.header
        self.header = new_node
        self.size += 1
    
    def pop(self):
        if not self.header: raise EmptyListException()
        popped = self.header.value()
        self.header = self.header.next_song
        self.size -= 1
        return popped
    
    def reversed(self):
        return reversed([num for num in self.__iter__()])
    
    def __iter__(self):
        playlist = self.header
        while playlist:
            yield playlist.current_song
            playlist = playlist.next_song
    
    def __len__(self):
        return self.size
