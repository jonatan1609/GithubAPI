import typing
from requests import get, post


class Request:
    response = ...

    def __class_getitem__(cls, item):
        return cls(item)

    def __init__(self, method: typing.Callable):
        self.method = method

    def __call__(self, *args, **kwargs):
        self.response = self.method(*args, **kwargs)
        return self

    def __enter__(self):
        if self.response.status_code not in {200, 201}:
            raise RuntimeError(self.response.json()["message"])
        return self.response.json()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


Get = Request[get]
Post = Request[post]
