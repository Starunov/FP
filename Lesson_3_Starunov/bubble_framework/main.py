from datetime import datetime

from requests_type import GetRequest, PostRequest


class NotFound:
    def __call__(self, *args, **kwargs):
        return '404 NOT FOUND', '<h1>Sorry bro, page not found!</h1>'


class Framework:
    def __init__(self, routes, fronts: list = []):
        self.routes_dict = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']
        request = {}
        for front in self.fronts:
            front(request)

        if method == 'GET':
            rget = GetRequest(environ)
            path = rget.path
            params = rget.get_data
            print("Параметры переданные в строке запроса:", params, type(params))
            view = self.routes_dict.get(path, NotFound())
            code, body = view(request)
            start_response(code, [('content-type', 'text/html')])
            return [body.encode('utf-8')]

        elif method == 'POST':
            rpost = PostRequest(environ)
            params = rpost.get_data
            path = rpost.path
            print("Данные переданные POST запросом:", params, type(params))
            view = self.routes_dict[path]
            code, body = view(request)
            start_response(code, [('content-type', 'text/html')])
            return [body.encode('utf-8')]


