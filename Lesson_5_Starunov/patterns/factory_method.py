from courses import Python, Physics, Design
from users import Student, Teacher


class CourseFactory:

    @staticmethod
    def create(name: str, category: object):
        return {
            'python': Python,
            'design': Design,
            'physics': Physics,
        }[name](name, category)


class UserFactory:
    @staticmethod
    def create(user_type):
        return {
            'student': Student,
            'teacher': Teacher,
        }[user_type]()


if __name__ == '__main__':
    pass
