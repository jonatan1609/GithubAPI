from ..utils import Delete


def delete_gist(
        token: str,
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> bool:
    """
    Delete a gist.
    :param token: Your github token to perform actions.
    :param gist_id: The ID of the gist.
    :param accept: Default: "application/vnd.github.v3+json"
    :return: `bool` - True in case the gist was deleted successfully.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    request = Delete(url=url, headers={"Accept": accept}, auth=("token", token))

    request.evaluate()
    request.response.raise_for_status()
    if request.response.status_code == 204:
        return True
