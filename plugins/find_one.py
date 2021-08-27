import os
from pyrogram import Client ,filters
from helper.database import find_one
ADMIN = int(os.environ.get("ADMIN", 923943045))


@Client.on_message(filters.user(ADMIN) & filters.command(["find"]))
async def findmenb(bot, message):
		id = message.text.split("/find")
		user_id = id[1].replace(" ", "")
		await message.reply_text(find_one(int(user_id)))
