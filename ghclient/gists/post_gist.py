import dataclasses
import typing
from .data_types import File, Gist
from ..utils import Post


def post_gist(
        token: str,
        description: str,
        contents: typing.Sequence[File],
        accept: str = "application/vnd.github.v3+json",
        public: bool = True,
) -> Gist:
    """
    Allows you to add a new gist with one or more files.

    Note: Don't name your files "gistfile" with a numerical suffix.
    This is the format of the automatic naming scheme that Gist uses internally.

    :param token: Your github token to perform actions.
    :param description: The description of the gist.
    :param contents: A list of File.
    :param accept: Default is application/vnd.github.v3+json.
    :param public: Determined whether the gist is public or private (secret).
    :return: `Gist` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = "https://api.github.com/gists"

    request = Post(
        url,
        headers={"Accept": accept},
        json={
            "description": description,
            "public": public,
            "files": {
                n: dataclasses.asdict(file) for n, file in enumerate(contents)
            }
        },
        auth=("token", token),
    )

    with request as response:
        return Gist(**response)
