from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from helper.database import set,unset ,insert
from helper.list import list

@Client.on_message(filters.private &filters.command(['unset']))
async def unsetlg(client,message):
	unset(int(message.chat.id))
	await message.reply_text("Successfully removed custom default language")

@Client.on_message(filters.private &filters.command(['set']))
async def setlg(client,message):
    	    user_id = int(message.chat.id)
    	    insert(user_id)
    	    text = message.text
    	    textspit = text.split('/set')
    	    lg_code = textspit[1]
    	    if lg_code:
    	    		cd = lg_code.lower().replace(" ", "")
    	    		try:
    	    			lgcd = list[cd]
    	    		except:
    	    			await message.reply_text("❗️ This language Not available in My List \n Or Check Your spelling 😉",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Check List 📑" ,url="https://raw.githubusercontent.com/lntechnical2/Google-Translater-/main/List/list.txt")]]))
    	    			return
    	    		set(user_id,lgcd)
    	    		await message.reply_text(f"Successfully set custom default language **{cd}**")
    	    else:
    	    		await message.reply_text(" Please use this command with an argument. \n **For Example:/set English**",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("How To Use",url = "https://youtu.be/dUYvenXiYKE")]]))
