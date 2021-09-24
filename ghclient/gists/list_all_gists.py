from ..utils import Get
from .data_types import SearchResultGist
from typing import List


def list_all_gists(
        token: str = None,
        since: str = None,
        per_page: int = 30,
        page: int = 1,
        accept: str = "application/vnd.github.v3+json"
) -> List[SearchResultGist]:
    """
    Lists the authenticated user's gists *or if called anonymously, this endpoint returns all public gists*
    :param token: User authentication, if token is not supplied - this endpoint returns all public gists.
    :param since: Only show notifications updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
    Default: forever.
    :param per_page: Results per page (max 100). Default: 30
    :param page: Page number of the results to fetch. Default: 1
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `List[SearchResultGist]`
    :raises: `RuntimeError` in case one of the parameters is invalid.

    **Important: In order to retrieve Secret Gists too, you must not user a regular OAuth Token
    but a special token which is being used in a GitHub App.**
    """
    url = "https://api.github.com/gists"
    with Get(
            url,
            headers={"Accept": accept},
            params={"since": since, "per_page": per_page, "page": page},
            auth=("token", token)
    ) as response:
        return [SearchResultGist(**response) for response in response]
