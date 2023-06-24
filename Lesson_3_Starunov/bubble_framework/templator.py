import os
from jinja2 import Environment, FileSystemLoader


BASE_DIR = os.getcwd()


def render(template_name, folder='templates', **kwargs):
    path = os.path.join(BASE_DIR, folder, template_name)
    with open(path, 'r', encoding='utf-8') as file:
        template = Environment(loader=FileSystemLoader(f'{folder}/')).from_string(file.read())

    return template.render(**kwargs)
