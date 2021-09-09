from github.gists.post_gist import post_gist, File
from github.gists import get_gist


TOKEN = "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"
#print(post_gist(TOKEN, "ABC", [File("A", "B")], public=False).id)
print(get_gist("819820f2f31fea8363ab73bce193a249"))