# created by :d

import pyrogram
from pyrogram import Client, filters, enums
from config import APP_ID, API_HASH, STRING_SESSION, MESAJ


userbot = Client(name='userbot', api_id=APP_ID, api_hash=API_HASH, session_string=STRING_SESSION, parse_mode=enums.ParseMode.HTML)
userbot.start()

@Client.on_message(filters.text & filters.private)
async def tsm(c: Client, m: "types.Message"):
    await m.reply_text(
        text=MESAJ,
        chat_id=chat_id)
       
