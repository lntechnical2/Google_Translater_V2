from pyrogram import Client, filters
from googletrans import Translator


@Client.on_message(filters.group & filters.command(["tr"]))
async def grouptrans(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			await message.reply_text(translation.text)
		except :
			print("error")
	else:
			 print("error")
			 
