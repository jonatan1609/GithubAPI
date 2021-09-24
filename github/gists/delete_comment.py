from ..utils import Delete


def delete_comment(
        token: str,
        gist_id: str,
        comment_id: int,
        accept: str = "application/vnd.github.v3+json",
) -> bool:
    """
    Delete a comment.

    :param token: Your github token to post a comment.
    :param gist_id: The gist to comment in.
    :param comment_id: The id of the comment.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `bool` - True in case the comment was deleted successfully.
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/comments/{comment_id}"

    request = Delete(
        url,
        headers={"Accept": accept},
        auth=("token", token),
    )

    request.evaluate()
    request.response.raise_for_status()
    if request.response.status_code == 204:
        return True
