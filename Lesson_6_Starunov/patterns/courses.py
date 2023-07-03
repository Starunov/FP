from pattern_prototype import CoursePrototype
from notifications import Subject


class Course(CoursePrototype, Subject):
    def __init__(self, name: str, category: object):
        super().__init__()
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)
        self.notify()
