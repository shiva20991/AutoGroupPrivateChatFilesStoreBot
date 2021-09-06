# (c) @AbirHasan2005 & @HuzunluArtemis

import asyncio
from pyrogram import Client, filters, idle
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, ChatPermissions

from configs import Config
from handlers.database.access_db import db
from handlers.forcesub_handler import ForceSub
from handlers.forwarder_handler import forwardMessage
from handlers.send_mesage_handler import sendMessage
from handlers.database.add_user import AddUserToDatabase

User = Client( session_name=Config.STRING_SESSION, api_id=Config.API_ID,  api_hash=Config.API_HASH)
Bot = Client( session_name="Auto Group - Private Chat Files Store Bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@Bot.on_message(filters.private & (filters.document | filters.video | filters.audio) & ~filters.edited)
async def private_handler(bot: Client, cmd: Message):
    if Config.ACCEPT_FROM_PRIVATE:
        media = cmd.document or cmd.video
        if media.file_name.rsplit(".", 1)[-1] in Config.BLOCKED_EXTENSIONS:
            return
        if media.file_size < int(Config.MIN_FILE_SIZE):
            return
        if (Config.FORCE_SUB_CHANNEL is not None) and (cmd.from_user.is_bot is False):
            await AddUserToDatabase(cmd)
            Fsub = await ForceSub(Bot, cmd)
            if Fsub == 400:
                await db.set_joined_channel(cmd.from_user.id, joined_channel=False)
                await db.set_group_id(cmd.from_user.id, group_id=cmd.chat.id)
                try:
                    await bot.restrict_chat_member(
                        chat_id=cmd.chat.id,
                        user_id=cmd.from_user.id,
                        permissions=ChatPermissions(can_send_messages=False)
                    )
                except:
                    pass
                return
            elif Fsub == 404:
                try:
                    await bot.kick_chat_member(chat_id=cmd.chat.id, user_id=cmd.from_user.id)
                except:
                    pass
            else:
                await db.delete_user(cmd.from_user.id)
        #
        forward = await forwardMessage(cmd)
        #
        if Config.AUTO_DELETE:
            text = f"""
    ....................... ✅ Tamamlandı / Finished .......................

    🇹🇷 Bu dosya {Config.AUTO_DELETE_TIME} saniye içinde silinecektir. Ancak, veritabanıma kopyaladım! Aşağıdaki linkle sonsuza kadar sana ait.
    🇬🇧 This file will be deleted in {Config.AUTO_DELETE_TIME} seconds. But, I copied it to the my database! It's yours forever with the link below.

    ............................ 🌧 Details / Detaylar ............................

    🌈 File: `{media.file_name}`

    [☀️ Link](https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}): `https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}`"""
        else:
            text = f"""
    ....................... ✅ Tamamlandı / Finished .......................

    🌈 File: `{media.file_name}`

    [☀️ Link](https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}): `https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}`"""
        await sendMessage(
            bot=bot,
            message_id=cmd.message_id,
            chat_id=cmd.chat.id,
            text=text
        )
        if Config.AUTO_DELETE:
            await asyncio.sleep(int(Config.AUTO_DELETE_TIME))
            try:
                await cmd.delete(True)
            except Exception as err:
                print(f"Unable to Delete Media Message!\nError: {err}\n\nMessage ID: {cmd.message_id}")
    #






@User.on_message(filters.group & (filters.document | filters.video | filters.audio))
async def files_handler(bot: Client, cmd: Message):
    media = cmd.document or cmd.video
    if not cmd.from_user.is_bot:
        if cmd.edit_date is not None:
            return
    if media.file_name.rsplit(".", 1)[-1] in Config.BLOCKED_EXTENSIONS:
        return
    if media.file_size < int(Config.MIN_FILE_SIZE):
        return
    if (Config.FORCE_SUB_CHANNEL is not None) and (cmd.from_user.is_bot is False):
        await AddUserToDatabase(cmd)
        Fsub = await ForceSub(Bot, cmd)
        if Fsub == 400:
            await db.set_joined_channel(cmd.from_user.id, joined_channel=False)
            await db.set_group_id(cmd.from_user.id, group_id=cmd.chat.id)
            try:
                await bot.restrict_chat_member(
                    chat_id=cmd.chat.id,
                    user_id=cmd.from_user.id,
                    permissions=ChatPermissions(can_send_messages=False)
                )
            except:
                pass
            return
        elif Fsub == 404:
            try:
                await bot.kick_chat_member(chat_id=cmd.chat.id, user_id=cmd.from_user.id)
            except:
                pass
        else:
            await db.delete_user(cmd.from_user.id)
    #
    forward = await forwardMessage(cmd)
    #
    if Config.AUTO_DELETE:
        text = f"""
....................... ✅ Tamamlandı / Finished .......................

🇹🇷 Bu dosya {Config.AUTO_DELETE_TIME} saniye içinde silinecektir. Ancak, veritabanıma kopyaladım! Aşağıdaki linkle sonsuza kadar sana ait.
🇬🇧 This file will be deleted in {Config.AUTO_DELETE_TIME} seconds. But, I copied it to the my database! It's yours forever with the link below.

............................ 🌧 Details / Detaylar ............................

🌈 File: `{media.file_name}`

[☀️ Link](https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}): `https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}`"""
    else:
        text = f"""
....................... ✅ Tamamlandı / Finished .......................

🌈 File: `{media.file_name}`

[☀️ Link](https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}): `https://t.me/{Config.BOT_USERNAME}?start={Config.URL_PREFIX}_{str(forward.message_id)}`"""
    await sendMessage(
        bot=bot,
        message_id=cmd.message_id,
        chat_id=cmd.chat.id,
        text=text
    )
    if Config.AUTO_DELETE:
        await asyncio.sleep(int(Config.AUTO_DELETE_TIME))
        try:
            await cmd.delete(True)
        except Exception as err:
            print(f"Unable to Delete Media Message!\nError: {err}\n\nMessage ID: {cmd.message_id}")


@Bot.on_message(filters.private & filters.command("start") & ~filters.edited)
async def start_handler(bot: Client, event: Message):
    __data = event.text.split("_")[-1]
    if __data == "/start":
        await sendMessage(bot, Config.START_MESSAGE, event.message_id, event.chat.id)
    else:
        file_id = int(__data)
        try:
            if Config.SEND_AS_COPY:
                await bot.copy_message(chat_id=event.chat.id, from_chat_id=int(Config.DB_CHANNEL_ID), message_id=file_id)
            else:
                await bot.forward_messages(chat_id=event.chat.id, from_chat_id=int(Config.DB_CHANNEL_ID), message_ids=file_id)
        except:
            await sendMessage(bot, f"Unable to Get Message!\n\nContact / Bildir: {Config.CONTACT_ADRESS}", event.message_id, event.chat.id)

@Bot.on_message(filters.group & filters.text & ~filters.edited)
async def Fsub_handler(bot: Client, event: Message):
    if (Config.FORCE_SUB_CHANNEL is not None) and (event.from_user.is_bot is False):
        await AddUserToDatabase(event)
        Fsub = await ForceSub(Bot, event)
        if Fsub == 400:
            await db.set_joined_channel(event.from_user.id, joined_channel=False)
            await db.set_group_id(event.from_user.id, group_id=event.chat.id)
            try:
                await bot.restrict_chat_member(
                    chat_id=event.chat.id,
                    user_id=event.from_user.id,
                    permissions=ChatPermissions(can_send_messages=False)
                )
            except:
                pass
        elif Fsub == 404:
            try:
                await bot.kick_chat_member(chat_id=event.chat.id, user_id=event.from_user.id)
            except:
                pass
        else:
            await db.delete_user(event.from_user.id)


@User.on_chat_member_updated()
async def handle_Fsub_Join(bot: Client, event: Message):
    """
    Auto Unmute Member after joining channel.

    :param bot: pyrogram.Client
    :param event: pyrogram.types.Message
    """

    if Config.FORCE_SUB_CHANNEL:
        try:
            user_ = await bot.get_chat_member(event.chat.id, event.from_user.id)
            if user_.is_member is False:
                return
        except UserNotParticipant:
            return
        group_id = await db.get_group_id(event.from_user.id)
        group_message_id = await db.get_group_message_id(event.from_user.id)
        if group_id:
            try:
                await bot.unban_chat_member(chat_id=int(group_id), user_id=event.from_user.id)
                try:
                    await bot.delete_messages(chat_id=int(group_id), message_ids=group_message_id, revoke=True)
                except Exception as err:
                    print(f"Unable to Delete Message!\nError: {err}")
                await db.delete_user(user_id=event.from_user.id)
            except Exception as e:
                print(f"Skipping FSub ...\nError: {e}")

# Start User Client
User.start()
print("Userbot Started!")
# Start Bot Client
Bot.start()
print("Bot Started!")
# Loop Clients till Disconnects
idle()
# Stop User Client
User.stop()
print("\n")
print("Userbot Stopped!")
# Stop Bot Client
Bot.stop()
print("Bot Stopped!")
