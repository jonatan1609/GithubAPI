from ..utils import Delete


def delete_gist(
        token: str,
        gist_id: str,
        accept: str = "application/vnd.github.v3+json"
) -> None:
    """
    Delete a gist.
    :param token: Your github token to perform actions.
    :param gist_id: The ID of the gist.
    :param accept: Default: "application/vnd.github.v3+json"
    :return: None
    """
    url = f"https://api.github.com/gists/{gist_id}"
    with Delete(url=url, headers={"Accept": accept}, auth=("token", token)) as response:
        return response
