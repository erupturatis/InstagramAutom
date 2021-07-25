from instabot import Bot
from Vars import username,password
import os

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#lambo", image="Posts/post1.jpg"):
    bot = Bot()
    bot.login(username=username, password=password)
    standardSpace="\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
    bot.upload_photo(image, caption=caption+standardSpace+credit+standardSpace+hashtags)
    os.remove('Posts/post1.jpg.REMOVE_ME')

