from instabot import Bot

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#lambo"):
    bot = Bot()
    bot.login(username="lamborify", password="Vulpea2012")
    image = "Posts/post1.jpg"
    bot.upload_photo(image, caption=caption+"\n"+credit+"\n\n Hashtags \n"+hashtags)

Post()