# (c) @AbirHasan2005 & @HuzunluArtemis

import asyncio
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from configs import Config


async def forwardMessage(file: Message):
    try:
        if Config.SAVE_AS_COPY:
            data = await file.copy(chat_id=int(Config.DB_CHANNEL_ID))
        else:
            data = await file.forward(chat_id=int(Config.DB_CHANNEL_ID))
        return data
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait")
        await asyncio.sleep(e.x)
        await forwardMessage(file)
