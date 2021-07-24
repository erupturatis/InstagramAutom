from instabot import Bot
from Vars import username,password

#venv -> Lib -> site-packages ->instabot->api->api_login.py-> comment 352,353,354

bot = Bot()
bot.login(username=username, password=password)

# medias = bot.get_total_user_medias("@lambo_turmoil")
# bot.download_photos(medias)