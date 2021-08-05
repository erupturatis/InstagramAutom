from instabot import Bot
from Vars import usernames,passwords
import os

first=0
bot = Bot()

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#lambo", image="Posts/post1.jpg", p=0):
    global first
    global bot

    bot.login(username=usernames[p], password=passwords[p], is_threaded=True )
    standardSpace="\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
    bot.upload_photo(image, caption=caption+standardSpace+credit+standardSpace+hashtags)
    os.remove('Posts/post1.jpg.REMOVE_ME')
    bot.logout()


