import typing
import dataclasses
from .data_types import Gist, File
from ..utils import Patch


def update_gist(
    token: str,
    gist_id: str,
    description: str = None,
    files: typing.Sequence[File] = (),
    accept: str = "application/vnd.github.v3+json"
) -> Gist:
    """
    Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.

    :param token: Your github token to perform actions.
    :param gist_id: The ID of the gist.
    :param description: Description of the gist
    :param files: Names of files to be updated
    :param accept: Default: "application/vnd.github.v3+json"
    :return: `Gist` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    assert description or files, "You must specify either `description` or `files`"
    url = f"https://api.github.com/gists/{gist_id}"
    body = {}
    if description:
        body["description"] = description
    if files:
        body["files"] = {n: dataclasses.asdict(file) for n, file in enumerate(files)}
    with Patch(url, headers={"Accept": accept}, json=body, auth=("token", token)) as response:
        return Gist(**response)
