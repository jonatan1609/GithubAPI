from ..utils import Get
from .post_gist import Gist


def get_gist(
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> Gist:
    """
    Documentation for get_gist. Get information and content of a particular gist_id.
    :param gist_id: The desired gist.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `Gist` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    with Get(url, headers={"Accept": accept}) as response:
        return Gist(**response)
