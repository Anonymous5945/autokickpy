
import time
from pyrogram import Client, filters

from pyrobot.pyrobot import PyroBot

from pyrobot import AUTH_CHANNEL, LIMIT_ID , group_id


async def get_forward_command(message):
   for m in message:
        try:
            await client.forward_messages(
                  chat_id=-1001428281865,
                  from_chat_id=message.chat.id,
                  message_ids=message.message_id
              )
            await asyncio.sleep(3)
        except Exception as error:
            await message.reply_text(
                str(error)
            )















@PyroBot.on_message(filters.chat(chats=AUTH_CHANNEL) & filters.incoming)
async def auto_forward(_, message):
       await get_forward_command(message)
