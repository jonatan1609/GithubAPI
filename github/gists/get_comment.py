from .data_types import Comment
from ..utils import Get


def get_comment(
        gist_id: str,
        comment_id: int,
        accept: str = "application/vnd.github.v3+json",
) -> Comment:
    """
    Post a new comment.

    :param gist_id: The gist to comment in.
    :param comment_id: The id of the comment.
    :param accept: Default is application/vnd.github.v3+json.
    :return: `Comment` object
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/comments/{comment_id}"

    with Get(
        url,
        headers={"Accept": accept},
    ) as response:
        return Comment(**response)
