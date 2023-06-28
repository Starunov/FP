from pattern_prototype import CoursePrototype


class Course(CoursePrototype):
    """Общие аттрибуты и методы для всех курсов"""
    def __init__(self, name: str, category: object):
        self.name = name
        self.category = category
        self.category.courses.append(self)


class Python(Course):
    pass


class Design(Course):
    pass


class Physics(Course):
    pass
