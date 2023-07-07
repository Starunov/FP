from datetime import date

current_date = date.today().strftime('%A %d %B %Y')


def sidebar(request):
    request['tasks'] = [
        {
            'task_head': 'Добавить',
            'current_date': current_date,
            'task_body': 'Добавить базу данных к своему проекту',
            'mark': False,
        },
        {
            'task_head': 'Для этого использовать',
            'current_date': current_date,
            'task_body': 'Для этого использовать паттерн Data Mapper',
            'mark': False,
        },
        {
            'task_head': 'Использовать',
            'current_date': current_date,
            'task_body': 'Использовать паттерн Unit of Work',
            'mark': False,
        },
        {
            'task_head': 'Можно',
            'current_date': current_date,
            'task_body': 'Можно попробовать дополнительно реализовать Identity Map',
            'mark': False,
        },
    ]


tasks = [sidebar]
