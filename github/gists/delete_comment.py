from ..utils import Delete


def delete_comment(
        token: str,
        gist_id: str,
        id: int,
        accept: str = "application/vnd.github.v3+json",
):
    """
    Delete a comment.

    :param token: Your github token to post a comment.
    :param gist_id: The gist to comment in.
    :param id: The id of the comment.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `Comment` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/comments/{id}"

    request = Delete(
        url,
        headers={"Accept": accept},
        auth=("token", token),
    )

    request.evaluate()
    request.response.raise_for_status()
    if request.response.status_code == 204:
        return True