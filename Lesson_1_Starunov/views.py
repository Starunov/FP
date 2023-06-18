from buble_framework.templator import render


class Home:
    def __call__(self, request):
        contex = {
            'title': 'Home',
        }
        return '200 OK', render(template_name='home.html', **contex)


class Examples:
    def __call__(self, request):
        contex = {
            'title': 'Examples',
        }
        return '200 OK', render(template_name='examples.html', **contex)


class Contacts:
    def __call__(self, request):
        context = {
            'title': 'Contacts',
        }
        return '200 OK', render(template_name='contacts.html', **context)
