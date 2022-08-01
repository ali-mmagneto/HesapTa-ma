# created by :d

import pyrogram
from pyrogram import Client, filters, __version__
from config import APP_ID, API_HASH, STRING_SESSION, MESAJ


UserBot = Client(
        name='userbot',
        session_string=STRING_SESSION, 
        api_id=APP_ID,
        api_hash=API_HASH
        )

@UserBot.on_message(filters.text & filters.private)
async def ubot(c: Client, m: "types.Message"):
    await m.reply_text(
        text=MESAJ,
        chat_id=chat_id,
        parse_mode=ParseMode.HTML
        )
       
UserBot.run()
