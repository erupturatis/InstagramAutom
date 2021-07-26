from instabot import Bot
from Vars import usernames,passwords
import os

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#lambo", image="Posts/post1.jpg", p=0):
    bot = Bot()
    bot.login(username=usernames[p], password=passwords[p])
    standardSpace="\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
    bot.upload_photo(image, caption=caption+standardSpace+credit+standardSpace+hashtags)
    os.remove('Posts/post1.jpg.REMOVE_ME')

