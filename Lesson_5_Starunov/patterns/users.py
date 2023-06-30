class User:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @property
    def full_name(self):
        return f'{self.lastname} {self.firstname}'


class Teacher(User):
    pass


class Student(User):
    pass
