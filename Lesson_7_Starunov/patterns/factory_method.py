from models import Course, Student, Teacher


class CourseFactory:

    @staticmethod
    def create(name: str, category: object):
        return Course(name, category)


class UserFactory:
    @staticmethod
    def create(user_type, firstname, lastname, age):
        return {
            'student': Student,
            'teacher': Teacher,
        }[user_type](firstname, lastname, age)


if __name__ == '__main__':
    pass
