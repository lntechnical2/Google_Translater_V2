from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from .helper import databse as data
from .helper import keybord as key

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
          data.insert(message.chat.id)
          await message.reply_text(
          text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",
          reply_to_message_id = message.message_id,
          reply_markup=InlineKeyboardMarkup(
            [ [ InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],[InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]   ]  ) )
            
@Client.on_message(filters.private & filters.text  )
async def echo(client, message):
	code = data.find(message.chat.id)
	if code :
			translator = Translator()
			translation = translator.translate(message.text,dest = code)
			await message.reply_text(translation.text)
	else:
		await  message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup =key.keybord1)

@Client.on_callback_query()
async def translate_text(bot,update):
      tr_text = update.message.reply_to_message.text
      cb_data = update.data
      if cb_data== "page2":
      	await update.message.edit("Select language 👇",reply_markup = key.keybord2)
      elif cb_data == "page1":
      	await update.message.edit("Select language 👇",reply_markup =key.keybord1)
      elif cb_data =="page3":
      	await update.message.edit("Select language 👇",reply_markup =key.keybord3)
      elif cb_data == "page4":
      	await update.message.edit("Select language 👇",reply_markup =key.keybord4)
      elif cb_data =="page5":
      	await update.message.edit("Select language 👇",reply_markup =key.keybord5)
      elif cb_data =="page6":
      	await update.message.edit("Select language 👇",reply_markup =key.keybord6)
      else :
      	translator = Translator()
      	translation = translator.translate(tr_text,dest = cb_data)
      	await update.message.edit(translation.text)
      				 					 			 			
