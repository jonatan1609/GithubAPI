from ..utils import Get
from .data_types import SearchResultGist
from typing import List


def list_user_gists(
        username: str,
        since: str = None,
        per_page: int = 30,
        page: int = 1,
        accept: str = "application/vnd.github.v3+json"
) -> List[SearchResultGist]:
    """
    Lists public gists for the specified user:

    :param since: Only show notifications updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
    Default: forever.
    :param per_page: Results per page (max 100). Default: 30
    :param page: Page number of the results to fetch. Default: 1
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `List[SearchResultGist]`
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/users/{username}/gists"
    with Get(
            url,
            headers={"Accept": accept},
            params={"since": since, "per_page": per_page, "page": page},
    ) as response:
        return [SearchResultGist(**gist) for gist in response]
