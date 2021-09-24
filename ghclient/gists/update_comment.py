from ..utils import Patch
from .data_types import Comment


def update_comment(
        token: str,
        gist_id: str,
        comment_id: int,
        comment_body: str,
        accept: str = "application/vnd.github.v3+json",
) -> Comment:
    """
    Delete a comment.

    :param token: Your github token to post a comment.
    :param gist_id: The gist to comment in.
    :param comment_id: The id of the comment.
    :param comment_body: The content of the comment.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `Comment` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/comments/{comment_id}"

    with Patch(
        url,
        headers={"Accept": accept},
        json={"body": comment_body},
        auth=("token", token),
    ) as response:
        return Comment(**response)
