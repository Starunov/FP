from wsgiref.simple_server import make_server

from bubble_framework.main import Framework
from bubble_framework.other_app import DebugApp, FakeApp
from views import Route
from tasks import tasks

routes = Route.routes

application = Framework(routes, tasks)

with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()
