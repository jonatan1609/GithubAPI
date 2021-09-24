from ..utils import Put


def star_gist(
        token: str,
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> bool:
    """
    Star a gist
    :param token: User authentication.
    :param gist_id: Star the gist by the authenticated user.
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `bool` - True in case the gist was starred successfully.
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/star"

    request = Put(
            url,
            headers={"Accept": accept},
            auth=("token", token)
    )
    request.evaluate()
    request.response.raise_for_status()
    if request.response.status_code == 204:
        return True
    return False
