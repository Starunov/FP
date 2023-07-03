from main import Framework
from datetime import datetime


class DebugApp(Framework):
    def __init__(self, routes, fronts):
        self.app = Framework(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, environ, start_response):
        with open('debug_mode.txt', 'a', encoding='utf-8') as file:
            now = datetime.now()
            print(now, str(now))
            file.write(f'  {datetime.now()}  '.center(100, '=') + '\n')
            for k, v in environ.items():
                write = f'[{k}] -- [{v}]\n'
                file.write(write)
            file.write('\n')
        return self.app(environ, start_response)


class FakeApp(Framework):
    def __init__(self, routes, fronts):
        self.app = Framework(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']

