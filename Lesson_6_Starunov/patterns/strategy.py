import os


class ConsoleWriter:
    def write(self, text):
        print(text)


class FileWriter:
    def __init__(self, file_name, path=''):
        self.path = os.path.join(path, file_name)

    def write(self, text):
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(text)
