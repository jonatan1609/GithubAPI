from ..utils import Get


def gist_is_starred(
        token: str,
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> bool:
    """
    Star a gist.
    :param token: User authentication.
    :param gist_id: gist to check if it's starred by the authenticated user or not.
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `bool` - True in case it's starred by the authenticated user, False otherwise.
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/star"

    request = Get(
            url,
            headers={"Accept": accept},
            auth=("token", token)
    )
    request.evaluate()
    if request.response.status_code == 404:
        return False
    request.response.raise_for_status()
    if request.response.status_code == 204:
        return True
