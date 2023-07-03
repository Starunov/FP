from factory_method import UserFactory, CourseFactory
from categories import Category


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(user_type, firstname, lastname, age):
        return UserFactory.create(user_type, firstname, lastname, age)

    @staticmethod
    def create_category(name):
        return Category(name)

    @staticmethod
    def find_category_by_id(category_id: int):
        result = Category.find_category(category_id)
        if result is None:
            raise Exception(f'Нет категории с id = {category_id}')
        return result

    @staticmethod
    def create_course(name: str, category: object):
        return CourseFactory.create(name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    def get_student(self, name):
        for item in self.students:
            if item.fullname == name:
                return item
        return None

    # @staticmethod
    # def decode_value(val):
    #     val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
    #     val_decode_str = decodestring(val_b)
    #     return val_decode_str.decode('UTF-8')
