from datetime import date

current_date = date.today().strftime('%A %d %B %Y')


def sidebar(request):
    request['tasks'] = [
        {
            'task_head': 'Внести изменения в wsgi-фреймворк,',
            'current_date': current_date,
            'task_body': 'Внести изменения в wsgi-фреймворк, '
                         'которые позволят использовать механизм наследования и включения шаблонов',
            'mark': True,
        },
        {
            'task_head': 'Создать',
            'current_date': current_date,
            'task_body': 'Создать базовый шаблон для всех страниц сайта',
            'mark': True,
        },
        {
            'task_head': 'Включенные шаблоны',
            'current_date': current_date,
            'task_body': 'Если нужно создать один или несколько включенных шаблонов',
            'mark': True,
        },
        {
            'task_head': 'Добавить',
            'current_date': current_date,
            'task_body': 'Добавить на сайт меню, которое будет отображаться на всех страницах',
            'mark': True,
        },
        {
            'task_head': 'Улучшить',
            'current_date': current_date,
            'task_body': 'Улучшить имеющиеся страницы с использованием базовых и включенных шаблонов',
            'mark': False,
        },
        {
            'task_head': 'Проверить',
            'current_date': current_date,
            'task_body': 'Проверить что фреймворк готов для дальнейшего использования, '
                         'при желании добавить какой либо полезный функционал',
            'mark': True,
        },

    ]


tasks = [sidebar]
