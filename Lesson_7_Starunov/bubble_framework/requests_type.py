from urllib.parse import unquote


class Request:
    def __init__(self, environ: dict):
        self.environ = environ

    @property
    def path(self):
        """
        Проверяет наличие завершающего слеша в url-адресе, если нет, то подставляет его.
        """
        path = self.environ.get('PATH_INFO', '')

        if not path.endswith('/'):
            path += '/'
        return path

    @staticmethod
    def parse_query_string(query_string: str) -> dict:
        query_string_decode = unquote(query_string)
        params_lst = query_string_decode.split('&')
        d = {}
        for param in params_lst:
            k, v = param.split('=')
            d[k] = v.replace('+', ' ')
        return d


class GetRequest(Request):

    @property
    def params(self):
        """
        Возвращает словарь с параметрами заданные в строке запроса,
        None если параметры не заданы
        """
        query_string = self.environ.get('QUERY_STRING')
        if query_string:
            return self.parse_query_string(query_string)


class PostRequest(Request):

    @property
    def params(self):
        val = self.environ.get('CONTENT_LENGTH') or 0
        data_bytes = self.environ['wsgi.input'].read(int(val))
        data = data_bytes.decode('utf-8')
        return self.parse_query_string(data)
