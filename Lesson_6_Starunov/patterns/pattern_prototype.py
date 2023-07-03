from copy import deepcopy


class CoursePrototype:
    def clone(self):
        return deepcopy(self)
