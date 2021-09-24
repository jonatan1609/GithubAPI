from ..utils import Get
from .data_types import Gist


def get_gist_revision(
        gist_id: str,
        sha: str,
        accept: str = "application/vnd.github.v3+json"
) -> Gist:
    """
    Star a gist
    :param gist_id: Star the gist by the authenticated user.
    :param sha: the revision sha.
    :param accept: Setting to application/vnd.github.v3+json is recommended.
    :return: `Gist` - The gist (the way it was in that revision).
    :raises: `RuntimeError` in case one of the parameters is invalid.
    """
    url = f"https://api.github.com/gists/{gist_id}/{sha}"

    with Get(
            url,
            headers={"Accept": accept}
    ) as response:
        return Gist(**response)

