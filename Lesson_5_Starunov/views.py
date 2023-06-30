from bubble_framework.templator import render
from patterns.single_ton import Logger
from patterns.engine import Engine
from patterns.decorators import Route

site = Engine()
logger = Logger('default')


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
        contex = {
            **request,
            'title': 'Users',
            'user_page_selected': 'selected',
        }
        return '200 OK', render(template_name='user/users_list.html', **contex)


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
            print(method)

        elif method == 'POST':
            data = request.get('data')
            category_id = data.get('category_id')
            if not category_id:  # путая строка
                raise ValueError('Category not be empty')

            category = site.find_category_by_id(int(category_id))
            course = site.create_course(name=data['name'], category=category)
            site.courses.append(course)

        return '200 OK', render(template_name='course/courses_list.html', **contex)


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
