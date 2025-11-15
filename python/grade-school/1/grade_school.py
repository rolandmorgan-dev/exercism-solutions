class School:
    def __init__(self):
        self.students = {}
        self.student_names = set()
        self.bool_add = []
        
    def add_student(self, name, grade):
        if name in self.student_names:
            self.bool_add.append(False)
        else:
            self.students.setdefault(grade, []).append(name)
            self.student_names.add(name)
            self.bool_add.append(True)
            
    def roster(self):
        return sum({k: sorted(v)\
                    for k,v in sorted(self.students.items())}.values(), [])

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return self.bool_add
