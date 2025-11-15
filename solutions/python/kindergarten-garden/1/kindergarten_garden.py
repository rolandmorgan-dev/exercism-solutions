plant={"G" : "Grass", "C" : "Clover", "R" : "Radishes", "V" : "Violets"}

class Garden:
    def __init__(self, diagram, students=[]):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)
    
    def plants(self, name):
        d = self.diagram
        if self.students:
            i = (self.students.index(name))*2
        else:
            i = (ord(name[0])-65)*2
            
        return [plant[d[0][i]],plant[d[0][i+1]],
                plant[d[1][i]],plant[d[1][i+1]]]