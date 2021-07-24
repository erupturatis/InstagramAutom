from instabot import Bot
from Vars import username,password

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#lambo"):
    bot = Bot()
    bot.login(username=username, password=password)
    image = "Posts/post1.jpg"
    bot.upload_photo(image, caption=caption+"\n"+credit+"\n\n Hashtags \n"+hashtags)

