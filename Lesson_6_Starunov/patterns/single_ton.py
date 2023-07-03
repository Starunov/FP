from datetime import datetime

from strategy import FileWriter, ConsoleWriter


class MetaSingleTon(type):
    def __init__(cls, cls_name: str, cls_bases: tuple or list, cls_attrs: dict):
        super().__init__(cls_name, cls_bases, cls_attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        name = args[0] if args else kwargs.get('name', None)
        if cls.__instance.get(name) is None:
            cls.__instance[name] = super().__call__(*args, **kwargs)
        return cls.__instance.get(name)


class Logger(metaclass=MetaSingleTon):
    def __init__(self, log_name: str, writer='console'):
        self.log_name = log_name

        self.writer = {
            'file': FileWriter(self.log_name),
            'console': ConsoleWriter(),
        }[writer]

    def log(self, text):
        text = f'[{datetime.now()}] - {text}\n'
        self.writer.write(text)

