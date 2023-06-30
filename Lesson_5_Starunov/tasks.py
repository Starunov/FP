from datetime import date

# current_date = date.today().strftime('%A %d %B %Y')
current_date = 'Saturday 24 June 2023'


def sidebar(request):
    request['tasks'] = [
        {
            'task_head': 'Добавить декоратор',
            'current_date': current_date,
            'task_body': 'Добавить декоратор для добавления связки url-view в приложение, '
                         'чтобы можно было добавлять url-ы, как в фреймворке Flask @app(‘/some_url/’)',
            'mark': True,
        },
        {
            'task_head': 'декоратор @debug',
            'current_date': current_date,
            'task_body': 'Добавить декоратор @debug, для view, если мы указываем данный декоратор над view, '
                         'то в терминал выводятся название функции и время ее выполнения',
            'mark': False,
        },
        {
            'task_head': 'Добавить подкатегории',
            'current_date': current_date,
            'task_body': 'Добавить подкатегорий. Т.е. категория курса может входит в другую категорию, '
                         'а может не входить и вложенность может быть любая. '
                         'Например: Программирование->Web->Python->Django. '
                         'После на страницу списка категорий добавить вывод количества курсов в каждой из категорий. '
                         'Например Программирование - 10, Web - 5, Python - 3, …',
            'mark': False,
        },
        {
            'task_head': 'Добавить 2 новых вида wsgi-application',
            'current_date': current_date,
            'task_body': 'Добавить 2 новых вида wsgi-application. Первый - логирующий (такой же как основной, '
                         'только он для каждого запроса выводит информацию (тип запроса и параметры) в консоль. '
                         'Второй - фейковый (на все запросы пользователя отвечает “200 OK”, “Hello from Fake”)',
            'mark': True,
        },
    ]


tasks = [sidebar]
