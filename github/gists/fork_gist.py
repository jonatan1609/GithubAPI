from ..utils import Post
from .data_types import Forked


def fork_gist(
        token: str,
        gist_id: str = None,
        accept: str = "application/vnd.github.v3+json"
) -> Forked:
    """
    Fork a particular gist.
    :param token: The token to authenticate the user in order to fork the gist.
    :param gist_id: The particular gist to get its forks.
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `Forked`
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/forks"

    with Post(
            url,
            headers={"Accept": accept},
            auth=("token", token)
    ) as response:
        return Forked(**response)
