from random import randint

class Robot:
    def __init__(self):
        self.name = self.unique_name()
        
    def reset(self):
        self.name = self.unique_name()
    
    def unique_name(self) -> str:
        while True:
            new_name=\
            chr(randint(65,90))+\
            chr(randint(65,90))+\
            str(randint(100,999))
            if not hasattr(self, "name") or new_name != self.name:
                return new_name
