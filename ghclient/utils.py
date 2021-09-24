import typing
from requests import get, post, patch, delete, put


class Request:
    response = ...
    is_json = True

    def __class_getitem__(cls, item):
        if isinstance(item, tuple):
            method, json = item
            self = cls(method)
            self.is_json = json
        else:
            self = cls(item)
        return self

    def __init__(self, method: typing.Callable):
        self.method = method

    def __call__(self, *args, **kwargs):
        new_self = self.__class__(self.method)
        new_self.is_json = self.is_json
        new_self.request_args = args, kwargs
        return new_self

    def evaluate(self):
        self.response = self.method(*self.request_args[0], **self.request_args[1])

    def __enter__(self):
        if self.response is Ellipsis:
            self.evaluate()
        self.response.raise_for_status()
        if self.response.text.strip():
            if self.response.status_code not in {200, 201}:
                raise RuntimeError(self.response.json()["message"])
            if self.is_json:
                return self.response.json()
            return self.response.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


Get = Request[get]
Post = Request[post]
Patch = Request[patch]
Delete = Request[delete, False]
Put = Request[put]
