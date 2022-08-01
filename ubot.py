# created by :d

import pyrogram
from pyrogram.enums import ParseMode
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
        text=MESAJ.format(m.from_user.mention),
        parse_mode=ParseMode.HTML
        )
    print("{message.from.chat_id} is kiss you") 

Logger.info(m="UserBot is running #created by :d")        
UserBot.run() 
