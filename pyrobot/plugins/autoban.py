import time
from pyrogram import Client, filters

from pyrobot.pyrobot import PyroBot

from pyrobot import AUTH_CHANNEL, lD_LIMIT

async def get_ban_command(message):
    until_date_val = int(time.time() + 31)
    for member in message.new_chat_members:
        try:
            if member.id >= lD_LIMIT:
              await message.chat.kick_member(
                  user_id=member.id,
                  until_date=until_date_val
              )
        except Exception as error:
            await message.reply_text(
                str(error)
            )
@PyroBot.on_message(filters.chat(chats=AUTH_CHANNEL) & filters.new_chat_members)
async def auto_ban(_, message):
       await get_ban_command(message)
