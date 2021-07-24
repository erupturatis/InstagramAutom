from instagramy import InstagramPost

def GetLikes(str):
    post = InstagramPost(str)
    return post.number_of_likes


def GetComments(str):
    post = InstagramPost(str)
    return post.number_of_comments

