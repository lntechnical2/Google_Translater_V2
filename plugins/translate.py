from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import database 

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
          await message.reply_text(
          text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",
          reply_to_message_id = message.message_id,
          reply_markup=InlineKeyboardMarkup(
            [ [ InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],[InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]   ]  ) )
            
