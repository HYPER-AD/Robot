from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_USERNAME, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://te.legra.ph/file/ed51293271f2d67b56783.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [❥︎❥︎𝐼𝑇𝑆𝑀𝐸ت︎𝑽𝑰𝑽𝑬𝑲 亗](tg://user?id=5656382791)🥀
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅᴏʀᴀ ʀᴏʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ - [ᴘɪʀᴏᴋɪᴅ](t.me/pirokid).**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✰ ᴏᴡɴᴇʀ ✰", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "✰ ʀᴇᴘᴏ ✰",
                        url="https://t.me/vivekevil",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✰ sᴏᴜʀᴄᴇ ✰"
_help__ = """ /repo to get repo 
             /Source to get repo
"""
