# created by :d

import pyrogram
from pyrogram import Client
from config import APP_ID, API_HASH, STRING_SESSION, MESAJ


ubot = Client(name='ubot', api_id=APP_ID, api_hash=API_HASH, session_string=STRING_SESSION)


@Client.on_message(filter.text & filter.private)
async def tsm(c: Client, m: "types.Message"):
    await m.reply_text(
        text=MESAJ,
        chat_id=chat_id)

ubot.run()
       
