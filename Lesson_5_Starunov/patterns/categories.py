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


if __name__ == '__main__':
    prog_cat = Category('programming')
    prog_cat.courses.append('Python')
    prog_cat.courses.append('Java')

    design_cat = Category(name='design')
    design_cat.courses.append('3DMax')
    design_cat.courses.append('Kompas 3D')

    print(prog_cat.courses, '\t\t', prog_cat.id)
    print(design_cat.courses, '\t\t', design_cat.id)

    find = Category.find_category(1)
    print(find.name, find.courses)

