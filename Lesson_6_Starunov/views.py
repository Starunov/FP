from bubble_framework.templator import render
from patterns.single_ton import Logger
from patterns.engine import Engine
from patterns.decorators import Route
from patterns.notifications import EmailNotifier, SmsNotifier

site = Engine()
logger = Logger('default', writer='file')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()


@Route('/')
class Home:
    def __call__(self, request):
        logger.log('Вызван метод __call__ класса Home')
        contex = {
            **request,
            'title': 'Home',
            'home_page_selected': 'selected',
        }
        return '200 OK', render(template_name='home.html', **contex)


@Route('/users')
class UsersList:
    def __call__(self, request):
        context = {
            **request,
            'title': 'Users',
            'user_page_selected': 'selected',
            'students': site.students,
            'teachers': site.teachers,
        }

        method = request.get('method')

        if method == 'GET':
            data = request.get('data')
            if data:
                user = list(filter(lambda user: user.fullname == data.get('username'), site.students + site.teachers))[0]
                context = {
                    **context,
                    'user': user
                }
                return '200 OK', render('user/user_detail.html', **context)

        elif method == 'POST':
            data = request.get('data')
            age = data.get('age')
            if int(age) < 0 or int(age) > 100:
                context = {
                    **request,
                    'title': 'New user',
                }
                return '200 OK', render(template_name='user/create_user.html', **context)

            user = site.create_user(data.get('category'), data.get('firstname'), data.get('lastname'), data.get('age'))

            if data.get('category') == 'student':
                site.students.append(user)
            elif data.get('category') == 'teacher':
                site.teachers.append(user)

        return '200 OK', render(template_name='user/users_list.html', **context)


@Route('/create-user')
class CreateUser:
    def __call__(self, request):
        context = {
            **request,
            'title': 'New user',
        }
        return '200 OK', render(template_name='user/create_user.html', **context)


@Route('/courses')
class CoursesList:
    def __call__(self, request):
        contex = {
            **request,
            'title': 'Courses',
            'courses_page_selected': 'selected',
            'courses': site.courses,
        }

        method = request.get('method')

        if method == 'GET':
            data = request.get('data')
            if data:
                for course in site.courses:
                    if data.get('course_name') == course.name:
                        context = {
                            **request,
                            'title': course.name,
                            'categories': site.categories,
                            'name': course.name,
                            'category_id': course.category.id,
                            'students': course.students,
                        }
                        return '200 OK', render(template_name='course/edit_course.html', **context)

        elif method == 'POST':
            data = request.get('data')
            category = site.find_category_by_id(int(data.get('category_id')))
            is_exist = list(filter(lambda course: course.name == data.get('name'), site.courses))
            if not is_exist:
                course = site.create_course(name=data['name'], category=category)
                course.observers.append(email_notifier)
                course.observers.append(sms_notifier)
                site.courses.append(course)

        return '200 OK', render(template_name='course/courses_list.html', **contex)


@Route('/add-to-course')
class AddStudentToCourse:
    def __call__(self, request):
        data = request.get('data')

        method = request.get('method')

        if method == 'POST':
            course = site.get_course(data.get('course_name'))
            student = site.get_student(data.get('student'))
            course.add_student(student)

        context = {
            **request,
            'title': 'Add student',
            'course_name': data.get('course_name'),
            'students': site.students,
        }
        return '200 OK', render('course/add_student_to_course.html', **context)


@Route('/create-course')
class CreateCourse:
    def __call__(self, request):
        context = {
            **request,
            'title': 'Create course',
            'categories': site.categories,
        }
        return '200 OK', render(template_name='course/create_course.html', **context)


@Route('/categories')
class CategoriesList:
    def __call__(self, request):
        context = {
            **request,
            'title': 'Categories',
            'categories_page_selected': 'selected',
            'categories': site.categories
        }
        if request.get('method') == 'POST':
            category_name = request.get('data').get('name')

            if not category_name:  # пустая строка
                raise ValueError('Category name not be empty')

            category = site.create_category(category_name)

            if category not in site.categories:
                site.categories.append(category)

        if context.get('method') == 'GET':
            if request.get('data'):  # /categories?category_id=0
                cat_id = int(request.get('data').get('category_id'))
                try:
                    site.find_category_by_id(cat_id)
                    view = CategoryDetail(cat_id)
                except Exception:
                    view = NotFound()
                return view(request)

        return '200 OK', render(template_name='category/categories_list.html', **context)


class CategoryDetail:
    def __init__(self, category_id: int):
        self.category_id = category_id

    def __call__(self, request):
        category = site.find_category_by_id(self.category_id)
        context = {
            **request,
            'category': category
        }

        return '200 OK', render(template_name='category/category_detail.html', **context)


@Route('/create-category')
class CreateCategory:
    def __call__(self, request):
        context = {
            **request,
            'title': 'Create category',
        }
        return '200 OK', render(template_name='category/create_category.html', **context)


class NotFound:
    def __call__(self, *args, **kwargs):
        return '404 NOT FOUND', '<h1>Sorry bro, page not found!</h1>'
