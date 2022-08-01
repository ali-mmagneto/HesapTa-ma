# created by :d

import re
import os
from os import environ
from pyrogram import Client
import tgcrypto


APP_ID = int(environ.get("APP_ID")) 
API_HASH = environ.get("API_HASH")
MESAJ = environ.get("MESAJ")

with Client(name='USS', api_id=APP_ID, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())

STRING_SESSION = app.export_session_string()

