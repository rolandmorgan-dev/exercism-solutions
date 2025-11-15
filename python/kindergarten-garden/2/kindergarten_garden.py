plant={"G" : "Grass", "C" : "Clover", "R" : "Radishes", "V" : "Violets"}

class Garden:
    def __init__(self, diagram, students=[]):
        self.diagram, self.students = diagram.splitlines(), sorted(students)
    
    def plants(self, name):
        i = (self.students.index(name))*2 if self.students else (ord(name[0])-65)*2
        return list(map(plant.get, self.diagram[0][i:i+2] + self.diagram[1][i:i+2]))