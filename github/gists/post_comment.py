from .data_types import Comment
from ..utils import Post


def post_comment(
        token: str,
        gist_id: str,
        comment_body: str,
        accept: str = "application/vnd.github.v3+json",
) -> Comment:
    """
    Post a new comment.

    :param token: Your github token to post a comment.
    :param gist_id: The gist to comment in.
    :param comment_body: The content of the comment.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `Comment` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/comments"

    request = Post(
        url,
        headers={"Accept": accept},
        json={"body": comment_body},
        auth=("token", token),
    )

    with request as response:
        return Comment(**response)
