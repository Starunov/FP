from patterns.notifications import Subject
from patterns.pattern_prototype import CoursePrototype
from patterns.unit_of_work import DomainObject


class MetaCategory(type):
    def __init__(cls, cls_name, cls_bases, cls_attrs):
        super().__init__(cls_name, cls_bases, cls_attrs)
        cls.auto_id = 0
        cls.__instance = {}

    def find_category(cls, category_id: int):
        for v in cls.__instance.values():
            if category_id == v.id:
                return v

    def __call__(cls, *args, **kwargs):
        name = args[0] if args else kwargs.get('name')
        if cls.__instance.get(name) is None:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            cls.auto_id += 1
        return cls.__instance.get(name)


class Category(metaclass=MetaCategory):
    def __init__(self, name):
        self.id = Category.auto_id
        self.name = name
        self.courses = []

    def course_count(self):
        return len(self.courses)


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


class User:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @property
    def fullname(self):
        return f'{self.lastname} {self.firstname}'


class Teacher(User):
    pass


class Student(User, DomainObject):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname, age)
        self.courses = []
