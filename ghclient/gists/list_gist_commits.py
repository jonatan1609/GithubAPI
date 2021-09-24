from ..utils import Get
from .data_types import Commit
from typing import List


def list_gist_commits(
        gist_id: str,
        per_page: int = 30,
        page: int = 1,
        accept: str = "application/vnd.github.v3+json"
) -> List[Commit]:
    """
    Lists commits in a particular gist.
    :param gist_id: The particular gist to get its commits.
    :param per_page: Results per page (max 100). Default: 30
    :param page: Page number of the results to fetch. Default: 1
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `List[Commit]`
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/commits"

    with Get(
            url,
            headers={"Accept": accept},
            params={"per_page": per_page, "page": page},
    ) as response:
        return [Commit(**commit) for commit in response]
