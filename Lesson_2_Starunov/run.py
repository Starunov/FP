import paths
from wsgiref.simple_server import make_server

from bubble_framework.main import Framework
from urls import routes


application = Framework(routes)

with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()
