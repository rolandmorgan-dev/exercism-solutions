class EmptyListException(Exception):
    def __init__(self, message = "The list is empty."):
        super().__init__(message)

class Node:
    def __init__(self, number, next_song = None):
        self.current_song = number
        self.next_song = next_song
    
    def value(self):
        return self.current_song
    
    def next(self):
        return self.next_song

class LinkedList:
    def __init__(self, numbers=[]):
        self.header = None
        self.size = 0
        for number in numbers: self.push(number)
    
    def head(self):
        if not self.header: raise EmptyListException()
        return self.header
    
    def push(self, value):
        self.header = Node(value, self.header)
        self.size += 1
    
    def pop(self):
        if not self.header: raise EmptyListException()
        popped = self.header.value()
        self.header = self.header.next_song
        self.size -= 1
        return popped
    
    def reversed(self):
        return LinkedList(self)
    
    def __iter__(self):
        playlist = self.header
        while playlist:
            yield playlist.current_song
            playlist = playlist.next_song
    
    def __len__(self):
        return self.size
