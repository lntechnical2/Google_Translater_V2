from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)

@Client.on_inline_query()
async def inline(_, query: InlineQuery):
        string = query.query.lower()
        if string == "":
        	METHOD=  [ InlineQueryResultArticle( title="How To Use", input_message_content=InputTextMessageContent("Ex ; ```@Googletranslateitbot how to use # hi```"),description="{Text} # {language code} ",thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        	await query.answer( results=METHOD,  cache_time=2, switch_pm_text="Using Method",switch_pm_parameter="start" )
        else:
        	splitit = string.split("#")        	     	
        try:
        		cd = splitit[1].lower().replace(" ", "")
        		text = splitit[0]
        except:
        	METHOD=  [ InlineQueryResultArticle( title="How To Use", input_message_content=InputTextMessageContent("Ex ; ```@Googletranslateitbot how to use # hi```"),description="{Text}#{language code} ",thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        	await query.answer( results=METHOD,  cache_time=2, switch_pm_text="Using Method",switch_pm_parameter="start" )
        	return
        try:
        	translator = Translator()
        	translation = translator.translate(text,dest = cd)
        except:
        	return
        TRTEXT=  [ InlineQueryResultArticle( title=f"Translated from {translation.src} To {translation.dest}", input_message_content=InputTextMessageContent(translation.text),description=f'{translation.text}',thumb_url="https://tg-link.herokuapp.com/dl/0/AgADh60xG50-wFc.jpg")]
        try:
        	await query.answer(results=TRTEXT ,  cache_time=2, switch_pm_text="Google Translater",switch_pm_parameter="start")
        except:
        	return
