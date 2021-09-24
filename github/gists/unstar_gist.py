from ..utils import Delete


def unstar_gist(
        token: str,
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> bool:
    """
    Unstar a gist.
    :param token: User authentication.
    :param gist_id: Unstar the gist by the authenticated user.
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `bool` - True in case the gist was unstarred successfully.
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/star"

    request = Delete(
            url,
            headers={"Accept": accept},
            auth=("token", token)
    )
    request.evaluate()

    if request.response.status_code == 204:
        return True
    return False
