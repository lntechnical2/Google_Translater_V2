from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("API_ID",12345))

API_HASH = os.environ.get("API_HASH", "")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=APP_ID,
        plugins=plugins
    )
    app.run()
