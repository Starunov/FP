from requests_type import GetRequest, PostRequest


class NotFound:
    def __call__(self, *args, **kwargs):
        return '404 NOT FOUND', '<h1>Sorry bro, page not found</h1>'


class Framework:
    def __init__(self, routes):
        self.routes_dict = routes

    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']

        if method == 'GET':
            rget = GetRequest(environ)
            path = rget.path
            params = rget.get_data
            print("Параметры переданные в строке запроса:", params, type(params))
            view = self.routes_dict.get(path, NotFound())
            request = {}
            code, body = view(request)
            start_response(code, [('content-type', 'text/html')])
            return [body.encode('utf-8')]

        elif method == 'POST':
            rpost = PostRequest(environ)
            params = rpost.get_data
            print("Данные переданные POST запросом:", params, type(params))
            # редирект на главную
            view = self.routes_dict['/']
            request = {}
            code, body = view(request)
            start_response(code, [('content-type', 'text/html')])
            return [body.encode('utf-8')]


