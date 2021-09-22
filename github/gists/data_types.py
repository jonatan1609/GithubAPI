import copy
import pickle
import dataclasses
import datetime
import re
import typing


def remove(*fields):
    def _(cls):
        ann = copy.copy(cls.__annotations__)
        for field in fields:
            del ann[field]
        return dataclasses.make_dataclass(cls.__name__, ann)
    return _


@dataclasses.dataclass(frozen=True)
class Field:
    type: typing.Any
    list: bool = False


class Custom:
    string_strip = re.compile(r"({/\w+})+")

    def __post_init__(self):
        # noinspection PyDataclass
        for f in dataclasses.fields(self):
            if isinstance(getattr(self, f.name), str):
                setattr(self, f.name, self.string_strip.sub("", getattr(self, f.name)))
            if isinstance(f.type, Field):
                if f.type.list:
                    setattr(self, f.name, [f.type.type(**i) for i in (
                        getattr(self, f.name).values()
                        if isinstance(getattr(self, f.name), dict)
                        else getattr(self, f.name)
                    )])
                else:
                    if f.type.type is str:
                        setattr(self, f.name, f.type.type(getattr(self, f.name)))
                    elif f.type.type is datetime.datetime:
                        setattr(self, f.name, datetime.datetime.strptime(getattr(self, f.name), "%Y-%m-%dT%H:%M:%SZ"))
                    else:
                        setattr(self, f.name, f.type.type(**getattr(self, f.name)))


@dataclasses.dataclass()
class File(Custom):
    filename: str
    content: str
    type: str = None
    language: str = None
    raw_url: str = None
    size: str = None
    truncated: bool = None


@dataclasses.dataclass()
class User(Custom):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


@dataclasses.dataclass()
class ForkUser(Custom):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: typing.Any
    company: typing.Any
    blog: str
    location: typing.Any
    email: typing.Any
    hireable: typing.Any
    bio: typing.Any
    twitter_username: typing.Any
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: Field(datetime.datetime)
    updated_at: Field(datetime.datetime)


@dataclasses.dataclass()
class Fork(Custom):
    url: str
    user: Field(ForkUser)
    id: str
    created_at: Field(datetime.datetime)
    updated_at: Field(datetime.datetime)


@dataclasses.dataclass()
class ChangeStatus:
    total: int
    additions: int
    deletions: int


@dataclasses.dataclass()
class Commit(Custom):
    user: Field(User)
    version: str
    committed_at: Field(datetime.datetime)
    change_status: Field(ChangeStatus)
    url: str


@dataclasses.dataclass()
class Gist(Custom):
    url: str
    forks_url: str
    commits_url: str
    id: str
    node_id: str
    git_pull_url: str
    git_push_url: str
    html_url: str
    files: Field(File, True)
    public: bool
    created_at: Field(datetime.datetime)
    updated_at: Field(datetime.datetime)
    description: str
    comments: int
    user: typing.Any
    comments_url: str
    owner: Field(User)
    forks: Field(Fork, True)
    history: Field(Commit, True)
    truncated: bool


@dataclasses.dataclass()
@remove("forks", "history")
class SearchResultGist(Gist):
    pass


@dataclasses.dataclass()
@remove("forks", "history", "truncated")
class ForkedGist(Gist):
    pass
