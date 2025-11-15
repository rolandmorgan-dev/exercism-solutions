class BufferFullException(BufferError):
    def __init__(self, message="Circular buffer is full"):
        super().__init__(message)

class BufferEmptyException(BufferError):
    def __init__(self, message="Circular buffer is empty"):
        super().__init__(message)

class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def read(self):
        if self.size == 0:
            raise BufferEmptyException()
        
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
    
    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException()
        
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
        
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
    
    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = self.tail = self.size = 0
