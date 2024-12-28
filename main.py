from pyrogram import Client, idle
from pyrogram.enums import ParseMode
import configparser

config = configparser.ConfigParser()

try:
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
except FileNotFoundError:
    print("Error: config.ini not found.")
except configparser.NoSectionError:
    print("Error: 'bot' section not found in config.ini.")
except configparser.NoOptionError:
    print("Error: 'token' not found in 'bot' section in config.ini.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")
