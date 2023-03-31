from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_USERNAME, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://te.legra.ph/file/fcd0011f39b29c72eaa84.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [ÐJ 𓆩✘𝕯𓆪](tg://user?id=5161032951)🥀
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀʟᴘʜᴀ ʀᴏʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ - [ᴅᴊ](t.me/NooBpy).**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✰ ᴏᴡɴᴇʀ ✰", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "✰ ʀᴇᴘᴏ ✰",
                        url="https://te.legra.ph/file/805b5bd70b632c1d100ee.jpg",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✰ sᴏᴜʀᴄᴇ ✰"
_help__ = """ /repo to get repo 
             /Source to get repo
"""
