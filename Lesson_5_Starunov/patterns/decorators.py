class Route:
    routes = {}

    def __init__(self, url: str):
        self.url = url
        if not self.url.endswith('/'):
            self.url += '/'

    def __call__(self, cls):
        self.routes[self.url] = cls()
