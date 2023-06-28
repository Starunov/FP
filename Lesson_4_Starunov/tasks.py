from datetime import date

# current_date = date.today().strftime('%A %d %B %Y')
current_date = 'Saturday 24 June 2023'


def sidebar(request):
    request['tasks'] = [
        {
            'task_head': 'Тема может быть любая',
            'current_date': current_date,
            'task_body': 'Тема (чему мы будем обучать) может быть любая, что вам больше нравиться '
                         '(например: продажа пирожков, йоге, администрированию, …)',
            'mark': True,
        },
        {
            'task_head': 'Минимальный функционал сайта',
            'current_date': current_date,
            'task_body': 'Создание категории курсов <br>'
                         'Вывод списка категорий <br>'
                         'Создание курса <br>'
                         'Вывод списка курсов <br>',
            'mark': True,
        },
    ]


tasks = [sidebar]
