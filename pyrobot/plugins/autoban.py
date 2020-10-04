from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.admin_check import admin_check
from pyrobot.helper_functions.extract_user import extract_user
from pyrobot.helper_functions.string_handling import extract_time

from pyrobot.pyrobot import PyroBot

async def get_ban_command(message):
    chat_id = message.new_chat_members.id
    until_date_val = 1601779726
    try:
        await message.chat.kick_member(
            user_id=chat_id,
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
@PyroBot.on_message(filters.new_chat_members)
async def auto_ban(_, message):
       await get_ban_command(message)
