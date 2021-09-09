import typing
from requests import get, post, patch, delete, put


class Request:
    response = ...

    def __class_getitem__(cls, item):
        return cls(item)

    def __init__(self, method: typing.Callable):
        self.method = method

    def __call__(self, *args, **kwargs):
        self.request_args = args, kwargs
        return self

    def evaluate(self):
        self.response = self.method(*self.request_args[0], **self.request_args[1])

    def __enter__(self):
        if self.response is Ellipsis:
            self.evaluate()
        if self.response.status_code not in {200, 201}:
            raise RuntimeError(self.response.json()["message"])
        return self.response.json()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


Get = Request[get]
Post = Request[post]
Patch = Request[patch]
Delete = Request[delete]
Put = Request[put]
