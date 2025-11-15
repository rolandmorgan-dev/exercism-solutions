class Clock:
    def __init__(self, hour, minute):
        self.hour = (minute // 60 + hour) % 24
        self.minute = minute % 60
    
    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"
    
    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"
    
    def __add__(self, minutes):
        self.hour = ((self.minute + minutes) // 60 + self.hour) % 24
        self.minute = (self.minute + minutes) % 60
        return str(Clock(self.hour, self.minute))
    
    def __sub__(self, minutes):
        self.hour = ((self.minute - minutes) // 60 + self.hour) % 24
        self.minute = (self.minute - minutes) % 60
        return str(Clock(self.hour, self.minute))
    
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
