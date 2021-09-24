import copy
import dataclasses
import datetime
import re
import typing


def remove(*fields):
    def _(cls):
        fields_copy = copy.copy(cls.__dataclass_fields__)
        annotations_copy = copy.deepcopy({**getattr(cls, "__use_annotations__", {}), **cls.__annotations__})
        for field in fields:
            del fields_copy[field]
            del annotations_copy[field]
        d_cls = dataclasses.make_dataclass(cls.__name__, annotations_copy, bases=(Custom,))
        d_cls.__dataclass_fields__ = fields_copy
        return d_cls
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
    # Only for type annotations:
    created_at: datetime.datetime
    updated_at: datetime.datetime
    # real fields:
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
    # Only for type annotations:
    user: ForkUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
    # real fields:
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
    # Only for type annotations:
    user: User
    committed_at: datetime.datetime
    change_status: ChangeStatus
    # real fields:
    user: Field(User)
    version: str
    committed_at: Field(datetime.datetime)
    change_status: Field(ChangeStatus)
    url: str


@dataclasses.dataclass()
class Gist(Custom):
    # Only for type annotations:
    files: typing.List[File]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner: User
    forks: typing.List[Fork]
    history: typing.List[Commit]
    # real fields:
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


@remove("forks", "history", "truncated")
class ForkedGist(Gist):
    pass


@remove("content", "truncated")
class NoContentFile(File):
    pass


@remove("forks", "history")
@dataclasses.dataclass()  # In case we don't leave the class body empty we need to re-create the dataclass.
class Forked(Gist):
    # Only for type annotations:
    files: typing.List[NoContentFile]
    # real fields:
    files: Field(NoContentFile, True)
    __use_annotations__ = Gist.__annotations__


class SearchResultGist(Forked):
    pass


@dataclasses.dataclass()
class Comment(Custom):
    # Only for type annotations:
    user: User
    created_at: datetime.datetime
    updated_at: datetime.datetime
    # real fields:
    url: str
    id: int
    node_id: str
    user: Field(User)
    author_association: str
    created_at: Field(datetime.datetime)
    updated_at: Field(datetime.datetime)
    body: str
