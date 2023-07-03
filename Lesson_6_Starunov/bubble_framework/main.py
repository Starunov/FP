from requests_type import GetRequest, PostRequest


class NotFound:
    def __call__(self, *args, **kwargs):
        return '404 NOT FOUND', '<h1>Sorry bro, page not found!</h1>'


class Framework:
    def __init__(self, routes, fronts: list = []):
        self.routes_dict = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        for front in self.fronts:
            front(request)

        request_type = None

        if method == 'GET':
            request_type = GetRequest(environ)
        elif method == 'POST':
            request_type = PostRequest(environ)

        request['data'] = request_type.params

        view = self.routes_dict.get(request_type.path, NotFound())
        code, body = view(request)
        start_response(code, [('content-type', 'text/html')])
        return [body.encode('utf-8')]
