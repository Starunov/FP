from bubble_framework.templator import render


class Home:
    def __call__(self, request):
        contex = {
            **request,
            'title': 'Home',
            'home_selected': 'selected',
        }
        return '200 OK', render(template_name='home.html', **contex)


class Examples:
    def __call__(self, request):
        contex = {
            **request,
            'title': 'Examples',
            'examples_selected': 'selected',
        }
        return '200 OK', render(template_name='examples.html', **contex)


class Contacts:
    def __call__(self, request):
        context = {
            **request,
            'title': 'Contacts',
            'contacts_selected': 'selected',
        }
        return '200 OK', render(template_name='contacts.html', **context)
