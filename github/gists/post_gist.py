import dataclasses
import json
import typing
from .data_types import File, Gist
from ..utils import Post


def post_gist(
        token: str,
        description: str,
        contents: typing.Sequence[File],
        accept: str = "application/vnd.github.v3+json",
        public: bool = True,
):
    """
    Documentation for post_gist.
    Upload a new file (or some files at once) to gist.github.com.
    :param token: Your github token to perform actions.
    :param description: The description of the gist.
    :param contents: A list of File.
    :param accept: Default is application/vnd.github.v3+json.
    :param public: Determined whether the gist is public or private (secret).
    :return: `dict`
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = "https://api.github.com/gists"

    response = Post(
        url,
        headers={"Accept": accept},
        data=json.dumps({
            "description": description,
            "public": public,
            "files": {
                n: dataclasses.asdict(file) for n, file in enumerate(contents)
            }
        }),
        auth=("token", token),
    )
    with response:
        return Gist(**response)
