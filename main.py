from pyrogram import Client, idle
from pyrogram.enums import ParseMode
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

token = config.get("bot", "token")


bot = Client(
    name="Feedback",
    api_id=2040,
    api_hash="b18441a1ff607e10a989891a5462e627",
    bot_token=token,
    in_memory=True,
    sleep_threshold=30,
    plugins=dict(root="plugins"),
    parse_mode=ParseMode.HTML
)

if __name__ == "__main__":
    bot.start()
    idle()
