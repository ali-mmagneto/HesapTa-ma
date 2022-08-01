# created by :d


import logging
import pyrogram
from pyrogram.enums import ParseMode
from pyrogram import Client, filters, __version__
from config import APP_ID, API_HASH, STRING_SESSION, MESAJ


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

UserBot = Client(
        name='userbot',
        session_string=STRING_SESSION, 
        api_id=APP_ID,
        api_hash=API_HASH
        )

@UserBot.on_message(filters.text & filters.private & filters.incoming)
async def ubot(c: Client, m: "types.Message"):
    await m.reply_text(
        text=MESAJ.format(m.from_user.mention),
        parse_mode=ParseMode.HTML
        )
    print("{message.from.chat_id} is kiss you") 

LOGGER.info(msg="UserBot is running #created by :d")        
UserBot.run()
