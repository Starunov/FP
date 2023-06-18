class NotFound:
    def __call__(self, *args, **kwargs):
        return '404 NOT FOUND', '<h1>Sorry bro, page not found</h1>'


class Framework:
    def __init__(self, routes):
        self.routes_dict = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path += '/'

        view = self.routes_dict.get(path, NotFound())
        request = {}
        code, body = view(request)
        start_response(code, [('content-type', 'text/html')])
        return [body.encode('utf-8')]
